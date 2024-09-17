# Assign buildings a number based on their sector and export the first building in sector 700

# Import modules
import arcpy

# Set workspace
arcpy.env.workspace = r"C:/Data.gdb"

# Number the buildings by sector
arcpy.NumberFeaturesBySector_defense("bldg_footprints",
                                     "sectors",
                                     "bldg_number",
                                     "LONG",
                                     "CENTER",
                                     100,
                                     "neighborhood_center",
                                     "DONT_ADD_DISTANCE")

# Select the first building in sector 700
select_from = "bldg_footprints"
expression = "bldg_number = 700"
arcpy.SelectLayerByAttribute_management(select_from,
                                        "NEW_SELECTION",
                                        expression)

# Export to new feature class
arcpy.FeatureClassToFeatureClass_conversion(select_from,
                                            arcpy.env.workspace,
                                            "bldg700")