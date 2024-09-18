import arcpy
CV = [["FieldName1", "CODED_VALUE", "DomainValue1"], 
      ["FieldName2", "CODED_VALUE", "DomainValue2"]]
arcpy.management.AddContingentValue("C:\\MyProject\\myConn.sde\\mygdb.USER1.myFC", 
                                    "MyFieldGroup", CV, "My Subtype", 
                                    "DO_NOT_RETIRE")