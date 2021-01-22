import re
import glob
import  os
import pandas as pd

# Initializing dictionary to put the content
c = {}

# List to put files that did not get appended 
notappend = []

# Naming pattern to name each text file
#namepattern = '\w\w_\d{2}_\d{2}_\d+'
pattern = '\w+\.'
pattern_diluni = '\w+\s.+\.'

pattern_common = '\w\w_+\s*.+\.'

def txtTodf(folder_name):
    # Folder_name = path to the folder which contains txt files
    
    file_list = glob.glob(os.path.join(os.getcwd(), folder_name, "*.txt"))
    for i in range(len(file_list)):
        name = re.findall(pattern_common,file_list[i])
        try:
            print(file_list[i])
            with open(file_list[i],encoding='utf-8') as f_input:
                c[name[0]] = f_input.read()
        except UnicodeDecodeError:
            print(f'Did not work for {file_list[i]}')
            notappend.append(name[0])
            
txtTodf("D:\FYP\Text\googleAPI\Accounting, Auditing, Finance")
            
for name in glob.glob(r'D:\FYP\Text\googleAPI\*'): 
    print(name+'+++++++++++++++++++++++++++++++')
    txtTodf(name)
# Converting the dictionary to a df
df = pd.DataFrame(list(c.items()),columns = ['name','text']) 
# Replacing \n 
df.text = df.text.apply(lambda x: x.replace("\n"," "))

df.to_csv("D:\FYP\Text_db_final_test.csv",encoding = "utf-8")
#txtTodf(r"D:\FYP\Text\googleAPI\Eng-Mech-Auto-Elec")
