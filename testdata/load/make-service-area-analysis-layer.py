# Name: MakeServiceAreaAnalysisLayer_Workflow2.py
# Description: Generate 3-minute service areas around fire stations at several
#               times of day to compare coverage differences due to varying
#               traffic conditions. Save the results to a feature class on disk.
# Requirements: Network Analyst Extension

# Import system modules
import arcpy
from arcpy import env
import os, datetime

try:
    # Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")
    
    # Set environment settings
    output_dir = "C:/Data"
    # The NA layer's data will be saved to the workspace specified here
    env.workspace = os.path.join(output_dir, "Output.gdb")
    env.overwriteOutput = True

    # Set local variables
    input_gdb = "C:/Data/SanFrancisco.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    layer_name = "FireStationCoverage"
    out_featureclass = os.path.join(output_dir, "Output.gdb",
                                                        "FireStationCoverage")
    travel_mode = "Driving Time"
    facilities = os.path.join(input_gdb, "Analysis", "FireStations")
    times_of_day = [datetime.datetime(2014, 9, 25, 7, 0, 0),
                    datetime.datetime(2014, 9, 25, 12, 30, 0),
                    datetime.datetime(2014, 9, 25, 17, 30, 0),
                    datetime.datetime(2014, 9, 25, 21, 0, 0)]

    # Create a new service area layer.
    result_object = arcpy.na.MakeServiceAreaAnalysisLayer(network, layer_name,
                                                travel_mode, "FROM_FACILITIES",
                                                [3], polygon_detail="HIGH",
                                                geometry_at_overlaps="OVERLAP")

    # Get the layer object from the result object. The service area layer can
    # now be referenced using the layer object.
    layer_object = result_object.getOutput(0)

    # Get the names of all the sublayers within the service area layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    # Stores the layer names that we will use later
    facilities_layer_name = sublayer_names["Facilities"]
    polygons_layer_name = sublayer_names["SAPolygons"]

    # The input data has a field for FireStationID that we want to transfer to
    # our analysis layer. Add the field, and then use field mapping to transfer
    # the values.
    arcpy.na.AddFieldToAnalysisLayer(layer_object, facilities_layer_name,
                                                    "FireStationID", "TEXT")
    field_mappings = arcpy.na.NAClassFieldMappings(layer_object,
                                                    facilities_layer_name)
    field_mappings["FireStationID"].mappedFieldName = "FireStationID"

    # Load the fire stations as facilities.
    arcpy.na.AddLocations(layer_object, facilities_layer_name, facilities,
                            field_mappings, "")

    # Add fields to the output Polygons sublayer for later use.
    arcpy.na.AddFieldToAnalysisLayer(layer_object, polygons_layer_name,
                                        "FireStationID", "TEXT")
    arcpy.na.AddFieldToAnalysisLayer(layer_object, polygons_layer_name,
                                        "TimeOfDay", "TEXT")

    # Get sublayers to work with later
    facilities_sublayer = arcpy.na.GetNASublayer(layer_object, "Facilities")
    polygons_sublayer = arcpy.na.GetNASublayer(layer_object, "SAPolygons")

    # Get the Service Area Layer's solver properties. This can be used to
    # set individual properties later without re-creating the layer.
    solver_properties = arcpy.na.GetSolverProperties(layer_object)

    # Solve the Service Area for each time of day in the time list
    for t in times_of_day:

        print("Calculating service area for time of day: ", t)

        # Use the solver properties to set the time of day for the solve
        solver_properties.timeOfDay = t

        # Solve the service area layer
        arcpy.na.Solve(layer_object)

        # Transfer the FireStationID field from the input Facilities to the
        # output Polygons
        arcpy.management.AddJoin(polygons_sublayer, "FacilityID",
                                        facilities_sublayer, "ObjectID")
        # The joined fields are qualified by the feature class name of the joined
        # table, so determine the feature class names
        field_qualifier_pol = os.path.basename(polygons_sublayer.dataSource)
        target_field_name = "%s.FireStationID" % field_qualifier_pol
        field_qualifier_fac = os.path.basename(facilities_sublayer.dataSource)
        expression = "!%s.FireStationID!" % field_qualifier_fac
        arcpy.management.CalculateField(polygons_sublayer, target_field_name,
                                        expression, "PYTHON")
        arcpy.management.RemoveJoin(polygons_sublayer)

        # Populate the TimeOfDay field in the output feature class
        expression = '"' + str(t) + '"'
        arcpy.management.CalculateField(polygons_sublayer, "TimeOfDay",
                                            expression, "PYTHON")

        # Append the polygons to the output feature class. If this was the first
        # solve, create the feature class.
        if not arcpy.Exists(out_featureclass):
            arcpy.management.CopyFeatures(polygons_sublayer, out_featureclass)
        else:
            arcpy.management.Append(polygons_sublayer, out_featureclass)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))