import sys

import csv
from bs4 import BeautifulSoup

# url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4"

with open("covid-19.html", "r") as f:
    html_content = f.read()
fptr = open("statistics.csv", "w")

content = BeautifulSoup(html_content, "html.parser")
nation_table = content.find("div", attrs={"id": "nationTable"})
trs = nation_table.find_all("tr", attrs={"class": "VirusTable_1-1-314_3m6Ybq"})

csv_writer = csv.writer(f)

for tr in trs:
    information = []
    tds = tr.find_all("td")
    for i in range(len(tds)):
        information.append(tds[i].text.strip())
    csv_writer.writerow(information)

fptr.close()