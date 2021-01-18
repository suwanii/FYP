from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd

driver = webdriver.Chrome(r"C:\Users\Suwani Gunasekara\Downloads\chromedriver_win32\chromedriver.exe")
#link to the category page
driver.get('http://topjobs.lk/applicant/vacancybyfunctionalarea.jsp?FA=HOT')
#driver.get('https://mobile.twitter.com/search?q=%23galaxynote7&src=recent_search_click')
content = driver.page_source
soup = BeautifulSoup(content)

linklist = []
pattern = '\/.*\w'
text = "http://topjobs.lk/"

#to scrape the links to the page with the image
for i in range(359):
    print(i)
    job = soup.find(id = 'tr'+str(i))
    link = job.find('a')['href']
    modified_link = re.findall(pattern,link)
    fulllink = text+modified_link[0]
    linklist.append(fulllink)

imagelinks = []
pattern_image = '\/.*\.[pj][np]g'
driver = webdriver.Chrome(r"C:\Users\Suwani Gunasekara\Downloads\chromedriver_win32\chromedriver.exe")

#to scrape the image link in png or jpg format
for i in range(len(linklist)):
    print(i)
    driver.get(linklist[i])
    content = driver.page_source
    soup = BeautifulSoup(content)
    c = soup.find('div',{'id':'remark'})
    image = c.find('img')
    #image = soup.find('img')
    imagelink = re.findall(pattern_image,str(image))
    try:
        fulllink = text+imagelink[0]
        imagelinks.append(fulllink)
    except IndexError:
        print(f"no link {i}")

#put the links into a df
df = pd.DataFrame(imagelinks, columns =['l' ])
df.to_csv(r"C:\Users\Suwani Gunasekara\Downloads\image_links.csv")

# use tab save to download the images


