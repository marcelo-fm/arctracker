# Name: DissolveNetwork_Workflow.py
# Description: Creates a new network dataset with reduced number of line
#              features in a new file geodatabase workspace. The network dataset
#              is also built so that it can be used to perform network analyses.
# Requirements: Network Analyst Extension

#Import system modules
import arcpy

try:
    #Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")
    
    #Set environment settings
    arcpy.env.workspace = "C:/data/SanFrancisco.gdb"
    arcpy.env.overwriteOutput = True

    #Set local variables
    inNetworkDataset = "Transportation/Streets_ND"
    outFolder = "C:/data/output"
    outputGDBName = "SanFranciscoDissolved"

    #Create a new file geodatabase that will contain the dissolved network
    result = arcpy.CreateFileGDB_management(outFolder, outputGDBName)

    #Get the path to the newly created file gdb from the result object.
    outputGDB = result.getOutput(0)

    #Dissolve the network dataset
    result = arcpy.DissolveNetwork_na(inNetworkDataset, outputGDB)

    #Get the path to the dissolved network dataset from the result object
    dissolvedNetworkDataset = result.getOutput(0)

    #The dissolved network dataset is unbuilt. So build the network dataset
    arcpy.BuildNetwork_na(dissolvedNetworkDataset)

    print("Script completed successfully")

except Exception as e:
    print(e)