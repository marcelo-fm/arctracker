# gridindexfeatures_example5.py
# Description: Creates Grid Index Features by specifying the origin
# coordinates, the index feature dimensions in page units, the number of
# rows, the number of columns, 5 as the starting page number and labeling
# to start at the origin
# Author: ESRI

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:\data\ProjectData.gdb"
env.outputCoordinateSystem = arcpy.SpatialReference("North America Albers Equal Area Conic.prj")

# Set local variables
outFeatureClass = "gridIndexFeatures"
usePageUnit = "USEPAGEUNIT"
scale = "100000"
polygonWidth = "1000 meters"
polygonHeight= "1000 meters"
originCoord = "-6000000 -1600000"
numberRows = "15"
numberColumns = "20"
startingPageNum = "5"
labeling = "LABELFROMORIGIN"


# Execute GridIndexFeatures
arcpy.GridIndexFeatures_cartography(outFeatureClass, "", "", usePageUnit,
                                    scale, polygonWidth, polygonHeight,
                                    originCoord, numberRows, numberColumns,
                                    startingPageNum, labeling)