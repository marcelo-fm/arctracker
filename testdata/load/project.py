# Name: Project_Example2.py

# Description: Project all feature classes in a geodatabase
# Requirements: os module

# Import system modules
import arcpy
import os

# Set environment settings
arcpy.env.workspace = "C:/data/Redlands.gdb"
arcpy.env.overwriteOutput = True

# Set local variables
outWorkspace = "C:/data/Redlands_utm11.gdb"

try:
    # Use ListFeatureClasses to generate a list of inputs 
    for infc in arcpy.ListFeatureClasses():
    
        # Determine if the input has a defined coordinate system, can't project it if it does not
        dsc = arcpy.Describe(infc)
    
        if dsc.spatialReference.Name == "Unknown":
            print('skipped this fc due to undefined coordinate system: ' + infc)
        else:
            # Determine the new output feature class path and name
            outfc = os.path.join(outWorkspace, infc)
            
            # Set output coordinate system
            outCS = arcpy.SpatialReference('NAD 1983 UTM Zone 11N')
            
            # run project tool
            arcpy.Project_management(infc, outfc, outCS)
            
            # check messages
            print(arcpy.GetMessages())
            
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
    
except Exception as ex:
    print(ex.args[0])