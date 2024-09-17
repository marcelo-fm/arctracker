import arcpy
arcpy.management.CreateCustomVerticalTransformation(
    vt_name="NAD_1983_2011_ellipsoid_to_GEOID18b",
    source_vt_coor_system='VERTCS["NAD_1983_2011",DATUM["D_NAD_1983_2011",SPHEROID["GRS_1980",6378137.0,298.257222101]],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]',
    target_vt_coor_system='VERTCS["NAVD88_height_(ftIntl)",VDATUM["North_American_Vertical_Datum_1988"],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Foot",0.3048]]',
    interpolation_gcs='GEOGCS["GCS_NAD_1983_2011",DATUM["D_NAD_1983_2011",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]',
    custom_vt="GEOID|g2018u0.bin|Bilinear",
    extent='-110 30 -80 40 GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]',
    accuracy=0.5
)