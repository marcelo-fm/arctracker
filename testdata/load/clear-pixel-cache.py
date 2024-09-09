#===========================
#Clear Pixel Cache
'''Usage: ClearPixelCache_management(in_mosaic_dataset, {generated_before})'''

import arcpy

#Clear Pixel Cache
mdname = r"c:\test\Clearpixelcahce.gdb\mosaicdataset"
date = "10/25/2018"


arcpy.management.ClearPixelCache(mdname, date)