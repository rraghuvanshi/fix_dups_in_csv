import os
import glob
import pandas as pd
import zipfile

from pandas import DataFrame

extension = 'xlsx'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# combine all files in the list
#combined_csv = combined_csv[combined_csv.ClientUserName != 'UK\PRV-raghuvar']
# export to csv
# combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
# df_csv = pd.read_csv('combined_csv.csv')

combined_xlsx = pd.concat([pd.read_excel(f) for f in all_filenames])

df_duplicates_removed = DataFrame.drop_duplicates(combined_xlsx, subset=['sourceIP','destinationIP'])

df_duplicates_removed.to_excel("dupsremoved.xlsx", index=False, encoding='utf-8-sig')

zipfile.ZipFile('dupsremoved.zip', 'w', zipfile.ZIP_DEFLATED).write("dupsremoved.xlsx")

# zout = zipfile.ZipFile(zfilename, "w", zipfile.ZIP_DEFLATED)
