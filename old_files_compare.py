import pandas as pd
col_list = ["SECTOR_ID"]
df1 = pd.read_csv('24072022_Actix_CellRef_5GExport_Ericsson.csv', low_memory=False, usecols=col_list )
df2 = pd.read_csv('export_old_sectors.csv', low_memory=False, usecols=col_list)

result = df1.merge(df2, on="SECTOR_ID", how="left").fillna(0).set_index("SECTOR_ID")

print(result)
result.to_csv ('5G_ERC_MISSING.csv')
