import arcpy
arcpy.env.workspace = 'c:/data'
arcpy.ddd.GenerateClearanceSurface('VegManagement.gdb/PowerLines', '15 Meters', 
                                   '9 Meters', 'ClearanceZone.tif', 
                                   '50 Centimeters', 'MAXIMUM', 45, '5 Meters')