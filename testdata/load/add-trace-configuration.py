import arcpy
arcpy.un.AddTraceConfiguration(
        r"HydroNetwork", "Upstream_HUC12", "UPSTREAM", 
        "Upstream trace for HUC12_allow indeterminate", ["HUC12", "Upstream"], 
        "NO_DIRECTION", '', "INCLUDE_BARRIERS", "VALIDATE_CONSISTENCY", 
        "DO_NOT_IGNORE_BARRIERS_AT_STARTING_POINTS", "TRACE_INDETERMINATE_FLOW", 
        None, None, "BOTH_JUNCTIONS_AND_EDGES")