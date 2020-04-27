import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
url = 'https://gujcovid19.gujarat.gov.in/'
#openning connection,grabbing page
uClient = uReq(url)
page_html = uClient.read()
# closing the connection
uClient.close()
#html parsing
page_soup = soup(page_html,"html.parser")
# has each district names is gujarat    
district_name = page_soup.findAll("td",{"class":"text-left"})
district_row = page_soup.findAll("span",{"class":"text-blue font-weight-bold"})
#print(district_row[2].span)
x = []
y = []
for i in district_name:
        x.append(i.text)
for i in district_row:
        y.append(int(i.text))
#print(max(y))
#index = np.arange(0,max(y),500)
#print(index)
index = np.arange(len(x))
plt.bar(index,y)
plt.xticks(index,x,fontsize=5,rotation=45)
plt.show()
