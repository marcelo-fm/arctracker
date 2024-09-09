# Description: Select features within a distance

# Import arcpy and set path to data
import arcpy

arcpy.env.workspace = r"c:\data\mexico.gdb"

arcpy.management.SelectLayerByLocation('cities', 'WITHIN_A_DISTANCE', 
                                       'chihuahua', '1.5 Miles')
arcpy.management.SelectLayerByLocation('cities', 'WITHIN_A_DISTANCE_GEODESIC', 
                                       'chihuahua', '200 Kilometers')

# When using WITHIN_A_DISTANCE, if distance units are not specified, the 
# distance value is assumed to be in the units of the input dataset's coordinate 
# system
arcpy.management.SelectLayerByLocation('cities', 'WITHIN_A_DISTANCE', 
                                       'chihuahua', '200')

# When using WITHIN_A_DISTANCE_GEODESIC, if distance units are not specified, 
# the distance value is assumed to be in meters
arcpy.management.SelectLayerByLocation('cities', 'WITHIN_A_DISTANCE_GEODESIC', 
                                       'chihuahua', '200')