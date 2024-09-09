import arcpy
arcpy.management.CreateDatabaseView("C:\\mymgdbs\\facilities.geodatabase",
                                    "dog_parks",
                                    "select objectid, park_name, park_address, park_hours from parks where park_type = dog")