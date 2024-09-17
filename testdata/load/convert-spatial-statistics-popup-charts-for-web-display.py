import arcpy
arcpy.env.workspace = r"C:\Analysis\health.gdb"

#Run a tool from the Spatial Statistics or Space Time Mining toolbox that generates popup charts
arcpy.LocalBivariateRelationships_stats("us_counties", "life_expectancy", "physical_activity", "LBR_life_expectancy_physical_activity")

# Run the Convert Spatial Statistics Popup Charts for Web Display tool
arcpy.stats.ConvertSSPopup("LBR_life_expectancy_physical_activity", "LBR_popups", None, None, "NO_ROTATE")