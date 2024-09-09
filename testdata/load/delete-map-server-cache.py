# Name: DeleteMapServerCache.py
# Description: The following stand-alone script demonstrates how to delete map server cache
#              tiles if the corresponding cache schema or tiles has been created
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

# List of variables for mapservice properties
connectionFile = r"C:\Users\<username>\AppData\Roaming\ESRI\Desktop10.1\ArcCatalog"
server = "arcgis on MyServer_6080 (publisher)"
serviceName = "Rainfall.MapServer"
inputService = connectionFile + "\\" + server + "\\" + serviceName
numOfCachingServiceInstances = 2


currentTime = datetime.datetime.now()
arg1 = currentTime.strftime("%H-%M")
arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
file = 'C:/data/report_%s.txt' % arg1

# print results of the script to a report
report = open (file,'w')

# To Recreate all the tiles for the default number of scales generated
try:
    starttime = time.clock()
    result = arcpy.server.DeleteMapServerCache(inputService,
                                               numOfCachingServiceInstances)
    finishtime = time.clock()
    elapsedtime = finishtime - starttime

    #print messages to a file
    while result.status < 4:
        time.sleep(0.2)
    resultValue = result.getMessages()
    report.write ("completed " + str(resultValue))

    print("Deleted cache tiles & schema for mapservice " + serviceName + \
        "\n  in " + str(elapsedtime) + " sec \n on " + arg2)

except Exception as e:
    # If an error occurred, print line number and error message
    tb = sys.exc_info()[2]
    report.write("Failed at \n" "Line %i" % tb.tb_lineno)
    report.write(str(e))


print("Deleted Map server Cache Tiles ")

report.close()