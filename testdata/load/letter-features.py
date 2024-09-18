# Select buildings with a footprint over 5000 square feet and assign a letter

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"

# Project data
out_coordinate_system = arcpy.SpatialReference(3395)
proj_bldg = "bldg_footprint_proj"
arcpy.management.Project("Buildings",
                         proj_bldg,
                         out_coordinate_system)

# Calculate area
arcpy.management.CalculateGeometryAttributes(proj_bldg,
                                             "area AREA",
                                             '',
                                             "SQUARE_FEET_US")

# Export to a new feature class
expression = "area >= 5000"
arcpy.conversion.FeatureClassToFeatureClass(proj_bldg,
                                            arcpy.env.workspace,
                                            "bldg_over_5000",
                                            expression)

# Letter the buildings
arcpy.defense.LetterFeatures("bldg_over_5000",
                             "bldg_letter",
                              None,
                              "CENTER",
                              "A_B_C",
                              "A",
                              "D",
                              "neighborhood_center",
                              "ADD_DISTANCE")