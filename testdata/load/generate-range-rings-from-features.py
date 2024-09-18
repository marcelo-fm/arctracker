# Description: Select all points that have a minimum ring distance of at least 
#              6 then create rings and radials around those points.

# Import modules
import arcpy

# Set workspace
arcpy.env.workspace = r"C:/Data.gdb"

# Select points from the input
pointsToCreate = "all_points"
hasMinimumDist = "Min6"
whereClause = "min_range >= 6"
arcpy.Select_analysis(pointsToCreate, hasMinimumDist, whereClause)

# Generate rings and radials around selected points
outputRings = "Rings"
ringType = "MIN_MAX"
outputRadials = "Radials"
arcpy.GenerateRangeRingsFromFeatures_defense(hasMinimumDist,
                                             outputRings,
                                             ringType,
                                             outputRadials,
                                             "Radials",
                                             "min_range", "max_range")