import arcpy

arcpy.env.workspace = r'c:\data'
arcpy.management.CreateMobileScenePackage(
    'Yosemite.mapx','YosemiteOffline.mspk', None, None, 'DEFAULT', 'SELECT', 
    'YosemiteOfflineScene', 
    'Offline mobile scene package for Yosemite National Park', None, 
    'mspk, yosemite, offline', None, None, 'STANDARD', 'DESKTOP', 
    'DISABLE_SCENE_EXPIRATION', 'ALLOW_TO_OPEN')