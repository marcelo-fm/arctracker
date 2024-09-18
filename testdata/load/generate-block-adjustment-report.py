import arcpy
mdname = "c:/omproject/adjustedcollection.gdb/droneimgs"
solutiontbl = "c:/omproject/adjustedcollection.gdb/droneimgs_solutiontbl"
solutionpnt = "c:/omproject/adjustedcollection.gdb/droneimgs_solutionpnt"
controlpnt = "c:/omproject/adjustedcollection.gdb/droneimgs_tiepoints"
arcpy.rm.GenerateBlockAdjustmentReport(
        mdname, solutiontbl, solutionpnt, "c:/omproject/adjustmentreport.pdf",
controlpnt, report_format="PDF")