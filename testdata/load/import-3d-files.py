'''****************************************************************************
Name: Import3DFiles Example
Description: This script demonstrates how to use the
             ListFiles method to collect all OpenFlight (*.flt) models in a
             workspace as input for the Import3DFiles tool.
****************************************************************************'''

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set Local Variables
OpenFlightList = arcpy.ListFiles("*.flt")
CS = "Coordinate Systems/Geographic Coordinate Systems/World/WGS 1984.prj"
outputFC = "Test.gdb/OpenFlight_Models"
if len(OpenFlightList) > 0:
    # Execute Import3DFiles
    arcpy.Import3DFiles_3d(OpenFlightList, outputFC, False, CS, False)
else:
    # Returned if there are no flt files in the target workspace
    print("There are no OpenFlight files in the " + env.workspace + " directory.")