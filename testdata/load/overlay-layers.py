#-------------------------------------------------------------------------------
# Name: OverlayLayers.py
# Description: Remove areas that are already developed from proposed development sites

# Import system modules
import arcpy

arcpy.env.workspace = "c:/data/data.gdb"  
# Set local variables
inFeatures = "areasOfInterest"
overlayFeatures = "commercial"
out = "DevelopmentSites"
overlayType = "ERASE"

# Run Overlay Layers
arcpy.gapro.OverlayLayers(inFeatures, overlayFeatures, out, 
                          overlayType)