import arcpy
arcpy.CreateDiagramLayerDefinition_nd(input_Network, "MyTemplate1", 
                                      "HIDE", "HIDE", "SHOW", "SHOW", 
                                      overwrite_all_layers="MERGE")