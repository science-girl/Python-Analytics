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


def google_sector_report():

    try:
        energy_data = get_file_data('Energy.htm')
        energy_dict = {}
        rows = energy_data.find(
            "table", class_="topmovers").find_all("tr")
        for row in rows:
            name = ""
            if not row.find("a") == None:
                name = row.find("a").get_text()
            cells = row.find_all("td")
            for cell in cells:
                if not cell.find("span", class_="chg") == None:
                    energy_dict[name] = cell.find_all(
                        "span", class_="chg")[1].get_text().split("%)")[0].split("(")[1]
                if not cell.find("span", class_="chr") == None:
                    energy_dict[name] = cell.find_all(
                        "span", class_="chr")[1].get_text().split("%)")[0].split("(")[1]
        print(energy_dict)
        # finance_data = get_file_data('Google Finance.htm')
        # industrial_data = get_file_data('Industrials.htm')
        # basic_mat_data = get_file_data('Basic Materials.htm')
    except:
        print("Unable to process HTML files")

    # return json_string


google_sector_report()
