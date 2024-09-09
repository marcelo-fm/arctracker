import arcpy

arcpy.env.workspace = r"C:\Health.gdb"

in_features = "cancer_deaths"
out_features = "cancer_rate"
rate_fields = "deaths_2024 population_2024; deaths_2023 population_2023"
rate_method = "RAW_RATE"
scaling_factor = 100000

arcpy.stats.CalculateRates(
    in_features, rate_fields,"NO_APPEND", out_features, rate_method, None, 
    None, None, None, None, None, None, scaling_factor)