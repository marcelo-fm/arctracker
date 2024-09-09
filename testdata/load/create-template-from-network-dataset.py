network = "C:/data/SanDiego.gdb/Transportation/Streets_ND"
output_xml_file = "C:/data/NDTemplate.xml"
arcpy.na.CreateTemplateFromNetworkDataset(network, output_xml_file)