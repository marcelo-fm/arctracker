'''****************************************************************************
       Name: Extract Building Footprints
Description: Extract footprint from lidar points classified as buildings, 
             regularize its geometry, and calculate the building height.

****************************************************************************'''
import arcpy

lasd = arcpy.GetParameterAsText(0)
footprint = arcpy.GetParameterAsText(1)

try:
    lasd_layer = 'building points'
    arcpy.management.MakeLasDatasetLayer(lasd, lasd_layer, class_code=6)
    temp_raster = 'in_memory/bldg_raster'
    arcpy.management.LasPointStatsAsRaster(lasd_layer, temp_raster,
                                           'PREDOMINANT_CLASS', 'CELLSIZE', 2.5)
    temp_footprint = 'in_memory/footprint'
    arcpy.conversion.RasterToPolygon(temp_raster, temp_footprint)
    arcpy.ddd.RegularizeBuildingFootprint(temp_footprint, footprint, 
                                          method='RIGHT_ANGLES')
    arcpy.ddd.LasPointStatsByArea(lasd_layer, footprint, ['MIN_Z', 'MAX_Z'])
    arcpy.management.AddField(footprint, 'Height', 'Double')
    arcpy.management.CalculateField(footprint, 'Height', 
                                    "round('!Z_Max! - !Z_Min!', 2)", 
                                    'PYTHON_9.3')


except arcpy.ExecuteError:
    print(arcpy.GetMessages())