import os
import arcpy

enterpriseProjectDir = "\\\\centralFileServer\\gisData\\ArcGISProProjects"
localProjectDir = "c:\\GISdata\\localProjects"

walk = arcpy.da.Walk(enterpriseProjectDir, datatype="Project")

for dirpath, dirnames, filenames in walk:
    for fname in filenames:
        project = os.path.join(dirpath, fame)
        outputFolder = os.path.join(localProjectDir, 
                                    os.path.splitext(os.path.basename(project))[0])
        print("Consolidating: {0} to {1}".format(project, outputFolder))
        arcpy.management.ConsolidateProject(project, outputFolder, "INTERNAL")