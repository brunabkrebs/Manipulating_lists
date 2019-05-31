from tkinter import askopenfilename
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel(askopenfilename())
print('Column headings:')
print(df.columns)

#LISTS BASICS
#to make a subset of the table:
listofcolors=df['blue'] #blue is the column name

#to see items in a list:
print(df['blue'])

#to call specific item in specific index:
print(df['blue'][1])

#to transform sub-dataframe to list:
listofcolors=listofcolors.tolist()

#############################################################

#PIPELINE TO FILTER TABLE
#open excel file with table
df=pd.read_excel(askopenfilename())

#determine column that determines which rows stay 
listofcolors=df['blue']

#copy results to new list to not alter original one
listofcolorsupdated = listofcolors.copy()

#if the item is what you want it to be in the original list, substitute it for 1 (or True) in the copied list
for i in range(4):
    if listofcolors[i]=='brown':
        listofcolorsupdated[i]=1
        
#make a list of only Trues from previous step
cells=(listofcolorsupdated==1)

#make new list with all rows with the index from previous step
newcelllist=(df[cells])

#save an excel file with the updated list
newlist = pd.ExcelWriter('table.xlsx', engine='xlsxwriter')
df.to_excel(newlist, sheet_name='Objects')
newlist.save()


###############################################################



