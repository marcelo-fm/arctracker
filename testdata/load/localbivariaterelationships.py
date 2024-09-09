# Use the Local Bivariate Relationships tool to study the relationship between
# obesity and diabetes.

# Import system modules.
import arcpy
import os

# Set property to overwrite existing output by default.
arcpy.env.overwriteOutput = True

try:
    # Set the workspace and input features.
    arcpy.env.workspace = r"C:\\LBR\\MyData.gdb"
    inputFeatures = 'ObesityDiabetes'

    # Set the output workspace and output name.
    outws = 'C:\\LBR\\outputs.gdb'
    outputName = 'LBR_Results'

    # Set input features, dependent variable, and explanatory variable.
    depVar = 'DiabetesRate'
    explVar = 'ObesityRate'

    # Set number of neighbors and permutations.
    numNeighbors = 50
    numPerms = '999'

    # Choose to create pop-ups.
    popUps = 'CREATE_POPUP'

    # Choose confidence level and apply False Discovery Rate correction.
    confLevel = '95%'
    fdr = 'APPLY_FDR'

    # Set the scaling factor.
    scaleFactor = 0.5

    # Run Local Bivariate Relationships.
    arcpy.stats.LocalBivariateRelationships(inputFeatures, depVar, explVar, 
                                            os.path.join(outws, outputName), 
                                            numNeighbors, numPerms, popUps, 
                                            confLevel, fdr, scaleFactor)

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())