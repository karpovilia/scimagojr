import pandas as pd
import requests
import os
from io import StringIO


def load_data(areas: dict, res_file_path: str):
    frames = list()
    try:
        for area, code in areas.items():
            url = f"https://www.scimagojr.com/journalrank.php?category={code}^&out=xls"
            response = requests.request("GET", url)
            content = response.content.decode("utf8")
            TESTDATA = StringIO(content)
            df = pd.read_table(TESTDATA, sep=";")
            df["Area"] = area
            frames.append(df)
        result = pd.concat(frames)
    except Exception as ex:
        print(ex)

    try:
        result.to_csv(res_file_path, sep=";")
    except OSError:
        pass
