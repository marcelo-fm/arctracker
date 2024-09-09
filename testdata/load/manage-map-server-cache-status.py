# Name: ManageMapServerCacheStatus.py
# Description: The following stand-alone script demonstrates how to delete
# Status of cache using ManageMapServerCachStatus tool
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
serviceName = "Rainfall.MapService"
inputService = connectionFile + "\\" + server + "\\" + serviceName
scales = ""
manageMode = "DELETE_CACHE_STATUS"
numOfCachingServiceInstances = "2"
outputFolder = ""
areaOfInterest = ""
reportExtents = ""


currentTime = datetime.datetime.now()
arg1 = currentTime.strftime("%H-%M")
arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
file = 'C:/data/report_%s.txt' % arg1

# print results of the script to a report
report = open(file,'w')

# use "scales[0]","scales[-1]","scales[0:3]"

try:
    starttime = time.clock()
    result = arcpy.server.ManageMapServerCacheStatus(inputService,
                                                     manageMode, scales,
                                                     numOfCachingServiceInstances,
                                                     outputFolder,
                                                     areaOfInterest,
                                                     reportExtents)
    finishtime = time.clock()
    elapsedtime = finishtime - starttime

    #print messages to a file
    while result.status < 4:
        time.sleep(0.2)
    resultValue = result.getMessages()
    report.write ("completed " + str(resultValue))

    print("Reported the Bundle status for scale =" + str(scales[-1]) + "of " + \
        serviceName + "at " + outputFolder + "\n using specified feature class " + \
        areaOfInterest + " in " + str(elapsedtime) + " sec \n on " + arg2)

except Exception as e:
    # If an error occurred, print line number and error message
    tb = sys.exc_info()[2]
    report.write("Failed at step 3 \n" "Line %i" % tb.tb_lineno)
    report.write(str(e))

report.close()