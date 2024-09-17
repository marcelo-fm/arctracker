#Merge items with items that are newer than year 1999

import arcpy
    
arcpy.MergeMosaicDatasetItems_management(
    "c:/data/merge_md_items.gdb/md", "Year>1999", "", "1000")