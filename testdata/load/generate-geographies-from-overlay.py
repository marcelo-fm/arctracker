import arcpy
arcpy.ba.GenerateGeographiesFromOverlay("US.ZIP5", "TradeArea", "ID",
                                        r"C:\Temp\Output.gdb\OverlayTradeAreas")