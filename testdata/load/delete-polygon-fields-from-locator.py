# Import system modules
import arcpy
arcpy.env.workspace = "C:/Data/USA"

# Set local variables
in_locator = "USA.loc"

arcpy.geocoding.DeletePolygonFieldsFromLocator(in_locator)