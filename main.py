import os
import glob
import pandas as pd
import zipfile

from pandas import DataFrame

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, skiprows=1) for f in all_filenames ])

combined_csv = combined_csv[combined_csv.ClientUserName != 'UK\PRV-raghuvar']
#export to csv
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

#df_csv = pd.read_csv('combined_csv.csv')

df_duplicates_removed = DataFrame.drop_duplicates(combined_csv)

df_ipdups_removed = DataFrame.drop_duplicates(combined_csv,subset= 'ClientComputerName')

df_ipdups_removed.to_csv("ipdupsremoved.csv",index=False, encoding='utf-8-sig')

df_duplicates_removed1 = df_duplicates_removed.sort_values(by=['Path','ClientComputerName','ClientUserName'], inplace=False)

df_duplicates_removed1.to_csv("dupsremoved.csv", index=False, encoding='utf-8-sig')

zipfile.ZipFile('dupsremoved.zip', 'w', zipfile.ZIP_DEFLATED).write("dupsremoved.csv")

#zout = zipfile.ZipFile(zfilename, "w", zipfile.ZIP_DEFLATED)