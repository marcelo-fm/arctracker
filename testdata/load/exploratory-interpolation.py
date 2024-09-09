# Interpolate points and a field using various interpolation methods
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
ingdb = directory + "data.gdb/"
outgdb = directory + "out.gdb/"
arcpy.env.workspace = directory
# Input points
inPoints = ingdb + "myPoints"
# Input field
inField = "myField"
# List of interpolation methods
interpMethods = ["SIMPLE_KRIGING", "UNIVERSAL_KRIGING", "EBK"]
# Exclude results with error reductions under 25%
exclCrit = [["MIN_PERC_ERROR", 25]]
# Output geostatistical layer with highest rank
outGALayer = "Result With Highest Rank"

### Set weighted average rank parameters
# Output table of ranks and cross validation results
outTable = directory + "outWeightedAverageTable"
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
arcpy.ga.ExploratoryInterpolation(inPoints, inField, outTable, outGALayer,
         interpMethods, compMethod, None, None, weightedCrit, exclCrit)



### Set hierarchical sorting parameters
# Output table of ranks and cross validation results
outTable = directory + "outHierSortTable"
# Use hierarchical sorting with tolerances
compMethod = "SORTING"
# Compare using highest prediction accuracy with a 10% tolerance
# Break ties by lowest bias
hierCrit = [
            ["ACCURACY", "PERCENT", 10],
            ["BIAS", "PERCENT", None]
           ]

# Compare using hierarchical sorting with tolerances
arcpy.ga.ExploratoryInterpolation(inPoints, inField, outTable, outGALayer,
         interpMethods, compMethod, None, hierCrit, None, exclCrit)