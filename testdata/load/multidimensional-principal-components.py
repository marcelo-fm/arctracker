# Import system modules  

import arcpy  
from arcpy.ia import *   

# Check out the ArcGIS Image Analyst extension license  
arcpy.CheckOutExtension("ImageAnalyst")  

arcpy.env.workspace = r"c:\data"  
arcpy.ia.MultidimensionalPrincipalComponents('sstData.crf', 'SPATIAL_REDUCTION', "StdTime", "sstData_temporal_PC.csv", "sstData_loading_raster.crf", "sstData_eiganvalues.csv", None, 3)