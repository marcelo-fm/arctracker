import arcpy

target_catalog_dataset = r"C:/Dataspace/studyarea.gdb/SampleCatalog"
input_portal_itemtypes = ["SCENE_SERVICE", "WFS"]
content = "MY_GROUPS"
portal_groups = "SampleGroup" 
portal_folders = None
access_level = "ORG"
arcpy.management.AddPortalItemsToCatalogDataset(target_catalog_dataset,
                                        input_portal_itemtypes, content,
                                        portal_folders, portal_groups,
                                        access_level)