from bs4 import BeautifulSoup
import requests


def get_details(jobs):
    for job in jobs:
        link = 'https://www.glassdoor.ca' + job.get('href')
        print("---------------------------------------------------")
        detail_req = Request(link, headers={
            'User-Agent': 'Mozilla/5.0'})
        detail_data = BeautifulSoup(urlopen(detail_req).read(), 'lxml')
        print(detail_data.find("title").get_text())
        print(link)
        print("---------------------------------------------------")
# import json
# json_jobs = json.loads(jobs)
# for job in json_jobs['itemListElement']:
#     print("---------------------------------------------------")
#     detail_req = Request(job["url"].replace("fr.", ""), headers={
#                          'User-Agent': 'Mozilla/5.0'})
#     detail_data = BeautifulSoup(urlopen(detail_req).read(), 'lxml')
#     print(detail_data.find("title").get_text())
#     print(job["url"].replace("fr.", ""))
#     print("---------------------------------------------------")
#     print(detail_data.find("div", class_="jobDescriptionContent").get_text())


url = 'https://www.glassdoor.ca/Job/vancouver-software-developer-jobs-SRCH_IL.0,9_IC2278756_KO10,28'
try:
    from urllib.request import Request, urlopen
    import sys
    range_len = 4
    for index in range(2, range_len, 1):
        job_url = url + '_IP' + str(index) + '.htm'
        print('JOB_URL', job_url)
        req = Request(job_url, headers={'User-Agent': 'Mozilla/5.0'})
        data = BeautifulSoup(urlopen(req).read(), 'lxml')
        jobs = data.find("div", {"id": "JobResults"}).find_all("a")

        try:
            get_details(jobs)
        except:
            e = sys.exc_info()[0]
            print("no details", e)
except:
    print("Cannot connect to:", job_url)
    print(sys.exc_info()[0])
