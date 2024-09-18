import arcpy
from arcpy.sa import *

arcpy.gp.UpdateAccuracyAssessmentPoints("aapnt1.shp", "grndtru.tif", "aapnt2.shp", "GROUND_TRUTH")