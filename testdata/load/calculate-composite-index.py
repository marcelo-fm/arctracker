# Import system modules 
import arcpy 
import os 

try: 
    # Set the workspace and overwrite properties
    arcpy.env.workspace = r"C:\temp\temp.gdb" 
    arcpy.env.overwriteOutput = True 
    
    # Set the input point feature parameters
    input_features = os.path.join(arcpy.env.workspace, "CommunityCharacteristics")

    # Set a list of variables that will be combined into an index
    input_variables = ["ASTHMA_Prevalence_Percent", "Health_NoInsurance_Percent", 
                       "BelowPovertyLine_Percent"]

    # Set the output name that will contain the index values.
    output_features = os.path.join(arcpy.env.workspace, "CommunityCharacteristicsIndex")

    # Set the method to scale the input variables
    preprocessing_method = "PERCENTILE"

    # Set the method to combine the input variables
    combination_method = "MEAN"
    variable_weights = [["ASTHMA_Prevalence_Percent", 2],
                        ["Health_NoInsurance_Percent", 1],
                        ["BelowPovertyLine_Percent", 1]]

    # Set the output settings
    output_index_name = "Asthma_Needs_Index"
    output_index_range = "0 100"
    output_classification = "QUANTILE"
    output_classification_num_classes = 5

    # Call the tool using the parameters defined above.
    arcpy.stats.CalculateCompositeIndex(
        in_table=input_features,
        in_variables=input_variables, 
        out_table=output_features,
        index_preset="CUSTOM",
        preprocessing=preprocessing_method,
        index_method=combination_method,
        index_weights=variable_weights,
        out_index_name=output_index_name,
        post_min_max=output_index_range,
        post_reclass=output_classification,
        post_num_classes=output_classification_num_classes)

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())