# Name: DistanceAccumulation_Ex_02.py
# Description: Calculates the distance accumulation.
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inputSourceRasterOrFeatures = 'https://MyPortal.esri.com/server/rest/services/Hosted/sources/ImageServer'
outputDistanceAccunulationName = "outDistAccum"
inputBarrierRasterOrFeatures  = 'https://MyPortal.esri.com/server/rest/services/Hosted/barrier/ImageServer'
inputSurfaceRaster = 'https://MyPortal.esri.com/server/rest/services/Hosted/surface/ImageServer'
inputCostRaster = 'https://MyPortal.esri.com/server/rest/services/Hosted/cost/ImageServer'
inputVerticalRaster = 'https://MyPortal.esri.com/server/rest/services/vertical/sources/ImageServer'
verticalFactor = ""
inputHorizontalRaster = 'https://MyPortal.esri.com/server/rest/services/Hosted/horizontal/ImageServer'
horizontalFactor = ""
outputBackDirectionRasterName = "outBackDir"
outputSourceDirectionRasterName = "outSourceDir"
outputSourceLocationRasterName = "outSourceLocation"
sourceInitialAccumulation = "IntitalAccum"
sourceMaximumAccumulation = "500000"
sourceCostMultiplier = "CostMultiplier"
sourceDirection = "FROM_SOURCE"
distanceMethod = "PLANAR"

# Execute 
arcpy.ra.DistanceAccumulation(inputSourceRasterOrFeatures, outputDistanceAccumulationName,
                            inputBarrierRasterOrFeatures, inputSurfaceRaster,
                            inputCostRaster, inputVerticalRaster, verticalFactor,
                            inputHorizontalRaster, horizontalFactor,
                            outputBackDirectionRasterName, outputSourceDirectionRasterName,
                            outputSourceLocationRasterName, sourceInitialAccumulation,
                            sourceMaximumAccumulation,sourceCostMultiplier, sourceDirection, distanceMethod)