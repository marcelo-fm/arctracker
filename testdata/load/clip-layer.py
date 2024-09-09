#-------------------------------------------------------------------------------
# Name: ClipLayer.py
# Description: Clip USA Rivers to the extent of state boundaries.

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/USA.gdb"

# Set local variables
clipFeatures = "USA_Rivers"
studyArea = "Nebraska_Boundary"
out = "NebraskaRivers"

# Run Clip Layer
arcpy.gapro.ClipLayer(clipFeatures, studyArea, out)