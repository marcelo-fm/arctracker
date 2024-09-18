import arcpy

arcpy.CheckOutExtension("ImageAnalyst")

in_video = "c:\\test\\drone_vid.ts"
out_metadata = "c:\\output\\outmeta.csv"
flight_path = "C:\\test\\meta.gdb\\flight_path"
flight_path_type = "POLYLINE"
image_path = "C:\\test\\meta.gdb\\image_path"
image_path_type = "POINT"
image_footprint = "C:\\test\\meta.gdb\\image_footprint"
start_time = "1 Seconds"
stop_time = "60 Seconds"
distance_between = "2 Meters"
min_time_between = "20 Seconds"

arcpy.ia.VideoMetadataToFeatureClass(
    in_video, out_metadata, flight_path, flight_path_type, image_path,
    image_path_type, image_footprint, start_time, stop_time, distance_between,
    min_time_between)