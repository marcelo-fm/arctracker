import arcpy

arcpy.edit.UpdateCOGO('Lot_Lines', 'USE_MINIMUM_DIFFERENCE', '1 Feet', 
                      'USE_MINIMUM_DIFFERENCE', '20')