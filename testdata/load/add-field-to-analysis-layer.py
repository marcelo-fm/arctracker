# Name: AddFieldToAnalysisLayer_Workflow.py
# Description: Transfers the Address field from the input fire station
#              features to the 2-,3-, and 5-minute service area polygon features
#              calculated from a service area analysis. The Address field can
#              be used to join other attributes from the fire station features
#              to the service area polygon features.
# Requirements: Network Analyst Extension

#Import system modules
import arcpy
from arcpy import env
import os

try:
    #Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")
    
    #Set environment settings
    output_dir = "C:/Data"
    #The NA layer's data will be saved to the workspace specified here
    env.workspace = os.path.join(output_dir, "Output.gdb")
    env.overwriteOutput = True

    #Set local variables
    input_gdb = "C:/Data/SanFrancisco.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    layer_name = "FireStationsCoverage"
    travel_mode = "Driving Time"
    cutoffs = [2, 3, 5] #minutes
    field_to_add = "Address"
    field_type = "TEXT"
    facilities = os.path.join(input_gdb, "Analysis", "FireStations")
    search_tolerance = "2 Miles"
    out_featureclass = os.path.join(output_dir, "Output.gdb",
                                                    "FireStationsCoverageArea")

    #Create a new service area analysis layer. For this scenario, the default
    #value for all the remaining parameters statisfies the analysis requirements
    result_object = arcpy.na.MakeServiceAreaAnalysisLayer(network, layer_name,
                                                travel_mode, cutoffs=cutoffs)

    #Get the layer object from the result object. The service area layer can now
    #be referenced using the layer object.
    layer_object = result_object.getOutput(0)

    #Get the names of all the sublayers within the service area layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    #Stores the layer names that we will use later
    facilities_layer_name = sublayer_names["Facilities"]
    polygons_layer_name = sublayer_names["SAPolygons"]

    #Add the Address field to the Facilities sublayer of the service area layer.
    #This is done before loading the fire stations as facilities so that the
    #Address values can be transferred from the input features to the
    #Facilities sublayer.
    arcpy.na.AddFieldToAnalysisLayer(layer_object, facilities_layer_name,
                                        field_to_add, field_type)

    #Add the fire station features as Facilities and map the Name and the
    #Address fields from the fire station features to the Name and Address
    #properties on the Facilities sublayer
    field_mappings = arcpy.na.NAClassFieldMappings(layer_object,
                                                    facilities_layer_name)
    field_mappings['Name'].mappedFieldName = "Name"
    field_mappings['Address'].mappedFieldName = "Address"
    arcpy.na.AddLocations(layer_object, facilities_layer_name, facilities,
                          field_mappings, search_tolerance)

    #Solve the service area layer
    arcpy.na.Solve(layer_object)

    #Get the layer objects for all the sublayers within the service area layer
    facilities_sublayer = layer_object.listLayers(facilities_layer_name)[0]
    polygons_sublayer = layer_object.listLayers(polygons_layer_name)[0]

    #Transfer the Address field from the Facilities sublayer to the Polygons
    #sublayer of the service area layer since we wish to export the polygons.
    #The FacilityID field in the Polygons sublayer is related to the ObjectID
    #field in the Facilities sublayer.
    arcpy.management.JoinField(polygons_sublayer, "FacilityID",
                                facilities_sublayer, "ObjectID", field_to_add)

    #Export the Polygons sublayer to a feature class on disk.
    arcpy.management.CopyFeatures(polygons_sublayer, out_featureclass)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))