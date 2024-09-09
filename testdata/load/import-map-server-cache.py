# Name: ImportMapServerCache.py
# Description: The following stand-alone script demonstrates how to import map
#               server cache from a source directory with Tile Package to an existing service for
#               the default number of scales specified using an AOI by uploading data to remote server
# To Import cache tiles for the scales specified for given feature class

# Requirements: os, sys, time and traceback modules
# Author: ESRI

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
sourceCacheType = "TILE_PACKAGE"
sourceCacheDataset = ""
sourceTilePackage = "C:\\data\\destination_folder\\TPK\\Rainfall.tpk"
uploadDataToServer = "UPLOAD_DATA"
scales = [500000,250000,125000,64000]
numOfCachingServiceInstances = "2"
cacheDir = "c:\\arcgisserver\\arcgiscache"
areaOfInterest = "C:/data/101/Portland/Portland_Metro.shp"
importExtents = ""
overwriteTiles = "MERGE"

currentTime = datetime.datetime.now()
arg1 = currentTime.strftime("%H-%M")
arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
file = 'C:/data/report_%s.txt' % arg1

# print results of the script to a report
report = open(file,'w')

# use "scales[0]","scales[-1]","scales[0:3]"

try:
    starttime = time.clock()
    result = arcpy.server.ImportMapServerCache(inputService, sourceCacheType,
                                               sourceCacheDataset,
                                               sourceTilePackage,
                                               uploadDataToServer, scales,
                                               numOfCachingServiceInstances,
                                               areaOfInterest, importExtents,
					       overwriteTiles)
    finishtime = time.clock()
    elapsedtime = finishtime - starttime
    #print messages to a file
    while result.status < 4:
        time.sleep(0.2)
    resultValue = result.getMessages()
    report.write ("completed " + str(resultValue))

    print("Imported Map server Cache Tiles successfully for " + serviceName + \
        " from " + sourceTilePackage + " to " + cacheDir + "\n using "+ areaOfInterest + \
        " in " + str(elapsedtime) + " sec \n on  " + arg2)

except Exception as e:
    # If an error occurred, print line number and error message
    tb = sys.exc_info()[2]
    report.write("Failed at step 2 \n" "Line %i" % tb.tb_lineno)
    report.write(str(e))

report.close()

print("Imported Map server Cache Tiles for the given feature class")