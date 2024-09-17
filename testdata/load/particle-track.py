# Name: ParticleTrack_Ex_02.py
# Description: Calculates the path of a particle through a velocity field.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inDirectionRaster = "gwdir"
inMagnitudeRaster = "gwmag"
sourcePoint = arcpy.Point(-200, -200)
outTrackFile = "C:/sapyexamples/output/trackfile.txt"
stepLength = 10
trackingTime = 10000000
outTrackPolylineFeatures = "C:/sapyexamples/output/trackpolyline.shp"

# Execute ParticleTrack
ParticleTrack(inDirectionRaster, inMagnitudeRaster, sourcePoint, outTrackFile,
              stepLength, trackingTime, outTrackPolylineFeatures)