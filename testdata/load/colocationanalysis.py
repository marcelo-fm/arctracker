# Analyze the spatial relationship (colocation) between elementary school locations and hospital locations

# Two categories from the same categorical field.
# Find the colocation of elementary schools and  middle schools

intype = "SINGLE_DATASET"
infc_interest = r"Colocation.gdb\Schools"
outfc = r"Outputs.gdb\School_Colocation"
field_interest = "Facility_Type"
time_field = ""
cat_interest = "Elementary"
infc_neigh = ""
field_neigh = ""
time_field_neigh = ""
cat_neigh = "Middle"
neighborhood_type = "K_NEAREST_NEIGHBORS"
num_neighbors = 8
dist_band = ""
swm_file = ""
temporal_type = ""
time_step_interval = ""
num_permutation = 99
weighting_scheme ="BISQUARE"
out_global_tbl = r"Outputs.gdb\Global_School_Colocation"

arcpy.stats.ColocationAnalysis(intype, infc_interest, outfc, field_interest,
                               time_field, cat_interest, infc_neigh, field_neigh,
                               time_field_neigh, cat_neigh, neighborhood_type,
                               num_neighbors, dist_band, swm_file, temporal_type,
                               time_step_interval num_permutation, weighting_scheme,
                               out_global_tbl)

# Categories from different datasets without categories
# Find the colocation of schools and hospitals

intype = "DATASETS_WITHOUT_CATEGORIES"
infc_interest = r"Colocation.gdb\Schools"
outfc = r"Outputs.gdb\Schools_Hospitals"
field_interest = ""
time_field = ""
cat_interest = ""
infc_neigh = r"Colocation.gdb\Hospitals"
field_neigh = ""
time_field_neigh = ""
cat_neigh = ""
neighborhood_type = "DISTANCE_BAND"
num_neighbors = ""
dist_band = "30 Kilometers"
swm_file = ""
temporal_type = ""
time_step_interval = ""
num_permutation = 199
weighting_scheme ="GAUSSIAN"
out_global_tbl = ""

arcpy.stats.ColocationAnalysis(intype, infc_interest, outfc, field_interest,
                               time_field, cat_interest, infc_neigh, field_neigh,
                               time_field_neigh, cat_neigh, neighborhood_type,
                               num_neighbors, dist_band, swm_file, temporal_type,
                               time_step_interval num_permutation, weighting_scheme,
                               out_global_tbl)

# Categories from two datasets
# Find the colocation of elementary schools and hospitals

intype = "TWO_DATASETS"
infc_interest = r"Colocation.gdb\Schools"
outfc = r"Outputs.gdb\Elementary_Hospitals"
field_interest = "Facility_Type"
time_field = ""
cat_interest = "Elementary"
infc_neigh = r"Colocation.gdb\Hospitals"
field_neigh = ""
time_field_neigh = ""
cat_neigh = ""
neighborhood_type = "K_NEAREST_NEIGHBORS"
num_neighbors = 15
dist_band = ""
swm_file = ""
temporal_type = ""
time_step_interval = ""
num_permutation = 499
weighting_scheme ="NONE"
out_global_tbl = ""

arcpy.stats.ColocationAnalysis(intype, infc_interest, outfc, field_interest,
                               time_field, cat_interest, infc_neigh, field_neigh,
                               time_field_neigh, cat_neigh, neighborhood_type,
                               num_neighbors, dist_band, swm_file, temporal_type,
                               time_step_interval num_permutation, weighting_scheme,
                               out_global_tbl)