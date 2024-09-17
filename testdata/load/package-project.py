import os
import arcpy

enterpriseProjectDir = "\\\\centralFileServer\\gisData\\ArcGISProProjects"
sharedProjectDir = "c:\\publicFiles\\sharedProjects"

walk = arcpy.da.Walk(enterpriseProjectDir, datatype="Project")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        if "oil" in filename.lower():
            project = os.path.join(dirpath, filename)
            outputFile = os.path.join(sharedProjectDir, os.path.splitext(os.path.basename(project))[0] + ".ppkx")
            print("Packaging: {0} to {1}".format(project, outputFile))
            arcpy.management.PackageProject(project, outputFile, "EXTERNAL")