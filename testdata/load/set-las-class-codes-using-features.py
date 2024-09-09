'''**********************************************************************
Name: Assign Withheld Classification Flag to Outlier Points in LAS Files
Description: Uses Locate Outliers to identify points in LAS files that
             should be assigned the 'withheld' classification flag.
             Designed for use as a script tool.
**********************************************************************'''
# Import system modules
import arcpy

# Set Local Variables
lasD = arcpy.GetParameterAsText(0)
outliers = 'in_memory/outliers'

# Execute LocateOutliers
arcpy.ddd.LocateOutliers(lasD, outliers, 'APPLY_HARD_LIMIT', -10,
                         350, 'APPLY_COMPARISON_FILTER', 1.2, 120,
                         0.8, 8000)

# Execute SetLasClassCodeUsingFeatures
arcpy.ddd.SetLasClassCodesUsingFeatures(lasd, [["outliers.shp", 5,
                                                "NO_CHANGE", "NO_CHANGE",
                                                "NO_CHANGE", "SET"]])