import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inSdFile = "myMapService.sd"
inServer = "HOSTING_SERVER"
inServiceName = "newServiceName"
inCluster = "myCluster"
inFolderType = "EXISTING"
inFolder = "existingFolder"
inStartup = "STOPPED"
inOverride = "OVERRIDE_DEFINITION"
inMyContents = "SHARE_ONLINE"
inPublic = "PRIVATE"
inOrganization = "NO_SHARE_ORGANIZATION"
inGroups = ["My Group", "MyGroup 2"]

# Run UploadServiceDefinition
arcpy.server.UploadServiceDefinition(inSdFile, inServer, inServiceName, 
                                     inCluster, inFolderType, inFolder, 
                                     inStartup, inOverride, inMyContents, 
                                     inPublic, inOrganization, inGroups)