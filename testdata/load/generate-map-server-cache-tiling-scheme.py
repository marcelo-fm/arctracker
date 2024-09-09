# Name: GeneateMapServerCacheTilingScheme.py
# Description: The following stand-alone script demonstrates how to create map
#               server cache schema using a given map document at a given
#               "pathForOutputXml"
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
mapDocument = "C:/data/101/Portland/mxd/_M_Portland_classic_FGDB_Local.mxd"
dataFrame = ""
outputTilingScheme = "C:/data/port.xml"
tileOrigin = ""
numOfScales = "4"
scales = "500000,250000,125000,64000"
tileSize = "256 x 256"
dotsPerInch = "96"

currentTime = datetime.datetime.now()
arg1 = currentTime.strftime("%H-%M")
arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
file = r'C:/data/report_%s.txt' % arg1

# print results of the script to a report
report = open(file,'w')

try:
    starttime = time.clock()
    result = arcpy.server.GenerateMapServerCacheTilingScheme(mapDocument, dataFrame,
                                                             tileOrigin, outputTilingScheme,
                                                             numOfScales, scales,
                                                             dotsPerInch, tileSize)
    finishtime = time.clock()
    elapsedtime = finishtime-starttime

    #print messages to a file
    while result.status < 4:
        time.sleep(0.2)
    resultValue = result.getMessages()
    report.write ("completed " + str(resultValue))

    print(" Created MapServer cache tiling schema successfully using" + \
        mapDocument + " at "+ outputTilingScheme + " in " + str(elapsedtime) + \
        " sec \n on " + arg2)

except Exception as e:
    # If an error occurred, print line number and error message
    tb = sys.exc_info()[2]
    report.write("Failed at step 1 \n" "Line %i" % tb.tb_lineno)
    report.write(str(e))

print("Created Map server Cache Tiling schema ")

report.close()