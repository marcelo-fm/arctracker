# Measure the geographic distribution of auto thefts
 
# Import system modules
import arcpy
 
# Local variables...
workspace = "C:/data"
locations = "AutoTheft.shp"
links = "AutoTheft_links.shp"
standardDistance = "auto_theft_SD.shp"
stardardEllipse = "auto_theft_SE.shp"
linearDirectMean = "auto_theft_LDM.shp"

# Set the workspace (to avoid having to type in the full path to the data every 
# time)
arcpy.env.workspace = workspace
 
# Process: Standard Distance of auto theft locations...
arcpy.stats.StandardDistance(locations, standardDistance, "1_STANDARD_DEVIATION")
 
# Process: Directional Distribution (Standard Deviational Ellipse) of auto 
# theft locations...
arcpy.stats.DirectionalDistribution(locations, standardEllipse, 
                                    "1_STANDARD_DEVIATION")
 
# Process: Linear Directional Mean of auto thefts...
arcpy.stats.DirectionalMean(links, linearDirectMean, "DIRECTION")