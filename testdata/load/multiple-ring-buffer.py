# Name: MultipleRingBuffer_Example2.py
# Description: Create multiple buffers for the input features
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/airport.gdb"
 
# Set local variables
inFeatures = "schools"
outFeatureClass = "c:/output/output.gdb/multibuffer1"
distances = [10, 20, 30]
bufferUnit = "meters"

# Execute MultipleRingBuffer
arcpy.analysis.MultipleRingBuffer(inFeatures, outFeatureClass, distances, 
                                  bufferUnit, "", "ALL")