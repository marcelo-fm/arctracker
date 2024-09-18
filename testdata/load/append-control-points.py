#append control points

import arcpy
arcpy.env.workspace = "c:/workspace"

#append the control points and tie points
target = "BD.gdb/tiePoints"
in_controlPoints = "BD.gdb/controlPoints"
dem = "BD.gdb/dem"
AOI = "-79.6407162269889 43.4853802421312 -79.094324938576 44.0836924137218"
AppOpt = "GCP"


arcpy.rm.AppendControlPoints(target, in_controlPoints, "", dem, "", "", "", AOI, appOpt)