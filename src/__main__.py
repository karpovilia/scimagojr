import os
import datetime
import json


from scimagojr.scraping import load_data

todaystr = datetime.date.today().isoformat()
basedir = "/home/alena/repos/scimagojr/"
res_file_path = os.path.join(basedir, f"scimagojr_full_{todaystr}.csv")
with open(os.path.join(basedir, "areas.json"), "r") as f:
    areas = json.load(f)
load_data(areas, res_file_path)
