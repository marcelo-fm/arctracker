"""Precalculate network locations with the Calculate Locations
geoprocessing tool, then run a Service Area workflow using
the arcpy.nax solver object. Map the precalculated network
locations using fieldMappings and load.
"""
import arcpy

arcpy.CheckOutExtension("network")

network = "C:/Data/Paris.gdb/Transportation/ParisMultimodal_ND"
input_facilities = "C:/Data/Paris.gdb/Analysis/Stores"
travel_mode = "Driving Time"

# Make a network dataset layer
nd_layer = arcpy.nax.MakeNetworkDatasetLayer(network).getOutput(0)

# Run Calculate Locations to calculate the network locations of
# the points in the input feature class. Use the same network,
# travel mode, and locate settings that will be used in the
# network analysis.
# Set a search_tolerance of 500 meters.
# Use search_criteria to locate only on streets and metro entrances.
# Use search_query to prevent locating on highways (FUNC_CLASS 1)
arcpy.nax.CalculateLocations(
    input_facilities,
    nd_layer,
    search_tolerance="500 Meters",
    search_criteria=[
        ["Streets", "SHAPE"],
        ["Metro_Lines", "NONE"],
        ["Transfer_Stations", "NONE"],
        ["Transfer_Street_Station", "NONE"],
        ["Metro_Entrances", "SHAPE"],
        ["Metro_Stations", "NONE"],
        ["ParisMultimodal_ND_Junctions", "NONE"]
    ],
    search_query=[["Streets", "FUNC_CLASS <> '1'"]],
    travel_mode=travel_mode
)

# Initialize the Service Area solver object
service_area = arcpy.nax.ServiceArea(nd_layer)

# Set the analysis properties. Use the same travel mode and
# locate settings that were used when precalculating the
# network locations
service_area.travelMode = travel_mode
service_area.searchTolerance = 500
service_area.searchToleranceUnits = arcpy.nax.DistanceUnits.Meters
service_area.searchSources = [
    ["Streets", "FUNC_CLASS <> '1'"],
    ["Metro_Entrances", "SHAPE"]
]
service_area.defaultImpedanceCutoffs = [5, 10]

# Construct a field mapping object with network location fields
field_mappings = service_area.fieldMappings(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    use_location_fields=True
)

# Load the input data using the field mappings
# Location fields are included automatically because
# of the field mappings.
service_area.load(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    input_facilities,
    field_mappings
)

# Solve the analysis
result = service_area.solve()
print(result.solveSucceeded)

# ...analysis of the results continues...