import os
import arcpy

arcpy.env.workspace = r"c:\ws\texas.gdb"
asset_fcs = ["td_towers", "td_localpd", "td_flt01"]
to_merge = []
out_merged = os.path.join(arcpy.env.workspace, "td_combined_buffers")
buffer_field = "vis_range"
start_field = "starttime"
end_field = "endtime"

for fc in asset_fcs:
   in_fc = os.path.join(arcpy.env.workspace, fc)
   out_fc = os.path.join(arcpy.env.workspace, "{}_b".format(fc))
   arcpy.intelligence.GenerateCoverageAreas(in_fc, out_fc, buffer_field, "", 
                                       start_field, end_field)
   to_merge.append(outfc)

arcpy.Merge_management(to_merge, out_merged)