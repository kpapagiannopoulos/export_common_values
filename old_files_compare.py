import pandas as pd
col_list = ["SECTOR_ID"]
df1 = pd.read_csv('24072022_Actix_CellRef_LTEExports_Ericsson.csv', low_memory=False, usecols=col_list )
df2 = pd.read_csv('export_old_sectors.csv', low_memory=False, usecols=col_list)

result = pd.merge(df1, df2, how="inner").fillna(0).set_index("SECTOR_ID")

print(result)
result.to_csv ('LTE_ERC_MISSING.csv')
