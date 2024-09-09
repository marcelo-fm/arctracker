# Import arcpy module
import arcpy

# Local variables:
ent_gdb = "/usr/gdbs/enterprisegdb.sde"
authorization_file = "/usr/scratch/keycodes"

# Process: Import authorization information from a new keycodes file.
arcpy.management.UpdateEnterpriseGeodatabaseLicense(ent_gdb, authorization_file)