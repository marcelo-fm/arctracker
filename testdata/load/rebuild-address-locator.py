# Import system modules
import arcpy
arcpy.env.workspace = "C:/ArcTutor/Geocoding/atlanta" 

# Set local variables:
address_locator = "Atlanta_AddressLocator"

arcpy.geocoding.RebuildAddressLocator(address_locator)