# Name: CalculateDistance_Ex_02.py
# Description: Calculates for each cell the Euclidean distance, direction and allocation
#              to the nearest source.
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inSourceData = 'https://MyPortal.esri.com/server/rest/services/Hosted/reccenter/ImageServer'
outDistanceName = "eucdistance"
maxDistance = "4000"
cellSize = "10"
outDirectionName = "eucdirect"
outAllocationName = "eurallocation"
allocationField = "dataid"


# Execute EucDistance
arcpy.ra.CalculateDistance(inSourceData, outDistanceName, maxDistance, cellSize, outDirectionName,
                           outAllocationName, allocationField)