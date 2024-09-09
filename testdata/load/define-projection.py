# Name: DefineProjection.py 
# Description: Records the coordinate system information for the specified input dataset or feature class

# import system modules
import arcpy

# set workspace environment
arcpy.env.workspace = "C:/data"

try:
    # set local variables
    in_dataset = "citylim_unk.shp" #"forest.shp"
    
    # get the coordinate system by describing a feature class
    dsc = arcpy.Describe("citylim_utm11.shp")
    coord_sys = dsc.spatialReference
    
    # run the tool
    arcpy.DefineProjection_management(in_dataset, coord_sys)
    
    # print messages when the tool runs successfully
    print(arcpy.GetMessages(0))
    
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
    
except Exception as ex:
    print(ex.args[0])