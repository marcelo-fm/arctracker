import arcpy
import os
import json

# Sign in to portal
arcpy.SignInToPortal("https://www.arcgis.com", "MyUserName", "MyPassword")

# Reference map to publish
aprx = arcpy.mp.ArcGISProject(r"C:\Project\World.aprx")
m = aprx.listMaps('World')[0]

# Set output file names
outdir = r"C:\Project\Output"
service_name = "VectorTileLayerExample"
package_filename = service_name + ".vtpk"
package_output_filename = os.path.join(outdir, package_filename)

# Create vector tile package
arcpy.management.CreateVectorTilePackage(m, package_output_filename, "ONLINE")

# Upload and publish vector tile package
result = arcpy.management.SharePackage(package_output_filename, publish_web_layer=True)

print("Finish uploading and publishing package")

# Get the item ID or service URL of the vector tile layer
jobresult = result[1]
result = json.loads(jobresult)

# Publish results JSON response example: {"publishStatus":"<status>","publishMessage":"<message>","publishResult":{"type":"Vector Tile Service","serviceurl":"<service_url>","size":1913146,"jobId":"<ID>","serviceItemId":"<ItemID>"}}
itemID = str(result.get('publishResult', {}).get('serviceItemId'))

print("Start Replacing")

# Set local variables for Replace Web Layer workflow
# target_layer/update_layer can be item ID or service URL; example below uses item ID
target_layer = "808ecf02f39441d69f245c0cb261134b"
archive_layer_name = "ReplaceWebLayerExample_archive"
update_layer = itemID
replace_item_info = "REPLACE"
create_new_item = "TRUE"

# Run Replace Web Layer
arcpy.server.ReplaceWebLayer(target_layer, archive_layer_name, update_layer,
                             replace_item_info, create_new_item)

print("Finished Replacing")