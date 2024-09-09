import arcpy

arcpy.management.MakeFeatureLayer(r"C:\Data\Canada\CanadaElecDist.shp", 
                                  "Canada_ElectoralDist")

arcpy.management.SelectLayerByAttribute("Canada_ElectoralDist", "NEW_SELECTION", 
                                        "\"PROVCODE\" = 'NS'")
count = arcpy.management.GetCount("Canada_ElectoralDist")[0]
print("Selected feature count: {}".format(count))

arcpy.analysis.PolygonNeighbors("Canada_ElectoralDist", 
                                r"C:\Data\Output\NS_elec_neigh.dbf", "ENNAME")
print(arcpy.GetMessages())