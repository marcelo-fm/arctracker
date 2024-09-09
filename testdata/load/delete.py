import arcpy
arcpy.env.workspace = r"C:\dataToDelete"
arcpy.management.Delete(['NIRrG_ps8.afr', 'redlands.tpkx', 'colormap.img'])