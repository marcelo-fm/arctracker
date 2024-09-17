# Name: GroupByProximity.py
# Description: Group roads together that touch
#
# Requirements: An advanced license

# Import system modules
import arcpy

# Set local variables
inFeatures = "C:\myData\cities.gdb\roads"
outname = "groupedRoads"
overlayType = "TOUCHES"

# Run Group By Proximity
result = arcpy.gapro.GroupByProximity(inFeatures, outname, overlayType)