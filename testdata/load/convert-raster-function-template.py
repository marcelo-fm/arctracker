#import arcpy module
import arcpy

#Set input parameters
in_json = "c:\\test\\aspect.json"
out_rftxml = "c:\\test\\aspect.rft.xml"
out_file_type = "XML"

#Convert json to rft.xml
arcpy.ConvertRasterFunctionTemplate_management(in_json, out_rftxml, out_file_type)