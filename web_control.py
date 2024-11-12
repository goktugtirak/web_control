import csv
from datetime import datetime
import requests
import json

url_logs = []

with open("url_list.csv", mode="r", newline="") as csv_file:
    urls = csv.reader(csv_file)
    for url in urls:
        r = requests.get(url[1])
        date = datetime.now()
        control_date = datetime.strftime(date, '%c')
        
        n = {
                "name": url[0],
                "url": url[1],
                "control_date": control_date,
                "status_code": r.status_code,
                "response_time": r.elapsed.total_seconds()
                }

        url_logs.append(n)

        with open("url_log.json", mode="w") as log_file:
            json.dump(url_logs, log_file, indent=4)
