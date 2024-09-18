# Name: Extract_KML_popup_table.py
# Description: Convert a .kmz file and transfer a 2-column table from the pop-up 
#              to the field attributes.

# Import system modules
import arcpy
import os

# Set local variables and location for the consolidated file geodatabase
out_location = "C:/WorkingData/fGDBs"
gdb = 'SCP BoardDistricts.gdb'
gdb_location = os.path.join(out_location, gdb)

# Set kmz path
kmz = os.path.join(out_location, "SCP BoardDistricts.kmz")

# Convert all KMZ files to feature in the current workspace
arcpy.conversion.KMLToLayer(kmz, out_location)
    
# Change the workspace to fGDB location
arcpy.env.workspace = gdb_location

# Loop through all the file geodatabases in the workspace
feature_classes = arcpy.ListFeatureClasses('*', '', 'Placemarks')
for fc in feature_classes:
    popup_info_field_name = 'PopupInfo'
    field_names = [['gs_guid', 'TEXT', '#', 255, None, ''], 
                   ['gs_vc_revision', 'TEXT', '#', 255, None, ''], 
                   ['gs_vc_modified_sw', 'TEXT', '#', 255, None, ''], 
                   ['gs_old_objectid', 'TEXT', '#', 255, None, ''], 
                   ['gs_date_created', 'TEXT', '#', 255, None, ''], 
                   ['gs_date_modified', 'TEXT', '#', 255, None, ''], 
                   ['gs_code', 'TEXT', '#', 255, None, ''], 
                   ['gs_reference_scale', 'TEXT', '#', 255, None, ''], 
                   ['gs_description', 'TEXT', '#', 255, None, ''], 
                   ['gs_plot_scale', 'TEXT', '#', 255, None, ''], 
                   ['gs_nisc_guid', 'TEXT', '#', 255, None, ''], 
                   ['gs_mapped_by', 'TEXT', '#', 255, None, ''], 
                   ['gs_district', 'TEXT', 'Name', 255, None, ''], 
                   ['gs_boardmember', 'TEXT', '#', 255, None, ''], 
                   ['gs_servicetype', 'TEXT', 'Name', 255, None, ''], 
                   ['gs_legacy_futuraguid', 'TEXT', '#', 255, None, ''], 
                   ['gs_last_modified_by', 'TEXT', '#', 255, None, ''], 
                   ['gs_shape_from_gps_sw', 'TEXT', '#', 255, None, ''], 
                   ['gs_district_code', 'TEXT', '#', 255, None, ''], 
                   ['gs_district_name', 'TEXT', '#', 255, None, '']]
    arcpy.management.AddFields(fc, field_names, None)
    field_calculation = [[calc[0], f"extract_field(!{popup_info_field_name}!, '{calc[0]}')"] for calc in field_names]
    arcpy.management.CalculateFields(
        fc, "PYTHON3", field_calculation, 
"""from lxml import etree as _etree
def extract_field(s, field):
    ''' Extract fields from pop-up from each record in the calculate fields tool '''
    html = _etree.HTML(s)

    # Get all 'td'
    rows = html.xpath('//table/tr/td')
    next_value = False
    for row in rows:
        c = row.text
        if next_value:
            return c
        if c == field:
            next_value = True
    return None""", 
        "NO_ENFORCE_DOMAINS")