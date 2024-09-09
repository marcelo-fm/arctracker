# Name: MakeVRPAnalysisLayer_Ex3_Workflow.py
# Description: Find the best routes for a fleet of vehicles, which is operated
#              by a distribution company, to deliver goods from a main
#              distribution center to a set of grocery stores.
# Requirements: Network Analyst Extension

# Import system modules
import arcpy
import os

try:
    # Check out the Network Analyst license if available.
    # Fail if the Network Analyst
    # license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")

    # Set environment settings
    output_dir = r"C:\Data"
    # The NA layer's data will be saved to the workspace specified here
    arcpy.env.workspace = os.path.join(output_dir, "Output.gdb")
    arcpy.env.overwriteOutput = True

    # Set local variables
    input_gdb = "C:/Data/SanFrancisco.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    layer_name = "StoreDeliveryRoute"
    travel_mode = "Driving Time"
    time_units = "Minutes"
    distance_units = "Miles"
    in_orders = os.path.join(input_gdb, "Analysis", "Stores")
    in_depots = os.path.join(input_gdb, "Analysis", "DistributionCenter")
    in_routes = os.path.join(input_gdb, "Analysis", "Routes")
    output_layer_file = os.path.join(output_dir, layer_name + ".lyrx")

    # Create a new Vehicle Routing Problem (VRP) layer. Since the time-based
    # attributes such as ServiceTime on orders and CostPerUnitTime on routes is
    # recorded in minutes, we use minutes for time_units parameter. As we are
    # using cost per unit distance in routes, we have to specify a distance
    # attribute. The values for CosterPerUnitDistance are in miles, so we
    # specify miles for distance units parameter
    result_object = arcpy.na.MakeVehicleRoutingProblemAnalysisLayer(
        network, layer_name, travel_mode, time_units, distance_units,
        line_shape="STRAIGHT_LINES")

    # Get the layer object form the result object. The route layer can now be
    # referenced using the layer object.
    layer_object = result_object.getOutput(0)

    # Get the names of all the sublayers within the VRP layer.
    sub_layer_names = arcpy.na.GetNAClassNames(layer_object)
    # Store the layer names that we will use later
    orders_layer_name = sub_layer_names["Orders"]
    depots_layer_name = sub_layer_names["Depots"]
    routes_layer_name = sub_layer_names["Routes"]

    # Load the store locations as orders. Using field mappings we map the
    # TimeWindowStart1, TimeWindowEnd1, and DeliveryQuantities properties
    # for Orders from the fields of store features and assign a value of
    # 0 to MaxViolationTime1 property. The Name and ServiceTime properties
    # have the correct mapped field names when using the candidate fields
    # from store locations feature class.
    candidate_fields = arcpy.ListFields(in_orders)
    order_field_mappings = arcpy.na.NAClassFieldMappings(layer_object, orders_layer_name, False, candidate_fields)
    order_field_mappings["TimeWindowStart"].mappedFieldName = "TimeStart1"
    order_field_mappings["TimeWindowEnd"].mappedFieldName = "TimeEnd1"
    order_field_mappings["DeliveryQuantity_1"].mappedFieldName = "Demand"
    order_field_mappings["MaxViolationTime"].defaultValue = 0
    arcpy.na.AddLocations(layer_object, orders_layer_name, in_orders, order_field_mappings, "")

    # Load the depots from the distribution center features. Using field mappings
    # we map the Name properties for Depots from the fields of distribution
    # center features and assign a value of 8 AM for TimeWindowStart1 and a
    # value of 5 PM for TimeWindowEnd1 properties
    depot_field_mappings = arcpy.na.NAClassFieldMappings(layer_object, depots_layer_name)
    depot_field_mappings["Name"].mappedFieldName = "Name"
    depot_field_mappings["TimeWindowStart"].defaultValue = "8 AM"
    depot_field_mappings["TimeWindowEnd"].defaultValue = "5 PM"
    arcpy.na.AddLocations(layer_object, depots_layer_name, in_depots, depot_field_mappings, "")

    # Load the routes from a table containing information about routes. In this
    # case, since the fields on the routes table and property names for Routes
    # are the same, we will just use the default field mappings
    routes_field_mappings = arcpy.na.NAClassFieldMappings(layer_object, routes_layer_name)
    routes_field_mappings["Name"].mappedFieldName = "Name"
    routes_field_mappings["StartDepotName"].mappedFieldName = "StartDepotName"
    routes_field_mappings["EndDepotName"].mappedFieldName = "EndDepotName"
    routes_field_mappings["StartDepotServiceTime"].mappedFieldName = "StartDepotServiceTime"
    routes_field_mappings["Capacity_1"].mappedFieldName = "Capacities"
    routes_field_mappings["CostPerUnitTime"].mappedFieldName = "CostPerUnitTime"
    routes_field_mappings["CostPerUnitDistance"].mappedFieldName = "CostPerUnitDistance"
    routes_field_mappings["MaxOrderCount"].mappedFieldName = "MaxOrderCount"
    routes_field_mappings["MaxTotalTime"].mappedFieldName = "MaxTotalTime"
    routes_field_mappings["MaxTotalTravelTime"].mappedFieldName = "MaxTotalTravelTime"
    routes_field_mappings["MaxTotalDistance"].mappedFieldName = "MaxTotalDistance"
    arcpy.na.AddLocations(layer_object, routes_layer_name, in_routes, routes_field_mappings, "")

    # Solve the VRP layer
    arcpy.na.Solve(layer_object)

    # Save the solved VRP layer as a layer file on disk with relative paths
    arcpy.management.SaveToLayerFile(layer_object, output_layer_file, "RELATIVE")

    print("Script Completed Successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback
    import sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))