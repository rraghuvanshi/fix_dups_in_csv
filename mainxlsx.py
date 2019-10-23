import os
import glob
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import zipfile

from pandas import DataFrame

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# combine all csv files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

df_duplicates_removed = DataFrame.drop_duplicates(combined_csv, subset=['sourceIP', 'destinationIP'])

df_duplicates_removed.to_csv("dupsremoved.csv", index=False, encoding='utf-8-sig')

zipfile.ZipFile('dupsremoved.zip', 'w', zipfile.ZIP_DEFLATED).write("dupsremoved.csv")
