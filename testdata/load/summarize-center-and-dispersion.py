# Name: SummarizeCenterAndDispersion.py
# Description: Calculate the directionality and movement of fire occurrences 
#              over time. This sample calculates a mean center and a standard 
#              deviational ellipse.
# Requirements: ArcGIS Pro Advanced license 

# Import system modules
import arcpy

# Set local variables
inFeatures = r"c:\data\MyBigDataConnection.bdc\fire_incidents"
outMeanCenter = r"c:\data\FireIncidents.gdb\fires_meancenter"
outEllipse = r"c:\data\FireIncidents.gdb\fires_ellipse"


# Run SummarizeCenterAndDispersion
arcpy.gapro.SummarizeCenterAndDispersion(inFeatures, "", outMeanCenter, "", 
                                         outEllipse, "2_STANDARD_DEVIATIONS")