# Name: ReconcileVersions.py
# Description: Reconciles all versions owned by a user with SDE.Default

# Import system modules
import arcpy, os

# Set workspace
workspace = 'C:/Data/connections/bender@production.sde'

# Set the workspace environment
arcpy.env.workspace = workspace

# Use a list comprehension to get a list of version names where the owner
# is the current user and make sure sde.default is not selected.
verList = [ver.name for ver in arcpy.da.ListVersions() if ver.isOwner
           == True and ver.name.lower() != 'sde.default']

arcpy.ReconcileVersions_management(workspace,
                                   "ALL_VERSIONS",
                                   "SDE.Default",
                                   verList,
                                   "LOCK_ACQUIRED",
                                   "NO_ABORT",
                                   "BY_OBJECT",
                                   "FAVOR_TARGET_VERSION",
                                   "NO_POST",
                                   "KEEP_VERSION",
                                   "c:\RecLog.txt")
print('Reconciling Complete')