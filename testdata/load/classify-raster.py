# Import system modules
import arcpy
from arcpy.sa import *


# Set local variables
insegras = "c:/classifydata/moncton_seg.tif"
indef_file = "c:/classifydata/moncton_sig.ecd"
in_additional_raster = "c:/classifydata/moncton.tif"


# Execute 
classifiedraster = ClassifyRaster(insegras, indef_file, in_additional_raster)

#save output
classifiedraster.save("c:/test/moncton_classified.tif")