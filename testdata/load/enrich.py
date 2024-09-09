import arcpy
arcpy.analysis.Enrich("City", r"C:\temp\Data.gdb\City_Enrich", 
                      "populationtotals.totpop_cy")