# Purpose: Calculate the number of features in a feature class

# Import system modules
import arcpy
 
lyrfile = r"C:\data\streets.lyr"
result = arcpy.management.GetCount(lyrfile)

# Print the number of features using the Result object
print('{} has {} records'.format(lyrfile, result[0]))