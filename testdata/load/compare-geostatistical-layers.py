# Compare various interpolation results
# Rank results by highest weighted average rank
# Rank same results by hierarchical sorting

# Import system modules
import arcpy

# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Allow overwriting output
arcpy.env.overwriteOutput = True

### Set shared parameters
# Set input and output locations
directory = "C:/data/"
outgdb = directory + "out.gdb/"
arcpy.env.workspace = directory
# Three interpolation results to compare
myGALayers = ["EBK", "Universal Kriging", "Kernel Interpolation"]
# Exclude results with error reductions under 25%
exclCrit = [["MIN_PERC_ERROR", 25]]
# Output geostatistical layer with highest rank
outGALayer = "Result With Highest Rank"

### Set weighted average rank parameters
# Output table of ranks and cross validation results
outTable = outgdb + "outWeightedAverageTable"
# Use weighted average rank
compMethod = "AVERAGE_RANK"
# Use all criteria with highest weight to prediction accuracy
weightedCrit = [
            ["ACCURACY", 3],
            ["BIAS", 1],
            ["WORST_CASE", 1],
            ["STANDARD_ERROR", 1],
            ["PRECISION", 1]
               ]

# Compare using weighted average rank
arcpy.ga.CompareGeostatisticalLayers(myGALayers, outTable, outGALayer,
         compMethod, None, None, weightedCrit, exclCrit)



### Set hierarchical sorting parameters
# Output table of ranks and cross validation results
outTable = outgdb + "outHierSortTable"
# Use hierarchical sorting with tolerances
compMethod = "SORTING"
# Compare using highest prediction accuracy with a 10% tolerance
# Break ties by lowest bias
hierCrit = [
            ["ACCURACY", "PERCENT", 10],
            ["BIAS", "PERCENT", None]
           ]

# Compare using hierarchical sorting with tolerances
arcpy.ga.CompareGeostatisticalLayers(myGALayers, outTable, outGALayer,
         compMethod, None, hierCrit, None, exclCrit)