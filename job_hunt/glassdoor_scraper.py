from bs4 import BeautifulSoup
import requests


def get_details(jobs):
    import json
    json_jobs = json.loads(jobs)
    for job in json_jobs['itemListElement']:
        print("---------------------------------------------------")
        detail_req = Request(job["url"].replace("fr.", ""), headers={
                             'User-Agent': 'Mozilla/5.0'})
        detail_data = BeautifulSoup(urlopen(detail_req).read(), 'lxml')
        print(detail_data.find("title").get_text())
        print(job["url"])
        print("---------------------------------------------------")
        print(detail_data.find("div", class_="jobDescriptionContent").get_text())


url = 'https://www.glassdoor.ca/Job/vancouver-software-developer-jobs-SRCH_IL.0,9_IC2278756_KO10,28.htm'
try:
    from urllib.request import Request, urlopen

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = BeautifulSoup(urlopen(req).read(), 'lxml')
    jobs = data.find("div", {"id": "JobResults"}).find_all(
        "script")[0].get_text()
    get_details(jobs)

except:
    print("Cannot connect to:", url)
