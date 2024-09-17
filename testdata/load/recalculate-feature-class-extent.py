import arcpy
feature_class = r"C:\Data\europe.gdb\norway_cities"
arcpy.management.RecalculateFeatureClassExtent(feature_class)