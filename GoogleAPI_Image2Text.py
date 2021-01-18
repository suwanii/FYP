import os, io
from google.cloud import vision_v1
import pandas as pd
import re
import glob

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\Suwani Gunasekara\Documents\my-env\googlapienv\quick-processor-301608-828388966b3f.json"
client = vision_v1.ImageAnnotatorClient()

#file_name = 'cable car.jpg'
#image_path = f'.\VisionAPI\Images\{file_name}'

pattern = '\w+\.'
pattern_diluni = '\w+\s.+\.'
def detectText(img):
    
    txtname = re.findall(pattern,img)
    print(txtname)
    
    with io.open(img, 'rb') as image_file:
        content = image_file.read()
    
    # construct an iamge instance
    image = vision_v1.types.Image(content=content)
    # annotate Image Response
    response = client.text_detection(image=image)  # returns TextAnnotation
    df = pd.DataFrame(columns=['locale', 'description'])
    
    texts = response.text_annotations
    for text in texts:
        df = df.append(
            dict(
                locale=text.locale,
                description=text.description
            ),
            ignore_index=True
        )
    
    #print(df['description'][0])
    with open(txtname[0]+'txt','w',encoding='utf-8') as f:
        f.write(df['description'][0])


#detectText(r"D:\FYP\Images\topjobs\AccountingAuditingFinance")
       
for name in glob.glob(r'D:\FYP\Images\topjobs\Office Admin-Secretary-Receptionist/*'): 
    print(name)
    detectText(name)
  