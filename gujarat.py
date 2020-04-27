import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
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
district_row = page_soup.findAll("td",{"class":"text-right"})
#print(district_row[2].span)
for i in district_row:
    print(i.span.text)