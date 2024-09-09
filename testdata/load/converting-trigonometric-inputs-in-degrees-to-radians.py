>>> import math
>>> deg2rad = math.pi / 180.0
>>> from arcpy.sa import *
>>> OutRas = Cos (InRas * deg2rad)