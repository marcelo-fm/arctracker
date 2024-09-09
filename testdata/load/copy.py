# Name: Copy_Example3.py
# Description: Copy a feature dataset and specify associated_data

# Import system modules
import arcpy

# The input is a feature dataset containing 3 feature classes: lakes, cities, rivers
in_data =  "C:/data/proj.gdb/mexico" 
out_data = "C:/data/proj.sde/mexico"

associated_data = ";".join(["lakes FeatureClass mexico_lakes #",
                            "cities FeatureClass mexico_cities #",
                            "rivers FeatureClass mexico_rivers #"])

# Rename each feature class during the copy operation using the associated_data parameter
arcpy.management.Copy(in_data, out_data, associated_data=associated_data)