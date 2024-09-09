# Description: Creates a series of strip map index features based on inputed
# line features with index feature dimensions specified in map units, the
# starting page number is 5 and the strip map direction is
# East-West/South-North.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:\data\ProjectData.gdb"

# Set local variables
inFeatures = "line"
outFeatureClass = "indexFeatures"
lenA = "10 Kilometers"
lenP = "5 Kilometers"
startingPageNum = "5"
directionType = "EW_SN"

# Execute StripMapIndexFeatures
arcpy.StripMapIndexFeatures_cartography(inFeatures, outFeatureClass, "", "",
                                        lenA, lenP, "", "", startingPageNum,
                                        directionType)