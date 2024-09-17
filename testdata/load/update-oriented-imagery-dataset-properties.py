# Import system modules
import arcpy

# Set local variables
in_oi = "C:/OrientedImageryExample/MyOI.gdb/MyOrientedImageryDataset"
new_maximum_distance = 550
footprint = "MyOrientedImageryDataset_footprint"
new_time_unit = "HOURS"
new_camera_height = 2.5

# Run Update Oriented Imagery Dataset Properties
arcpy.oi.UpdateOrientedImageryDatasetProperties(
    in_oriented_imagery_dataset = in_oi,
    maximum_distance = new_maximum_distance,
    footprint_item = footprint,
    time_interval_unit = new_time_unit,
    camera_height = new_camera_height,
)