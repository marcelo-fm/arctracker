'''****************************************************************************
Name: Split Large LAS File
Description: Divides a large LAS file whose point distribution covers the full
             XY extent of the data into smaller files to optimize performance
             when reading lidar data.
****************************************************************************'''
# Import system modules
import arcpy
import tempfile
import math

in_las_file = arcpy.GetParameterAsText(0)
tile_width = arcpy.GetParameter(1) # double in LAS file's XY linear unit
tile_height = arcpy.GetParameter(2) # double in LAS file's XY linear unit
out_folder = arcpy.GetParameterAsText(3) # folder for LAS files
out_name_suffix = arcpy.GetParameterAsText(4) # basename for output files
out_lasd = arcpy.GetParameterAsText(5) # output LAS dataset


try:
    temp_lasd = arcpy.CreateUniqueName('temp.lasd', tempfile.gettempdir())
    arcpy.management.CreateLasDataset(in_las_file, temp_lasd, 
                                      compute_stats='COMPUTE_STATS')
    desc = arcpy.Describe(temp_lasd)
    total_columns = int(math.ceil(desc.extent.width/tile_width))
    total_rows = int(math.ceil(desc.extent.height/tile_height))
    digits = int(math.log10(max(cols, rows))) + 1
    for row in range(1, total_rows+1):
        yMin = desc.extent.YMin + tile_height*(row-1)
        yMax = desc.extent.YMin + tile_height*(row)
        for col in range (1, total_columns+1):
            xMin = desc.extent.XMin + tile_width*(col-1)
            xMax = desc.extent.XMax + tile_width*(col)
            name_suffix = '_{0}_{1}x{2}'.format(out_name_suffix, 
                                                str(row).zfill(digits), 
                                                str(col).zfill(digits))
            arcpy.ddd.ExtractLas(temp_lasd, out_folder, 
                                 arcpy.Extent(xMin, yMin, xMax, yMax),
                                 name_suffix=name_suffix, 
                                 rearrange_points='REARRANGE_POINTS',
                                 compute_stats='COMPUTE_STATS')
    arcpy.env.workspace = out_folder
    arcpy.management.CreateLasDataset(arcpy.ListFiles('*{0}*.las'.format(out_name_suffix)),
                                      out_lasd, compute_stats='COMPUTE_STATS',
                                      relative_paths='RELATIVE_PATHS')
except arcpy.ExecuteError:
    print(arcpy.GetMessages())