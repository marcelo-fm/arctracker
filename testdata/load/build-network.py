# Name: BuildNetwork_ex02.py
# Description: Build a network dataset.
# Requirements: Network Analyst Extension 

#Import system modules
import arcpy
from arcpy import env
import sys
import os
import shutil

try:
    #Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")
    
    #Set environment settings
    env.workspace = "C:/data/SanFrancisco.gdb"
    
    #Set local variables
    inNetworkDataset = "Transportation/Streets_ND"
    
    #Build the network dataset
    arcpy.BuildNetwork_na(inNetworkDataset)
    
    #If there are any build errors, they are recorded in a BuildErrors.txt file
    #present in the system temp directory. So copy this file to the directory
    #containing this script
    
    #First get the path to the system temp directory
    tempDir = os.environ.get("TEMP")
    if tempDir:
        shutil.copy2(os.path.join(tempDir,"BuildErrors.txt"),sys.path[0])
    
    print("Script completed successfully.")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))