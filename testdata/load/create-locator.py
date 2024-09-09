# Description: Create a multirole locator (PointAddress & StreetAddress) using a hosted
# feature service from ArcGIS Online as reference data.
# country_code and language_code
# are specified and will be applied to the entire reference dataset.
# The new locator will be created in a file folder.

# Import system modules
import arcpy

# Sign in to ArcGIS Online to use feature services as input
arcpy.SignInToPortal("https://www.arcgis.com", "<username>", "<password>")

# Set local variables
country = "USA"
in_table = "https://services.arcgis.com/<layer_id>/arcgis/rest/services/<service_name>/FeatureServer/<layer_number> PointAddress;"\
           "https://services.arcgis.com/<layer_id>/arcgis/rest/services/<service_name>/FeatureServer/<layer_number> StreetAddress"
field_mapping = ["PointAddress.ADDRESS_JOIN_ID '0'.PT_ADDR_ID",\
                "PointAddress.HOUSE_NUMBER '0'.ADDRESS",\
                "PointAddress.STREET_NAME '0'.ST_NAME",\
                "PointAddress.SIDE '0'.SIDE",\
                "PointAddress.CITY '0'.CITY",\
                "PointAddress.REGION '0'.STATE",\
                "StreetAddress.HOUSE_NUMBER_FROM_LEFT '1'.L_F_ADD_INT",\
                "StreetAddress.HOUSE_NUMBER_TO_LEFT '1'.L_T_ADD_INT",\
                "StreetAddress.HOUSE_NUMBER_FROM_RIGHT '1'.R_F_ADD_INT",\
                "StreetAddress.HOUSE_NUMBER_TO_RIGHT '1'.R_T_ADD_INT",\
                "StreetAddress.STREET_PREFIX_DIR '1'.PREFIX",\
                "StreetAddress.STREET_PREFIX_TYPE '1'.PRETYPE",\
                "StreetAddress.STREET_NAME '1'.NAME",\
                "StreetAddress.STREET_SUFFIX_TYPE '1'.TYPE",\
                "StreetAddress.STREET_SUFFIX_DIR '1'.SUFFIX",\
                "StreetAddress.CITY_LEFT '1'.PLACENAME_L",\
                "StreetAddress.CITY_RIGHT '1'.PLACENAME_R",\
                "StreetAddress.REGION_LEFT '1'.STATE",\
                "StreetAddress.REGION_ABBR_LEFT '1'.STATE_L",\
                "StreetAddress.REGION_RIGHT '1'.STATE",\
                "StreetAddress.REGION_ABBR_RIGHT '1'.STATE_R"]
out_locator = r"C:\output\locators\MultiroleFeatureServiceBasedLocator"
language = "ENG"

# Run CreateLocator
arcpy.geocoding.CreateLocator(country, in_table, field_mapping, out_locator, language)