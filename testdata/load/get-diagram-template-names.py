# Name: ExportAllDiagramTemplateDefinitions.py
# Description: Export definitions of all diagram templates related to a given network.

# Import system modules
import arcpy
import os
import re

# Initialize variables
msgInputsErr = "Invalid arguments."
msgScriptErr = "Error during script operation."
ndbd_ext = ".ndbd"
ndld_ext = ".ndld"

# Set overwrite option
arcpy.env.overwriteOutput = True

# Decodes parameters
try:
    input_Network = arcpy.GetParameterAsText(0)
    input_Folder = arcpy.GetParameterAsText(1)

    if input_Network == "" or input_Folder == "" :
        raise Exception()

except Exception:
    arcpy.AddError(msgInputsErr)
    raise

# Main code
try:
    arcpy.AddMessage("Retrieving the templates list...")
    output_TemplateNames = arcpy.GetDiagramTemplateNames_nd(input_Network)
    templateNamesList = re.split(';', str(output_TemplateNames))
    arcpy.AddMessage("Looping on each template...")
    for template in templateNamesList:
        message = "Exporting template: {}".format(template)
        arcpy.AddMessage(message)
        arcpy.ExportDiagramTemplateDefinitions_nd(input_Network, template, 
                                                  os.path.join(input_Folder, template + ndbd_ext), 
                                                  os.path.join(input_Folder, template + ndld_ext))

except Exception:
    arcpy.AddError(msgScriptErr)
    raise