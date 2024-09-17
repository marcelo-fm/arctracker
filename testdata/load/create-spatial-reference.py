# This script reprojects a shapefile in Redlands folder
# from NAD 1983 UTM Zone 11N
# to NAD 1983 StatePlane California V FIPS 0405 (US Feet)

# import system modules
import arcpy
 
try:
    # set the workspace environment
    arcpy.env.workspace = r"C:\data\Redlands"

    # create a spatial reference object to be used as output coordinate system
    out_sr = arcpy.CreateSpatialReference_management("NAD 1983 StatePlane California V FIPS 0405 (US Feet)")

    # use the output of CreateSpatialReference as input to Project tool
    # to reproject the shapefile
    arcpy.Project_management("citylimit_Project1.shp", "city_CA_FIPS0405", out_sr)

except arcpy.ExecuteError:
    # print geoprocessing message
    print(arcpy.GetMessages(2))
          
except Exception as ex:
    # print the exception message
    print(ex.args[0])