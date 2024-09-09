import arcpy
arcpy.management.UploadFileToPortal(r"C:\states.lyrx", "MyFile", "", 
                              "My Summary", "tag1, tag2", "EVERYONE", 
                              "MYGROUP")