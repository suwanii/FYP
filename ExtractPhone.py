import re
import glob
import  os
import pandas as pd

df = pd.read_csv("D:\FYP\Text_db_final_2.csv")

tel = {}


def extPhone(index):
    '''
    

    Parameters
    ----------
    index : number
        It will take the index of a given row and checks if it has any 
        pattern specified in the pattern list.

    Returns
    -------
    numbers : list of telephone numbers
    

    '''
    
    t = df.text[index]
    id_ = df.name[index]
    # I need to put several patterns
    pattern = ['\d{3}\s\d{3}\s\d{4}','[+]94\s\d{2}\s\d{7}','[(][+]94[)]\s\d{3}\s\d{3}\s\d{3}',
               '\d{4}\s\d{2}\s\d{2}\s\d{2}','\d{3}\s\d{2}\s\d{2}\s\d{3}','\d{10}','\d\|\s\d{2}\s\d{3}\s\d{3}',
              '\d{4}\s\d{3}\s\d{3}','\d{4}\s\d{6}','\d{7}'
              ]
    numbers = []
    for i in range(len(pattern)):
        num = re.findall(pattern[i],t)
        if len(num) > 0:
            numbers.append(num)
    #print("Len is",len(numbers))
    if len(numbers) == 0:
        print(f"{id_} , {index}")
    else:
        tel[id_] = numbers
        #df.loc[df.name == id_,'Telephone'] = numbers
        return numbers

for i in range(1390):
    extPhone(i)

# combining the extracted telephone number with the existing data frame
df['Tel'] = df['name'].map(tel)

# Putting the df into a csv
#df.to_csv("D:\FYP\Text_db_2.csv")
