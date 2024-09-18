# Import system modules
import arcpy

# Set the workspace
arcpy.env.workspace = "c:/data/mexico.gdb"

# Make a layer from the feature class
arcpy.management.MakeFeatureLayer("cities", "cities_lyr") 
 
# Select all cities that overlap the chihuahua polygon
arcpy.management.SelectLayerByLocation("cities_lyr", "intersect", "chihuahua", 
                                       0, "new_selection")

# Within selected features, further select only those cities that have a 
# population > 10,000   
arcpy.management.SelectLayerByAttribute("cities_lyr", "SUBSET_SELECTION", 
                                        '"population" > 10000')
 
# Convert the selected features to JSON
arcpy.conversion.FeaturesToJSON("cities_lyr", r"c:\data\myjsonfeatures.json")