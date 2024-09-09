# Name: SmoothLine_Example2.py
# Description: Simplify and then Smooth coastlines

# Import system modules
import arcpy
import arcpy.cartography as CA

# Set environment settings
arcpy.env.workspace = "C:/data/Portland.gdb/Hydrography"

# Set local variables
inCoastlineFeatures = "coastlines"
barriers = "C:/data/Portland.gdb/Structures/buildings"
simplifiedFeatures = "C:/data/PortlandOutput.gdb/coastlines_simplified"
smoothedFeatures = "C:/data/PortlandOutput.gdb/coastlines_smoothed"

# Simplify coastlines.
CA.SimplifyLine(inCoastlineFeatures, simplifiedFeatures, "POINT_REMOVE", 50, 
                "RESOLVE_ERRORS", "KEEP_COLLAPSED_POINTS", "CHECK", barriers)

# Smooth coastlines.
CA.SmoothLine(simplifiedFeatures, smoothedFeatures, "PAEK", 100, "", 
              "FLAG_ERRORS", barriers)