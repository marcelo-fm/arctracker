# Import system modules
import arcpy
import os

arcpy.env.workspace = "C:/OrientedImageryExample"

# Set local variables
fld = r"C:\OrientedImagerySamples"
oi_dataset = "C:\OrientedImageryExample\Sample.gdb\oi_dataset"
in_file = os.path.join(fld, "sampleinput.csv")
in_folder = os.path.join(arcpy.GetInstallInfo()['InstallDir'], 'Resources',
                         'OrientedImagery', 'CustomInputTypes',
                         'SampleInputType')
img_folder = os.path.join(fld, "Images")
img_ext = "mrf"
in_data= f'"CSV File" {in_file};"Image Folder" {img_folder};"Image Extension" {img_ext}'

# Run Add Images From Custom Input Type
arcpy.oi.AddImagesFromCustomInputType(
    oi_dataset, input_type="SampleInputType", in_type_folder="in_folder",
    in_data=in_data)