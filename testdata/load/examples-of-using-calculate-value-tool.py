Expression:
fn("%Input Feature Class%")

Code Block:
def fn(InputFC):
	   # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True

    # Process: Select Layer By Attribute (Select Layer By Attribute) (management)
    InputFC_Layer, Count = arcpy.management.SelectLayerByAttribute(InputFC, "NEW_SELECTION", "LABEL LIKE '%HIGHWAY%'")

    # Process: Copy Features (Copy Features) (management)
    copyFeaturesOutput = "C:\\temp\\Output.gdb\\copyFeaturesOutput"
    arcpy.management.CopyFeatures(InputFC_Layer, copyFeaturesOutput)

    # Process: Buffer (Buffer) (analysis)
    bufferOutput = "C:\\temp\\Output.gdb\\bufferOutput"
    arcpy.analysis.Buffer(copyFeaturesOutput, bufferOutput, "1500 Feet")
    return bufferOutput