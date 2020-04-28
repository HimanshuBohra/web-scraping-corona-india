import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
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
district_quarantine = page_soup.findAll("span",{"class":"text-blue font-weight-bold"})
district_confirmed = page_soup.findAll("span",{"class":"text-red font-weight-bold"})
district_tested = page_soup.findAll("span",{"class":"text-orange font-weight-bold"})
district_recovered = page_soup.findAll("span",{"class":"text-success font-weight-bold"})
district_death = page_soup.findAll("span",{"class":"font-weight-bold"})
# bar graph for district wise quarantined patients in gujarat
x = []
y_quaran = []
for i in district_name:
        x.append(i.text)

#bar graph for district wise quarantined patients
for i in district_quarantine:
        y_quaran.append(int(i.text))
index = np.arange(len(x))
plt.bar(index,y_quaran)
plt.xticks(index,x,fontsize=5,rotation=45)
plt.show()
#bar graph for district wise confirmed cases in gujarat
y_confirm = []
for i in district_confirmed:
        y_confirm.append(int(i.text))
plt.bar(index,y_confirm)
plt.xticks(index,x,fontsize=5,rotation=45)
plt.show()

#bar graph for district wise tested patients
y_tested = []
for i in district_tested:
        y_tested.append(int(i.text))
plt.bar(index,y_tested)
plt.xticks(index,x,fontsize=5,rotation=45)
plt.show()
#bar graph for district wise recovered patients
y_recovered = []
for i in district_recovered:
        y_recovered.append(int(i.text))
plt.bar(index,y_recovered)
plt.xticks(index,x,fontsize=5,rotation=45)
plt.show()
#bar graph for district wise deaths 
y_death = []
for i in district_death:
        y_death.append(int(i.text))
plt.bar(index,y_death)
plt.xticks(index,x,fontsize=5,rotation=45)
plt.show()
