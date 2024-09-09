# Name: ExportMapServerCache.py
# Description: The following stand-alone script demonstrates how to export cache
#               as TILE_PACKAGE for default number of scales of a service, to a
#               TARGET_CACHE_PATH which is inaccessible to server instances using
#               COPY_DATA_FROM_SERVER
# Requirements: os, sys, time and traceback modules

# Any line that begins with a pound sign is a comment and will not be executed
# Empty quotes take the default value.
# To accept arguments from the command line replace values of variables to
#                                                           "sys.argv[]"

# Import system modules
import arcpy
from arcpy import env
import os, sys, time, datetime, traceback, string

# Set environment settings
env.workspace = "C:/data"

# List of input variables for map service properties
connectionFile = r"C:\Users\<username>\AppData\Roaming\ESRI\Desktop10.1\ArcCatalog"
server = "arcgis on MyServer_6080 (publisher)"
serviceName = "Rainfall.MapServer"
inputService = connectionFile + "\\" + server + "\\" + serviceName
targetCachePath = "C:/temp/usa"
exportCacheType = "TILE_PACKAGE"
copyDataFromServer = "COPY_DATA"
storageFormat = "COMPACT"
scaleValues = [500000,250000,125000,64000]
numOfCachingServiceInstances = "2"
exportExtents = ""
areaOfInterest = ""
overwriteTiles = "MERGE"

currentTime = datetime.datetime.now()
arg1 = currentTime.strftime("%H-%M")
arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
file = 'C:/data/report_%s.txt' % arg1

# print results of the script to a report
report = open(file,'w')

# use "scaleValues[0]","scaleValues[-1]","scaleValues[0:3]"

try:
    starttime = time.clock()
    result = arcpy.server.ExportMapServerCache(inputService, targetCachePath,
                                               exportCacheType,
                                               copyDataFromServer,
                                               storageFormat, scales,
                                               numOfCachingServiceInstances,
                                               areaOfInterest,
                                               exportExtents, overwriteTiles)
    finishtime = time.clock()
    elapsedtime = finishtime - starttime

    #print messages to a file
    while result.status < 4:
        time.sleep(0.2)
    resultValue = result.getMessages()
    report.write ("completed " + str(resultValue))

    print("Exported cache successfully for mapservice " + serviceName + " to " + \
        targetCachePath + " in " + str(elapsedtime) + " sec \n on" + arg2)

except Exception as e:
    # If an error occurred, print line number and error message
    tb = sys.exc_info()[2]
    report.write("Failed at step 1 \n" "Line %i" % tb.tb_lineno)
    report.write(str(e))

print("Exported Map server Cache ")

report.close()