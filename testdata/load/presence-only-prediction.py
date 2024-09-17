# This example uses presence and background points and explanatory 
# variables from rasters, fields, and distance features to train a 
# model, using additional parameters to apply basis functions, use 
# spatial thinning, perform cross-validation, and receive diagnostic 
# training outputs. 

# Import system modules 
import arcpy 

try: 
    # Set the workspace and overwrite properties
    arcpy.env.workspace = r"C:\MyData.gdb" 
    arcpy.env.overwriteOutput = True 

    ### MODEL INPUTS ###
    
    # Set the input point feature parameters
    in_point_features = "presence_observations"
    contains_background = "PRESENCE_AND_BACKGROUND_POINTS
    presence_indicator_field = "Presence"
    
    # Set the explanatory Training variables
    explanatory_fields = [["Survey_Region", "true"], 
                          ["Temperature", "false"], 
                          ["Humidity", "false"]]
    explanatory_rasters = [["Elevation", "false"], 
                           ["Canopy", "false"], 
                           ["ClimacticWaterDeficit", "false"], 
                           ["LandCoverClassification", "true"], 
                           ["UpperSlope", "false"],
                           ["LowerSlope", "false"]]
    explanatory_dist_features = [["Streams", "false"], 
                                 ["Lakes", "false"], 
                                 ["Roads", "false"]]                           
    
    ### MODEL CONFIGURATION ###

    # Set basis functions
    basis_functions = "LINEAR;QUADRATIC;PRODUCT;HINGE"
    number_knots = 10

    # Set the study area
    study_area_type = "CONVEX_HULL"
    study_area_polygon = None

    # Set spatial thinning 
    spatial_thinning = "THINNING"
    min_nearest_neighbor_distance = "500 Meters"
    number_of_iterations = 10

    # Set the relative weight of presence to background and link function, using
    # background points as observed absence
    relative_weight = 1
    link_function = "LOGISTIC"

    # Set the presence probability cutoff
    cutoff = 0.3

    ### MODEL OUTPUTS AND VALIDATION ###

    # Set training outputs for model evaluation
    out_trained_features = "Out_Trained_Features"
    out_trained_raster = "Out_Trained_Raster"
    out_response_curve_table = "Out_Response_Curves"
    out_sensitivity_table = "Out_Sensitivity_Table"
    
    # Set cross-validation options
    resampling_scheme = "RANDOM"
    number_of_groups = 3

    # Call the tool using the parameters defined above.
    arcpy.stats.PresenceOnlyPrediction(
        input_point_features=in_point_features,
        contains_background=contains_background,
        explanatory_variables=explanatory_fields,
        explanatory_rasters=explanatory_rasters,
        distance_features=explanatory_dist_features,
        basis_expansion_functions=basis_functions,
        number_knots=number_knots,
        study_area_type=study_area_type,
        spatial_thinning=spatial_thinning,
        thinning_distance_band=min_nearest_neighbor_distance,
        number_of_iterations=number_of_iterations,
        relative_weight=relative_weight,
        link_function=link_function,
        presence_probability_cutoff=cutoff,
        output_trained_features=out_trained_features,
        output_trained_raster=out_trained_raster,
        output_response_curve_table=out_response_curve_table,
        output_sensitivity_table=out_sensitivity_table,
        resampling_scheme=resampling_scheme,
        number_of_groups=number_of_groups)