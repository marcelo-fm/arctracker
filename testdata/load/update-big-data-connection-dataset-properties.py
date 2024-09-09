# Name: UpdateBDCDatasetProperties.py
# Description: Add a filter and modify the schema, time, and geometry for a MFC dataset
# Requirements: ArcGIS Pro Advanced License

# Import system modules
import arcpy

# Set local variables
dataset = r"c:\Projects\MyProjectFolder\my_BigDataConnection.mfc\myBigDataset"
filter = "COUNT > 500"
field_properties = "Field1 FLOAT true;Field2 STRING true;Field3 DOUBLE true"
geometry_type = "POINT"
sref = "4326"
geometry_format = "XYZ"
x_field = "Long"
y_field = "Lat"
z_field = ""
time_type = "INSTANT"
time_zone = "UTC"
time_formats = "Year yyyy"
file_extension = "csv"
file_delimiter = ","
file_terminator = r"\n"
file_quotechar = '"'
has_header_row = True
file_encoding = "UTF-8"


# Run Update MFC Dataset Properties
arcpy.gapro.UpdateBDCDatasetProperties(dataset, filter, field_properties, geometry_type, sref, geometry_format, "",
x_field, y_field, z_field, time_type, time_zone, time_formats, None, file_extension, file_delimiter, file_terminator, 
file_quotechar, has_header_row, file_encoding)