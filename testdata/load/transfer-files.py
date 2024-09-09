#===========================
#Transfer files
'''Usage: TransferFiles_management(inputpaths;inputpaths..., outputfolder, {filefilter})'''

import arcpy

#Transfer folder of files with filter
input_folder = "c:\\test\\uploaddata"
output_foler = "c:\\clouconnection\\s3cloudstore.acs\\s3folder"
filter = "*.tif"

arcpy.management.TransferFiles(input_folder, output_foler, filter)