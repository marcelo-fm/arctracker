import os
import arcpy
arcpy.CheckOutExtension("network")

gtfs_folders = [
    r"E:\GTFS\Agency1",
    r"E:\GTFS\Agency2"
]
streets_orig = r"E:\Data\StreetData.gdb\Streets"

working_folder = r"E:\TransitAnalysis"
nd_template = os.path.join(working_folder, "TransitNetworkTemplate.xml")
gdb_name = "TransitNetwork.gdb"
out_gdb = os.path.join(working_folder, gdb_name)
fd_name = "TransitNetwork"
fd_path = os.path.join(out_gdb, fd_name)
streets = os.path.join(fd_path, "Streets")
nd_name = "TransitNetwork_ND"
nd_path = os.path.join(fd_path, nd_name)

# Create a file geodatabase and feature dataset to store the network dataset
arcpy.management.CreateFileGDB(working_folder, gdb_name)
arcpy.management.CreateFeatureDataset(out_gdb, fd_name, arcpy.SpatialReference(4326))

# Copy the streets data into the feature dataset so it can be used by the network dataset
# If the original streets are not in the same spatial reference as the feature dataset, you might
# need to use the Project tool instead of Copy.
arcpy.management.Copy(streets_orig, streets)

# Convert the GTFS dataset into public transit data model tables and feature classes
arcpy.transit.GTFSToPublicTransitDataModel(gtfs_folders, fd_path)

# Connect the transit stops to the streets and create the rest of the data model feature classes
# Use an expression to connect transit stops only to streets where pedestrians are allowed.
where = "PedestriansAllowed = 1"
arcpy.transit.ConnectPublicTransitDataModelToStreets(fd_path, streets, "100 meters", where)

# Create the network dataset from a template
arcpy.na.CreateNetworkDatasetFromTemplate(nd_template, fd_path)

# Build the network dataset
arcpy.na.BuildNetwork(nd_path)