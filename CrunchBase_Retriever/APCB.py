

# need Python and BeautifulSoup to run

#download webpage from crunchbase

from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup as bs


# the location for the downloaded webpage
baseLocation = "/Users/oliverwang/Downloads/"

# the name of the webpage
htmlName2 = "Zenefits _ CrunchBase.html"



htmlName = htmlName2
htmlLocation = baseLocation+htmlName;
soup = bs(open(htmlLocation, encoding = "utf-8"))
Name = soup.find(id="profile_header_heading").text
Headquarters = soup.find(id="info-card-overview-content").div.dl.find_all('div')[1].find_all('dd')[0].text
Description = soup.find(id="info-card-overview-content").div.dl.find_all('div')[1].find_all('dd')[1].text
Founders = ', '.join([each.text for each in soup.find(id="info-card-overview-content").div.dl.find_all('div')[1].find_all('dd')[2].find_all('a')])
Categories 	= ', '.join([each.text for each in soup.find(id="info-card-overview-content").div.dl.find_all('div')[1].find_all('dd')[3].find_all('a')])
Website = soup.find(id="info-card-overview-content").div.dl.find_all('div')[1].find_all('dd')[4].text
Founded = soup.find(id="timeline-container").div.find_all('div')[1].div.dd.text
Funding = soup.find('span',{'class':'funding_amount'}).parent.text
try:
	Investors = ', '.join([each.text for each in soup.find(id="investors").parent.next_sibling.find_all('h4')])
except:
	Investors 	= ' '

try:
	BoardMember = ', '.join([each.h4.text for each in soup.find(id="board_members_and_advisors").parent.parent.find_all('div',{'class':'info-block'})])
except:
	BoardMember = ' '

Final = Name+'~'+Headquarters+'~'+Description+'~'+Founders+'~'+Categories+'~'+Website+'~'+Founded+'~'+Funding+'~'+Investors+'~'+BoardMember

# where the text file is stored
with open("/Users/oliverwang/Desktop/data.txt", "a") as myfile:
    myfile.write(Final+'\n');
