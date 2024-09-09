import arcpy

usa_locator = r"C:\Data\USA.loc"
my_clipped_locator = r"C:\Data\SanDiego.loc"

# Define the extent using an arcpy Extent object
my_san_diego_extent = arcpy.Extent(
    -13115569.084655, 3826591.24577018, -12897364.810527, 3969918.09780486, 
    spatial_reference=arcpy.SpatialReference('WGS 1984 Web Mercator (auxiliary sphere)'))

# Run ClipLocator
arcpy.geocoding.ClipLocator(usa_locator, my_clipped_locator, None, my_san_diego_extent)