import pandas as pd
import re

# Import data
df = pd.read_csv("D:\FYP\Text_db_final_2.csv")

# Initializing a dictionary to put the extracted addresses
adrs = {}

def extractAdd(index):
    t = df.text[index]
    id_ = df.name[index]
    # I need to put several patterns
    patterns = ['No[.]\s[0-9]{1,3},\s.+,.\s\w+[.]','No[.]\s*[0-9]{1,3}\/*[0-9]{1,3},\s.+,\s\w+\W\d*',
                '[0-9]{1,3},\s+.+,\s+\w+\W\d*','No[.]\s[0-9]{1,3},\s.+,\s\w+\s']
              
    address = []
    '''
    while len(address)<0:
        for i in range(len(patterns)):
            address = re.findall(patterns[i],t)
            #if len(addtess) > 
    '''
    
    for i in range(len(patterns)):
        address = re.findall(patterns[i],t)
        if len(address) > 0 :
            break
   
    
    #print("Len is",len(numbers))
    if len(address) == 0:
        print(f"{id_} , {index}")
    else:
        adrs[id_] = address



for i in range(3000):
    extractAdd(i)

# Combining the extracted address number with the existing data frame
df['Address'] = df.name.map(adrs)

#df.to_csv("D:\FYP\Text_db_3.csv")
       
    