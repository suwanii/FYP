import pandas as pd
import re

df = pd.read_csv("D:\FYP\Text_db_final_2.csv")

pattern = '\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}'

email = {}

def extemail(index):
    '''

    Parameters
    ----------
    index : number
        It will take the index of a given row and checks if it has any 
        pattern specified in the pattern list.
      
    Returns
    -------
    None.

    '''
    t = df.text[index]
    id_ = df.name[index]
    try:
        print(f"extracting {index}")
        mail = re.findall(pattern,t)
        # print outs the ads without email
        if len(mail) == 0:
            print(f"{id_} , {index}")
        else:
            email[id_] = mail
    except TypeError:
        print(f"Error in {id_}-----------------------------------------{index}")

for i in range(1389):
    extemail(i)

# Combining the extracted telephone number with the existing data frame
df['Email'] = df.name.map(email)

#df.to_csv("D:\FYP\Text_db_3.csv")