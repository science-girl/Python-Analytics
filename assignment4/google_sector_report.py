"""
Modify the following google_sector_report so that it returns a json
dump that contains the following information about each sector:
1. The sector name
2. The percentage change in sector value
3. The biggest gainer and the percentage change in the biggest gainer
4. The biggest loser and the percentage change in the biggest loser

The structure of the json is given in the assignment description on EdX.

Note:
To read files, use:

with open('filename') as f:
    lines = f.readlines()
"""


def get_file_data(file_name):
    from bs4 import BeautifulSoup
    try:
        with open(file_name) as f:
            return BeautifulSoup(f, 'lxml')
    except:
        print("Cannot read: ", file_name)
        return


def get_sector_data(data):
    sector_title = data.find(
        "div", class_="hdg top appbar-hide").get_text().strip()
    sector_dict = {}
    rows = data.find("table", class_="topmovers").find_all("tr")
    for row in rows:
        name = ""
        if not row.find("a") == None:
            name = row.find("a").get_text()
        cells = row.find_all("td")
        for cell in cells:
            if not cell.find("span", class_="chg") == None:
                sector_dict[name] = float(cell.find_all("span", class_="chg")[
                    1].get_text().split("%)")[0].split("(")[1])
            if not cell.find("span", class_="chr") == None:
                sector_dict[name] = float(cell.find_all("span", class_="chr")[
                    1].get_text().split("%)")[0].split("(")[1])
    sector_sorted = sorted((value, key)
                           for (key, value) in sector_dict.items())
    sector_json = {}
    sector_json[sector_title] = {"biggest_gainer": {
        "equity": sector_sorted[len(sector_sorted)-1][1], "change": sector_sorted[len(sector_sorted)-1][0]}, "biggest_loser": sector_sorted[0][1], "change": sector_sorted[0][0]}
    return sector_json


def google_sector_report():

    try:
        energy_data = get_file_data('Energy.htm')
        print(get_sector_data(energy_data))
        # finance_data = get_file_data('Google Finance.htm')
        # industrial_data = get_file_data('Industrials.htm')
        # get_sector_data(industrial_data)
        # basic_mat_data = get_file_data('Basic Materials.htm')
    except:
        print("Unable to process HTML files")

    # return json_string


google_sector_report()
