import requests
import urllib
import json
import re
from bs4 import BeautifulSoup

#web = urllib.urlopen("https://www.instagram.com/nataliengibson")

url = "https://www.instagram.com/" + raw_input("Enter instagram handle of person")

response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')
#data = soup.find_all("script")[19].string

#print(soup.prettify())

dp = soup.find_all("script")

link= dp[1].text

startindex = dp[1].text.find("profile_pic_url_hd") + 22

endindex = startindex

while link[endindex]!= '"' :
    endindex = endindex + 1

#endindex = endindex-1

#print(link[startindex],link[endindex])

#print(link[startindex:endindex])

urllib.urlretrieve(link[startindex:endindex], "./profilepic.jpg")

arr = []


arr = [ m.start() for m in re.finditer('thumbnail_src', dp[1].text)]
#print(arr)

for i in range(0,len(arr)) :
    tempstart = arr[i] + 17
    tempend = tempstart
    #print(link[tempstart])

    while link[tempend]!='"' :
        tempend = tempend + 1

    #print(link[tempstart:tempend])
    location = "./image" + str(i)
    urllib.urlretrieve(link[tempstart:tempend], location)

