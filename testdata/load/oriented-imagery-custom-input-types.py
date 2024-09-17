def oriented_imagery_properties(self, input_data, aux_input):
    """Generate the oriented imagery records."""
    metadata = input_data["Metadata File"]
    image_folder = input_data["Image Location"]
    dem = input_data["DEM"]
    def_ground = aux_input["Default Ground Elevation"]
    offset = aux_input["Offset"]

    # Implementation goes here

    yield {
        "SHAPE@": camera_point_geom,
        "Name": image_name,
        "ImagePath": image_path,
        "AcquisitionDate": acquisition_date,
        "CameraHeading": heading,
        "CameraPitch": pitch,
        "CameraRoll": roll,
        "HorizontalFieldOfView": hfov,
        "VerticalFieldOfView": vfov,
        "CameraHeight": camera_height,
        "FarDistance": far_distance,
        "NearDistance": near_distance,
        "OrientedImageryType": oi_type,
        "CameraOrientation": cam_ori,
        "CameraId": int(c_id),
        "CameraType": c_type
    }