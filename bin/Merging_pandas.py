import pandas as pd

print("Merging all 3")
print("-"*20)
# --------------

merged_df = pd.concat([my_db_df, my_json_df, my_text_df], axis=0)
print(merged_df)

merged_df.to_csv("temp2.csv", index=False)

print("#"*40, end="\n\n")
################################

print("Finding Empty cells")
print("-"*20)
# --------------

print(merged_df.isnull())

print("#"*40, end="\n\n")
################################

print("Count Empty cells")
print("-"*20)
# --------------

print(merged_df.isnull().sum())

# 26/Apr/2000

print("#"*40, end="\n\n")
################################

print("fill empty cells with '26/Apr/2000'")
print("-"*20)
# --------------

merged_df["DATE"] = merged_df["DATE"].fillna("26/Apr/2000")
print(merged_df.isnull().sum())

print("#"*40, end="\n\n")
################################

print("Final merged_df")
print("-"*20)
# --------------

print(merged_df)

print("#"*40, end="\n\n")
################################

print('Write to files')
print("-"*20)
# --------------

# pandas_report.csv
merged_df.to_csv("pandas_report.csv", index=False)

# pandas_report.xlsx
merged_df.to_excel("pandas_report.xlsx", index=False)

# pandas_report.xml
merged_df.to_xml("pandas_report.xml")

print("""
Created below reports 

pandas_report.csv
pandas_report.xlsx
pandas_report.xml

please check""")

print("#"*40, end="\n\n")
################################