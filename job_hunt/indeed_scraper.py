#
# for now run: 
#    python -u .\indeed_scraper.py > <output.txt>
#

import requests
from bs4 import BeautifulSoup
from lxml import html

def getRowResult(div):
    try:
        job_url = "https://ca.indeed.com" + div.find("a", class_="turnstileLink").get("href")
        job_details = BeautifulSoup(requests.get(job_url).content, 'lxml')
        print("-------------------------------------------------------------")
        print(job_details.find("title").get_text())
        print(job_url)
        print("-------------------------------------------------------------")
            
        print(job_details.find("span",{"id":"job_summary"}).get_text())
    except:
        print("Failed to get job details")

def getTotalResults(results):
    num_results_str = results.find("div",  {"id":"searchCount"}).get_text().split()
    return int(num_results_str[len(num_results_str)-1].replace(',', ''))
    

def main():
    url='https://ca.indeed.com/jobs?q=software+developer&l=Vancouver%2C+BC'

    try:
        response = requests.get(url)
        if not response.status_code == 200:
            return
        results = BeautifulSoup(response.content, "lxml")
        range_len = int(getTotalResults(results) / 10.0)

        num = 0
        for page in range(10,range_len, 10):
            url = url + "&start=" + str(page)
            response = requests.get(url)
            if not response.status_code == 200:
                return
            results = BeautifulSoup(response.content, "lxml")

            divs = results.find_all("h2", class_="jobtitle")
            for div in divs:
                getRowResult(div)
                num += 1
        print(num)
  
    except:
        print("Failed to access ", url)

main()