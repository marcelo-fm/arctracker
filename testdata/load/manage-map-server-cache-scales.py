# Name: ManageMapServerCacheScales.py
# Description: The following stand-alone script demonstrates how to add a new 
#               scale in a tiling scheme for a map or image service.
#               This tool only works for weblayers/services based on
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

desiredScales= "18055.954822;9027.977411;4513.988705;2256.994353;1128.497176;564.248588;282.124294;141.062147;70.5310735;35.2655"

# Variables for reporting
currentTime = datetime.datetime.now()
arg1 = currentTime.strftime("%H-%M")
arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
file = 'C:/results/report_%s.txt' % arg1

# Print results of the script to a report
report = open(file,'w')

try:
    result = arcpy.server.ManageMapServerCacheScales(myServerServiceURL, desiredScales)
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

print ("Updated Cache Tiling Scales for " + serviceName)