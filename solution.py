import requests
from bs4 import BeautifulSoup

company_name =raw_input("Enter the name of company ")

base_url = 'https://www.mptax.mp.gov.in/mpvatweb/dealerSearch.do'

headers = {
	"User-Agent": "Mozilla/5.0",
"Accept": "text/html;q=0.9,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Connection": "close",
"Content-Type": "application/x-www-form-urlencoded"
}

data = {
	"viewKeyHidden":"dlrSearch",	
	"name":company_name
}


r1 = requests.post(base_url,headers=headers,data=data,verify=False)
# print r1.text
soup = BeautifulSoup(r1.text,"html.parser")
tabs = soup.findAll('table',{'class':"tab3"})

headings = ["Sr.No.","Firm Name","TIN No.","Registration Status","Tax Type","Registration Date","Cancellation Date","Circle Name"]
i=0
# data = [company1 ,company2]

for row in tabs[2]:
	for tds in row:
		if(i==8):
			i=i-8
		print headings[i]
		i=i+1
		for td in tds:
			print str(td)

