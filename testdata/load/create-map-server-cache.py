# Name: CreateMapServerCache.py
# Description: The following stand-alone script demonstrates how to create map
#               using existing predefined schema
# Requirements: os, sys, time & traceback modules

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
serviceCacheDirectory = "C:\\arcgisserver\\directories\\arcgiscache"
tilingSchemeType = "PREDEFINED"
scalesType = ""
tileOrigin = ""
scalesType = ""
numOfScales = ""
scales = ""
dotsPerInch = "96"
tileSize = "256 x 256"
cacheTileFormat = "MIXED"
tileCompressionQuality = "75"
storageFormat = "COMPACT"
predefinedTilingScheme = "C:/data/TilingSchemes/ArcGIS_Online_Bing_Maps_Google_Maps.xml"


currentTime = datetime.datetime.now()
arg1 = currentTime.strftime("%H-%M")
arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
file = 'C:/data/report_%s.txt' % arg1

# print results of the script to a report
report = open(file,'w')

try:
    starttime = time.clock()
    result = arcpy.server.CreateMapServerCache(inputService,
                                               serviceCacheDirectory,
                                               tilingSchemeType, scalesType,
                                               numOfScales, dotsPerInch,
                                               tileSize, predefinedTilingScheme,
                                               tileOrigin, scales,
                                               cacheTileFormat,
                                               tileCompressionQuality,
                                               storageFormat)

    finishtime = time.clock()
    elapsedtime = finishtime - starttime

    #print messages to a file
    while result.status < 4:
        time.sleep(0.2)
    resultValue = result.getMessages()
    report.write ("completed " + str(resultValue))

    print("Created cache schema using predefined tiling schema for " + \
        serviceName + " in " + str(elapsedtime) + " sec \n on " + arg2)

except Exception as e:
    # If an error occurred, print line number and error message
    tb = sys.exc_info()[2]
    report.write("Failed at step 1 \n" "Line %i" % tb.tb_lineno)
    report.write(str(e))

print("Executed creation of map server Cache schema using tiling scheme")
report.close()