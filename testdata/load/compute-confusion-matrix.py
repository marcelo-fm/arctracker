import arcpy
from arcpy.sa import *

arcpy.gp.ComputeConfusionMatrix("aapnt2.shp", "confm.dbf")