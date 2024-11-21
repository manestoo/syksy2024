import requests
import csv

response = requests.get("http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=22")
lines = response.text.strip().split(',')

with open('hae_tiedot.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(lines)
