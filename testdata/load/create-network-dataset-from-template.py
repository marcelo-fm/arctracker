# Name: NetworkDatasetTemplate_workflow.py
# Description: Create a new network dataset with the same schema as an existing
#               network dataset
# Requirements: Network Analyst Extension

#Import system modules
import arcpy
import os

try:
    #Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")
    
    #Set local variables
    original_network = "C:/data/Region1.gdb/Transportation/Streets_ND"
    new_network_location = "C:/data/Region2.gdb/Transportation"
    xml_template = "C:/data/NDTemplate.xml"
    
    #Create an XML template from the original network dataset
    arcpy.na.CreateTemplateFromNetworkDataset(original_network, xml_template)

    #Create the new network dataset in the output location using the template.
    #The output location must already contain feature classes and tables with 
    #the same names and schema as the original network.
    arcpy.na.CreateNetworkDatasetFromTemplate(xml_template,
                                                new_network_location)
    
    #Build the new network dataset
    arcpy.na.BuildNetwork(os.path.join(new_network_location, "Streets_ND"))

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print(("An error occurred on line %i" % tb.tb_lineno))
    print((str(e)))