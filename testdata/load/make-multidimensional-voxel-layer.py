import arcpy

# Create the voxel layer
arcpy.md.MakeMultidimensionalVoxelLayer(
    in_dataset=r"C:\data\emu_small_subset.nc",
    out_layer="emu_small_subset_Layer",
    variables=[[False, "ocean_name", "DISCRETE"], [True, "salinity", "CONTINUOUS"], [True, "temp", "CONTINUOUS"]],
    voxel_position="CENTER",
    exaggeration_mode="FROM_VOXEL_DATASET_ORIGIN",
    exaggeration=None,
    offset=None,
    optimize_performance="OPTIMIZED"
)

# Create the voxel scene layer package
arcpy.management.CreateVoxelSceneLayerContent(
    in_dataset="emu_small_subset_Layer",
    out_slpk=r"C:\data\emu_voxel.slpk"
)

# Share the slpk and publish as web scene layer
arcpy.management.SharePackage(
    in_package=r"C:\data\emu_voxel.slpk",
    username="",
    password=None,
    summary="",
    tags="",
    credits="",
    public="MYGROUPS",
    groups=None,
    organization="MYORGANIZATION",
    publish_web_layer="TRUE",
    portal_folder=""
)