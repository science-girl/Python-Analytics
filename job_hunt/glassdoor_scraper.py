from bs4 import BeautifulSoup
import requests


def get_details(jobs):
    job_set = set()
    for job in jobs:
        job_set.add(job.get('href'))
    for j in set(job_set):
        if j.find('&jobListingId=') > 0:
            link = 'https://www.glassdoor.ca' + j
            detail_req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            detail_data = BeautifulSoup(urlopen(detail_req).read(), 'lxml')
            print("---------------------------------------------------")
            print(detail_data.find("title").get_text())
            print(link)
            print("---------------------------------------------------")
            print(detail_data.find("div", class_="jobDescriptionContent").get_text())


def get_num_pages(data):
    try:
        start = data.find("script").get_text().find('[') + 1
        end = data.find("script").get_text().find(';') - 1
        cleaned = data.find("script").get_text()[start:end].replace("\'", "\"")
        import json
        json_results = json.loads(cleaned.replace("\t", "").replace(
            "\n", "").replace("[,", "["))
        total_search_results = json_results['search']['totalSearchResults']
        range_len = json_results['search']['displayedSearchResults']
    except:
        print("Error retrieving number of pages")
        return
    return int(int(total_search_results) / int(range_len))


url = 'https://www.glassdoor.ca/Job/vancouver-software-developer-jobs-SRCH_IL.0,9_IC2278756_KO10,28'
try:
    from urllib.request import Request, urlopen
    import sys
    req = Request(url + '.htm', headers={'User-Agent': 'Mozilla/5.0'})
    data = BeautifulSoup(urlopen(req).read(), 'lxml')
    num_pages = get_num_pages(data)

    for index in range(2, num_pages):
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
    print("Cannot connect to:", url)
    print(sys.exc_info()[0])
