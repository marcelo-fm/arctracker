import arcpy
arcpy.ba.ImportSegmentationProfile(r"C:\temp\importprofile.csv", "Total Households", r"C:\output\CustomerProfile.sgprofile", "Seg_ID", "Count_int", "Total_Volume")