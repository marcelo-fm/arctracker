# Description: Use SummarizeNearby to summarize population

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/city.gdb"

# Set local variables
newStore = "new_store_location"
censusInfo = "census_blocks"
outFeatureClass = "crimes_aggregated"
distanceType = "TRAVEL_TIME"
distance = "10;20"
distanceUnit = "Minutes"
time = "10/15/2014 2:14:19 PM"
timeZone = "GEOLOCAL"
keepPolys = True
sumFields = [["Pop2010", "Sum"],["OWNERS", "Sum"]]
addShapeSum = True

arcpy.analysis.SummarizeNearby(newStore, censusInfo, outFeatureClass, 
                               distanceType, distance, distanceUnit,
                               time, timeZone, keepPolys, sumFields,
                               addShapeSum)