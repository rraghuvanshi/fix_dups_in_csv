import os
import glob
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import zipfile

from pandas import DataFrame

extension = 'xlsx'

if extension == 'xlsx':
    all_xlsfilenames = [i for i in glob.glob('*.{}'.format(extension))]
    count = 0
    suffix = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for file in all_xlsfilenames:
        csvname = file+suffix[count]+"."+"csv"
        data_xls = pd.read_excel(file, '2019-10-21-data_export', index_col=None)
        data_xls.to_csv(csvname, encoding='utf-8', index=False)
        count = count + 1
        data_xls = None

count = None


# combine all csv files in the list
all_filenames = [i for i in glob.glob('*.{}'.format('csv'))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

df_duplicates_removed = DataFrame.drop_duplicates(combined_csv, subset=['sourceIP', 'destinationIP'])

df_duplicates_removed.to_csv("dupsremoved.csv", index=False, encoding='utf-8-sig')

zipfile.ZipFile('dupsremoved.zip', 'w', zipfile.ZIP_DEFLATED).write("dupsremoved.csv")








