## Name: SpaceTimeKernelDensity_Ex_standalone.py  
## Description: Calculate spatial temporal salinity concentration using a multidimensional dataset 
## Requirements: Spatial Analyst Extension 
 
## Import system modules 
import arcpy  
from arcpy import env   
from arcpy.sa import *

## Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")
 
## Set environment settings 
env.workspace = r" C:\STKD_Test"
# To allow overwriting outputs change overwriteOutput option to True. 
env.overwriteOutput = False 
  
## Set local variables 
in_features = "WOD_subset"  
Population_Field = "Salinity"  
Elevation_Field = "Z"  
Elevation_Field_Unit = "Meter"  
Time_Field = "Time"  
Cell_Size = "30"  
Resultant_values = "Densities"  
Method = "Planar" 
Elevation_Unit = "Meter"  
  
## Execute: Space Time Kernel Density  
STKD_out_raster = SpaceTimeKernelDensity(in_features, Population_Field,   
                                Elevation_Field, Elevation_Field_Unit,   
                                Time_Field, Cell_Size,   
                                resultant_values=Resultant_values,   
                                method=Method, 
                                elevation_unit=Elevation_Unit) 
  
## Save the output 
STKD_out_raster.save("STKD_test.crf")