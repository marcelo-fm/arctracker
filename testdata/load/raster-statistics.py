import arcpy

# Statistics using a skip factor of 100 for x and y, and 
# ignore values of 0 and 255
arcpy.env.rasterStatistics = 'STATISTICS 100 100 (0 255)'