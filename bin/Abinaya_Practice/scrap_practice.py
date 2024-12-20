


import requests

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# success code - 200
#print(r)

# print content of request
#print(r.content.decode())

from bs4 import BeautifulSoup
bs=(r.content.decode())

soup = BeautifulSoup(bs, "html.parser")
#print(soup)
#print(soup.prettify())


####Get Log Data


log_data1 = soup.body
print(log_data1)


print('&'*60)

log_data2=soup.body.pre.text
print(log_data2)

titles = soup.find_all('h1')
for title in titles:
    print(title.text)
