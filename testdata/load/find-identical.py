import arcpy

from itertools import groupby
from operator import itemgetter

# Set workspace environment
arcpy.env.workspace = r"C:\data\redlands.gdb"

# Run Find Identical on feature geometry only.
result = arcpy.FindIdentical_management("parcels", "parcels_dups", ["Shape"])
    
# List of all output records as IN_FID and FEAT_SEQ pair - a list of lists
out_records = []   
for row in arcpy.SearchCursor(result.getOutput(0), fields="IN_FID; FEAT_SEQ"):
    out_records.append([row.IN_FID, row.FEAT_SEQ])

# Sort the output records by FEAT_SEQ values
# Example of out_records = [[3, 1], [5, 3], [1, 1], [4, 3], [2, 2]]
out_records.sort(key = itemgetter(1))
    
# records after sorted by FEAT_SEQ: [[3, 1], [1, 1], [2, 2], [5, 3], [4, 3]]
# records with same FEAT_SEQ value will be in the same group (i.e., identical)
identicals_iter = groupby(out_records, itemgetter(1))
    
# now, make a list of identical groups - each group in a list.
# example identical groups: [[3, 1], [2], [5, 4]]
# i.e., IN_FID 3, 1 are identical, and 5, 4 are identical.
identical_groups = [[item[0] for item in data] for (key, data) in identicals_iter]

print(identical_groups)