import arcpy
 
# Set the XY Domain to 
#   xmin of -180
#   ymin of -90
#   xmax of 180
#   ymax of 90
arcpy.env.XYDomain = "-180 -90 180 90"