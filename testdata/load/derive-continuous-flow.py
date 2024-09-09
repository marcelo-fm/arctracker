# Name: DeriveContinuousFlow_standalone.py
# Description: Generates a flow accumulation raster considering real depressions
#              specified through a raster dataset.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_surface_raster = "surface.tif"
in_depressions_data = "depressions.tif"

# Execute DeriveContinuousFlow
out_derivecontinuousflow_raster = DeriveContinuousFlow(in_surface_raster, in_depressions_data,
                                 "", "", "", "")

# Save the output
out_derivecontinuousflow_raster.save("C:/arcpyExamples/outputs/out_facc.tif")