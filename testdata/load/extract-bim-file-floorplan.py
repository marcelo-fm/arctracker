import arcpy

arcpy.conversion.ExtractBIMFileFloorplan(
    in_bim_file_workspace=r"\\BIM\DATA\Example_DA\HUT\HUT_DA_vr2_2023.rvt",
    output_workspace=r"C:\Projects\MyProject136\MyProject136.gdb",
    out_feature_dataset_name="HUT_DA_vr2_2023",
    out_polyline_featureclass_name="HUT_DA_vr2_2023_planline",
    out_polygon_featureclass_name="HUT_DA_vr2_2023_planPolygon",
    out_poi_featureclass_name="HUT_DA_vr2_2023_planPOI",
    out_footprint_featureclass_name="HUT_DA_vr2_2023_Footprint",
    additional_polyline_categories=["ARCHITECTURAL_COLUMN", "STRUCTURAL_COLUMN", "WINDOWS", "FURNITURE", "FURNITURE_SYSTEM"],
    additional_polygon_categories=["AREAS", "ROOMS", "ROOFS"],
    included_levels=["Level 1" "Roof"])