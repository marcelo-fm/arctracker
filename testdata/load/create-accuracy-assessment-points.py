import arcpy
from arcpy.sa import *

arcpy.gp.CreateAccuracyAssessmentPoints("cls.tif", "aapnt1.shp", "COMPUTED", "1500", "RANDOM")