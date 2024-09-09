# Import system modules 
import arcpy

# Overwrite existing output, by default
arcpy.env.overwriteOutput = True

# Local variables...
arcpy.env.workspace = r"c:\projects\dimensionreduction.gdb"

# Reduce the fields of population by age group using Reduced-Rank LDA method; 
# use "State" as the categorical field; choose the eigenvector output. 
arcpy.stats.DimensionReduction("DemographicData", 
           "DemographicData_DimensionReduction", 
           "age_group_1;age_group2;age_group_3;age_group_4;age_group_5", 
           "LDA", "SCALE_DATA", "State", None, None, 
           "APPEND", None, "EigenVectorTable", 0, NEW_OUTPUT)