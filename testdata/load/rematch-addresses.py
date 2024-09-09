# Rematch unmatched addresses in a geocoded feature class.
# Import system modules
import arcpy
arcpy.env.workspace = "C:/ArcTutor/Geocoding/atlanta.gdb" 

# Set local variables:
where_clause = "Status = 'U' "
geocoded_feature_class = "geocode_result"

arcpy.geocoding.RematchAddresses(geocoded_feature_class, where_clause)