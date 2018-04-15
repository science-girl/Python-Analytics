from bs4 import BeautifulSoup
import requests

url = 'https://www.glassdoor.ca/Job/vancouver-software-developer-jobs-SRCH_IL.0,9_IC2278756_KO10,28.htm'
try:
    from urllib.request import Request, urlopen

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = BeautifulSoup(urlopen(req).read(), 'lxml')
    # print(data)
    jobs = data.find("div", {"id": "JobResults"}).find_all(
        "script")[0].get_text()
    print(jobs)

except:
    print("Cannot connect to:", url)
