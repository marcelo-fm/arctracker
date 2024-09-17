##===========================
##Generate Exclude Area
##Usage: GenerateExcludeArea_management in_raster out_raster 8_BIT | 11_BIT | 
##                                      12_BIT | 16_BIT COLOR_MASK | HISTOGRAM_PERCENTAGE
##                                      {max_red} {max_green} {max_blue} {max_white} 
##                                      {max_black} {max_magenta} {max_cyan}
##                                      {max_yellow} {percentage_low} {percentage_high}

import arcpy
arcpy.env.workspace = "c:/workspace"

# Generate exclude area dataset from raster dataset with Histogram
arcpy.GenerateExcludeArea_management("srcimage.tif", "exarea.tif", "8_BIT",
                                     "HISTOGRAM_PERCENTAGE", "", "", "", "",
                                     "", "", "", "", "10", "100")                                      

# Generate exclude area dataset from mosaic dataset with Color Mask
arcpy.GenerateExcludeArea_management("CC.gdb/srcmd", "exarea.tif", "8_BIT",
                                     "COLOR_MASK", "255", "200", "50", "255",
                                     "10", "210", "100", "255", "", "")