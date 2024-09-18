import arcpy
arcpy.management.CreateFieldGroup("C:\\MyProject\\myConn.sde\\mygdb.USER1.myFC",
                                  "MyFieldGroup", 
                                  ["Field1", "Field2", "Field3"],
                                  "RESTRICT")