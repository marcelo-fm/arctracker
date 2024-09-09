import arcpy

# Point Address Data from Tutorial Data
in_point_features = r"C:\Data\SanMarcos.gdb\Address_Points"
point_field_mapping = "STREET_FULL_NAME ADDRESS"

# Street Address Data from Tutorial Data
in_street_features = r"C:\Data\SanMarcos.gdb\Address_Lines"
street_field_mapping = "HOUSE_NUMBER_FROM_LEFT L_ADDNUM_FROM;HOUSE_NUMBER_TO_LEFT L_ADDNUM_TO;HOUSE_NUMBER_FROM_RIGHT R_ADDNUM_FROM;HOUSE_NUMBER_TO_RIGHT R_ADDNUM_TO;STREET_PREFIX_DIR STPREDIR;STREET_NAME STNAME;STREET_SUFFIX_TYPE STSUFFIX;STREET_SUFFIX_DIR STPOSTDIR"

output_data_path = r"C:\Data\SanMarcos.gdb\Street_Points"

arcpy.geocoding.AssignStreetsToPoints(
    in_point_features,
    point_field_mapping,
    in_street_features,
    street_field_mapping,
    output_data_path,
    street_fields=None,
    distance=70,
    output_geometry="STREET_POINT_GEOMETRY"
)