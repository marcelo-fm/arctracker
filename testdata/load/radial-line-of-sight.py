# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Select points from observers from input
observers =  "Observers"
branch = "Branch"
whereClause = "Marines = 'Yes'"
arcpy.analysis.Select(branch, Marines, whereClause)

# Create Radial Line Of Sight using Marine observers
in_observer_features = "Observers"
in_surface = "Elevation_Dataset"
out_feature_class = "RLOS_Observers_Marines"
radius = "METERS"
observer_height_above_surface = "METERS"
arcpy.defense.RadialLineOfSight(Observers,
                                Elevation_Dataset,
                                RLOS_Observers_Marines,
                                1000,
                                2)