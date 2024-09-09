'''****************************************************************************
       Name: Classify Lidar & Extract Building Footprints
Description: Extract footprint from lidar points classified as buildings, 
             regularize its geometry, and calculate the building height.

****************************************************************************'''
import arcpy

lasd = arcpy.GetParameterAsText(0)
dem = arcpy.GetParameterAsText(1)
footprint = arcpy.GetParameterAsText(2)

try:
    desc = arcpy.Describe(lasd)
    if desc.spatialReference.linearUnitName in ['Foot_US', 'Foot']:
        unit = 'Feet'
    else:
        unit = 'Meters'
    ptSpacing = desc.pointSpacing * 2.25
    sampling = '{0} {1}'.format(ptSpacing, unit)
    # Classify overlap points
    arcpy.ddd.ClassifyLASOverlap(lasd, sampling)
    # Classify ground points
    arcpy.ddd.ClassifyLasGround(lasd)
    # Filter for ground points
    arcpy.management.MakeLasDatasetLayer(lasd, 'ground', class_code=[2])
    # Generate DEM
    arcpy.conversion.LasDatasetToRaster('ground', dem, 'ELEVATION', 
                                        'BINNING NEAREST NATURAL_NEIGHBOR', 
                                        sampling_type='CELLSIZE', 
                                        sampling_value=desc.pointSpacing)
    # Classify noise points
    arcpy.ddd.ClassifyLasNoise(lasd, method='ISOLATION', edit_las='CLASSIFY', 
                               withheld='WITHHELD', ground=dem, 
                               low_z='-2 feet', high_z='300 feet', 
                               max_neighbors=ptSpacing, step_width=ptSpacing, 
                               step_height='10 feet')
    # Classify buildings
    arcpy.ddd.ClassifyLasBuilding(lasd, '7.5 feet', '80 Square Feet')
    #Classify vegetation
    arcpy.ddd.ClassifyLasByHeight(lasd, 'GROUND', [8, 20, 55], 
                                  compute_stats='COMPUTE_STATS')
    # Filter LAS dataset for building points
    lasd_layer = 'building points'
    arcpy.management.MakeLasDatasetLayer(lasd, lasd_layer, class_code=[6])
    # Export raster from lidar using only building points
    temp_raster = 'in_memory/bldg_raster'
    arcpy.management.LasPointStatsAsRaster(lasd_layer, temp_raster,
                                           'PREDOMINANT_CLASS', 'CELLSIZE', 2.5)
    # Convert building raster to polygon
    temp_footprint = 'in_memory/footprint'
    arcpy.conversion.RasterToPolygon(temp_raster, temp_footprint)
    # Regularize building footprints
    arcpy.ddd.RegularizeBuildingFootprint(temp_footprint, footprint, 
                                          method='RIGHT_ANGLES')

except arcpy.ExecuteError:
    print(arcpy.GetMessages())