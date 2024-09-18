# Name: TopoToRaster_Ex_02.py
# Description: Interpolates a hydrologically correct surface 
#    from point, line, and polygon data.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointElevations = TopoPointElevation([['spots.shp', 'spot_meter'], 
                                        ['spots2.shp', 'elev']])
inBoundary = TopoBoundary(['boundary.shp'])
inContours = TopoContour([['contours.shp', 'spot_meter']])
inLake = TopoLake(['lakes.shp'])
inSinks = TopoSink([['sink1.shp', 'elevation'], ['sink2.shp', 'none']])
inStream = TopoStream(['streams.shp'])

inFeatures = ([inPointElevations, inContours, inLake, inBoundary, inSinks])

# Execute TopoToRaster
outTTR = TopoToRaster(inFeatures)

# Save the output 
outTTR.save("C:/sapyexamples/output/ttrout03")