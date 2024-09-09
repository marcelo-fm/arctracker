# import module
import arcpy

# Set geoprocessing workspace environment
arcpy.env.workspace = "c:/data"

# Set variables 
infc = "Blocks"
field = "POP2000"
outfc = "PopHotSpots"
neighbors = 10

# Run the CalculateDistanceBand tool to get a distance for use with the Hot Spot 
# tool from the tool result object
mindist, avgdist, maxdist = arcpy.stats.CalculateDistanceBand(infc, neighbors, 
                                                              "EUCLIDEAN_DISTANCE")
 
# Run the Hot Spot Analysis tool, using the maxdist output from the Calculate 
# Distance Band tool as an input
arcpy.stats.HotSpots(infc, field, outfc, "Fixed Distance Band", 
                        "EUCLIDEAN_DISTANCE", "None", maxdist)