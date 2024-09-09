#====================================
# CreateCloudStorageConnectionFile
# Usage:
# arcpy.management.CreateCloudStorageConnectionFile(
#     out_folder_path, out_name, AZURE | AMAZON | GOOGLE | ALIBABA, bucket_name,
#     {access_key_id}, {secret_access_key}, {region}, {end_point},
#     { {Name} {Value}; {Name} {Value}...})
# arcpy.management.CreateCloudStorageConnectionFile(
#     out_folder_path, out_name, AZURE | AMAZON | GOOGLE | ALIBABA, bucket_name,
#     {access_key_id}, {secret_access_key}, {region}, {end_point},
#     {config_options})

import arcpy

outfolder = "C:/Workspace/connections"
connectname = "planetary_landsat.acs"
provider = "Azure"
accesskey = "landsateuwest"
secretkey = ""
bucketname = "landsat-c2"
folder = ""
region = ""
endpoint = ""
config_options= "ARC_TOKEN_OPTION_NAME AZURE_STORAGE_SAS_TOKEN; ARC_TOKEN_SERVICE_API https://planetarycomputer.microsoft.com/api/sas/v1/token/landsateuwest/landsat-c2"

# Create connection to planetary computer landsat data collection

print(arcpy.CreateCloudStorageConnectionFile_management(outfolder, connectname, provider, bucketname, accesskey, secretkey, region, endpoint, config_options, folder))
print(arcpy.GetMessages())