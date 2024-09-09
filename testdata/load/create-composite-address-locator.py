# Create a composite address locator using the StreetMap US Streets and Tutorial Atlanta locators.

# Import system modules
import arcpy 

arcpy.env.workspace = "C:/ArcTutor/Geocoding/atlanta/"

# Set local variables:
US_Streets_locator = "C:/dm_stmap_dvd/streetmap_na/data/Street_Addresses_US"
Atlanta_locator = Atlanta
Atlanta_Composite = US_Atlanta_Composite

# Field mapping
address_field_map = "Address 'Street or Intersection' true true false 100 Text 0 0 ,First,#,Atlanta_locator,Address,0,0,US_Streets_locator,Street;"
city_field_map = "City 'City or Placename' true true false 40 Text 0 0 ,First,#,Atlanta_locator,City,0,0,US_Streets_locator,City;"
state_field_map = "State 'State' true true false 20 Text 0 0 ,First,#,Atlanta_locator,State,0,0,US_Streets_locator,State;"
zip_field_map = "Zip 'Zipcode' true true false 10 Text 0 0 ,First,#,Atlanta_locator,Zip,0,0,US_Streets_locator,ZIP"

composite_locator_field_map = address_field_map + city_field_map + state_field_map + zip_field_map

arcpy.geocoding.CreateCompositeAddressLocator("Atlanta_locator Atlanta;US_Streets_locator US_Streets", composite_loactor_field_map,"Atlanta '\"City\" = 'Atlanta'';US_Streets #",Atlanta_Composite)