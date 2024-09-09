# Name: ConvertMapServerCacheStorageFormat.py
# Description: The following stand-alone script demonstrates how to convert map
#               server cache storage format to the alteranate storage format for
#               a weblayers/map or image service based on
#               ArcGIS Enterprise or a stand alone ArcGIS Server

import arcpy
import os

# Sign in to portal
myPortal= "https://www.myArcGISEnterprise.com/webadaptor"
arcpy.SignInToPortal(myPortal, "MyUserName", "MyPassword")
serviceName= "MyCounty"
serviceType= "MapServer"
myPortalServiceURL = (myPortal + "/" + "rest/services" +"/" + serviceName + "/" + serviceType)


# Stand alone ArcGIS Server
target_server_connection = r"C:\Project\gisserver.ags.esri.com (publisher).ags"
serviceName= "MyCounty"
serviceType= "MapServer"
myServerServiceURL= target_server_connection + "/" + serviceName + "." + serviceType

# Variables for reporting
currentTime = datetime.datetime.now()
arg1 = currentTime.strftime("%H-%M")
arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
file = 'C:/results/report_%s.txt' % arg1

# Print results of the script to a report
report = open(file,'w')

try:
    #result = arcpy.server.ConvertMapServerCacheStorageFormat(myPortalServiceURL, -1)
    result = arcpy.server.ConvertMapServerCacheStorageFormat(myServerServiceURL, -1)
    while result.status < 4:
        time.sleep(0.2)
    resultValue = result.getMessages()
    report.write ("completed " + str(resultValue))
    
except Exception as e:
    
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    report.write("Failed at step 1 \n" "Line %i" % tb.tb_lineno)
    report.write(e.message)
report.close()

print ("Converted Map Server Cache Storage format for " + serviceName)