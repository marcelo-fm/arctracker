import arcpy
arcpy.AddTerminalConfiguration_un('Electric Utility Network', 'config3', 
                                  'DIRECTIONAL', 'A true;B false;C false', None, 
                                  "AB A-B;ABAC 'A-B;A-C'", 'AB')