import arcpy
import datetime

days_valid = 14
expiration_date = (datetime.date.today() + datetime.timedelta(days=days_valid)).strftime("%x")
outputfile = "d:/Data/Output/sandiego.mmpk"

arcpy.management.CreateMobileMapPackage(
    [r"C:\data\Basemap1.mapx", r"C:\data\Map1.mapx"], outputfile, None, 
    r"\\share\layers\AreaOfInterest.lyrx", "DEFAULT", "CLIP", "Title", 
    "Summary", "description", "Tag", "Credits", "Use",
    "STANDARD", "ENABLE_MAP_EXPIRATION",
    "DONOT_ALLOW_TO_OPEN", expiration_date,
    "This map is expired.  Contact the map publisher for an updated map.")