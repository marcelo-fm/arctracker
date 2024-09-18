import arcpy
arcpy.AlterFieldGroup_management("C:\\MyProject\\myConn.sde\\mygdb.USER1.myFC",
                                 "MyFieldGroup", "MyNewFieldGroupName",
                                 ["Field1", "Field3"],
                                 "DO_NOT_RESTRICT")