# Name: DisableEditorTracking.py
# Description: Disables editor tracking on a feature class.

# Import arcpy module
import arcpy

# Local variables:
Buildings = "d:\\RC.gdb\\RC\\Buildings"

# Process: Disable Editor Tracking
arcpy.DisableEditorTracking_management(Buildings,
                                       "DISABLE_CREATOR",
                                       "DISABLE_CREATION_DATE",
                                       "DISABLE_LAST_EDITOR",
                                       "DISABLE_LAST_EDIT_DATE")