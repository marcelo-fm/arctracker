'''****************************************************************************
       Name: Tile & Classify LAS Files
Description: Creates & classifies tiled LAS files.
****************************************************************************'''
# Import system modules
import arcpy
import tempfile
import math

in_las = arcpy.GetParameterAsText(1) # The LAS files that need to be tiled
out_folder = arcpy.GetParameterAsText(2) # folder for LAS files
basename = arcpy.GetParameterAsText(3) # basename for output files
out_lasd = arcpy.GetParameterAsText(4) # output LAS dataset


try:
    # Create temp LAS dataset to reference LAS files that will be tiled
    temp_lasd = arcpy.CreateUniqueName('temp.lasd', tempfile.gettempdir())
    arcpy.management.CreateLasDataset(in_las, temp_lasd)
    arcpy.ddd.TileLas(temp_lasd, out_folder, basename, out_lasd, las_version=1.4, 
                      point_format=7, file_size=300)
    arcpy.management.Delete(temp_lasd)
    arcpy.ddd.ClassifyLasGround(out_lasd, method='AGGRESSIVE')
    arcpy.ddd.ClassifyLasBuilding(out_lasd, min_height='3 Meters', min_area='4 Meters')
    arcpy.ddd.ClassifyLasByHeight(out_lasd, height_classification=[(3, 6), (4,20), (5,70)],
                                  noise='All Noise', compute_stats='COMPUTE_STATS')

except arcpy.ExecuteError:
    print(arcpy.GetMessages())