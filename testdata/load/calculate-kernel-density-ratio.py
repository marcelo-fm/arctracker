# Name: CalculateKernelDensityRatio_Ex_02.py 
# Description: Calculates the ozone concentration per population of each county out of 
#              Sierra Nevada Mountain in California 
#              based on the two point samples using a kernel function to 
#              fit a smoothly tapered surface of density ratio. 
# Requirements: Spatial Analyst Extension 

# Import system modules 
import arcpy 
from arcpy import env 
from arcpy.sa import * 

# Set environment settings 
env.workspace = r"C:/sapyexamples/data" 

# Set local variables 
inFeatures1 = "ozone_california.shp" 
inFeatures2 = "pop_california.shp" 
populationField1 = "OZONE" 
populationField2 = "POP" 
cellSize = 60 
searchRadius1 = 2500 
searchRadius2 = 500 
inBarriers1 = "SierraNevada.shp" 
inBarriers2 = "county.shp" 

# Execute CalculateKernelDensityRatio 
outKernelDensityRatio = CalculateKernelDensityRatio(inFeatures1, inFeatures2, populationField1, populationField2,
                                                    cellSize, searchRadius1, searchRadius2, "DENSITIES", "PLANAR",
                                                    inBarriers1, inBarriers2) 

# Save the output  
outKernelDensityRatio.save(r"C:/sapyexamples/output/KD_ozone_california.tif")