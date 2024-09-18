import arcpy
arcpy.management.MatchLayerSymbologyToAStyle("Streets", "$feature.RoadClass", 
                                             r"C:\RoadClasses.stylx")