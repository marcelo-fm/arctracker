'''****************************************************************************
Name: Classify Noise Points
Description: Updates classification of version 1.0 LAS files to conform to
             the standardized class codes introduced in the 1.1 specifications.
             The code is designed for use as a script tool.
****************************************************************************'''
# Import system modules
import arcpy
import exceptions, sys, traceback

# Set Local Variables
inLas = arcpy.GetParameterAsText(0)
recursion = arcpy.GetParameterAsText(1)
lasd = arcpy.GetParameterAsText(2)
reclassList = arcpy.GetParameterAsText(3) #List of values '<oldCode> <newCode>'
calcStats = arcpy.GetParameter(4)

try:
    # Execute CreateLasDataset
    arcpy.management.CreateLasDataset(inLas, lasd, folder_recursion=recursion)
    # Execute Locate Outliers
    outlier_pts = 'in_memory/outliers'
    arcpy.ddd.LocateOutliers(lasd, out_feature_class=outlier_pts, 
                            apply_hard_limit='Apply_Hard_Limit', 
                            absolute_z_min=-15, absolute_z_max=680, 
                            apply_comparison_filter='Apply_Comparison_Filter',
                            z_tolerance=0, slope_tolerance=150, 
                            exceed_tolerance_ratio=0.5, outlier_cap=3000)
    # Execute ChangeLasClassCodes
    arcpy.ddd.LocateLasPointsByProximity(lasd, in_features=outlier_pts, 
                                         search_radius='0.5 Centimeters', 
                                         class_code=18)
    # Report messages
    arcpy.GetMessages(0)

except arcpy.ExecuteError:
    print(arcpy.GetMessages())