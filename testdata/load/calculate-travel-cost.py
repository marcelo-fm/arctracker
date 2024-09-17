# Name: CalculateTravelCost_Ex_02.py
# Description: Calculates for each cell the least accumulative cost distance
#    to the nearest source over a cost  surface. 
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inSource = 'https://MyPortal.esri.com/server/rest/services/Hosted/landuse/ImageServer'
outDistName = 
inCostRast = "costraster"
inElev = "elevation"
maxDist = "50000"

inHoriz = "backlink2"
horizFactor = "FORWARD 0.5 1.0"
inVertical = "focalcost.tif"
verticalFactor = "Binary 1.0 -30 30"

sourceCostMultiplier =
sourceStartCost =
sourceResistanceRate =
sourceCapacity = 
sourceTravelDirection =

optBacklinkName = "c:/sapyexamples/output/pathbacklink"
optAlloName =
allocField = 

# Execute CalculateTravelCost
arcpy.ra.CalculateTravelCost(inSource, outDistName, inCostRast, inElev, maxDist, inHoriz, horizFactor,
                           inVertical, verticalFactor, sourceCostMultiplier, sourceStartCost,
                           sourceResistanceRate, sourceCapacity, sourceTravelDirection, optBacklinkName,
                           optAlloName, allocField)

# Execute CostDistance
outTravelCost = CalculateTravelCost(inSourceData, inCostRaster, maxDistance, outBkLinkRaster)