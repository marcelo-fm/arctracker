# Import system modules
import os
import arcpy

# Get Parameters
layers = arcpy.GetParameter(0)  # Accepts Feature Layers (multivalue)
sym = arcpy.GetParameter(1)  # Accepts a Feature Layer

# Apply symbology to each input layer, store the result objects in a list
results = []
for layer in layers:

    # Derive the name of the output featureclass
    layername = arcpy.Describe(layer).baseName
    outfeature = os.path.join(arcpy.env.scratchGDB, layername + "_out")

    # Copy feature to get output. This step can be replaced by other
				# steps that produce or manipulate a featureclass.
    arcpy.management.CopyFeatures(layer, outfeature)

				# Apply symbology to the final output
    res = arcpy.management.ApplySymbologyFromLayer(outfeature, sym)

    # Append multivalue feature
    results.append(res)

# Set the symbology of the derived output parameter using the 
# list of result objects
arcpy.SetParameter(2, results)