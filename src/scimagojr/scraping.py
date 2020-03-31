import pandas as pd
import requests
import os
import traceback
from io import StringIO


def load_data(areas: dict, res_file_path: str):
    frames = list()
    try:
        for area, code in areas.items():
            response = requests.get(
                f"https://www.scimagojr.com/journalrank.php?category={code}^&out=xls"
            )
            content = response.content.decode("utf8")
            TESTDATA = StringIO(content)
            df = pd.read_table(TESTDATA, sep=";")
            df["Area"] = area
            frames.append(df)
        result = pd.concat(frames)
    except Exception as ex:
        traceback.print_tb(ex.__traceback__)

    try:
        result.to_csv(res_file_path, sep=";")
    except OSError as ex:
        traceback.print_tb(ex.__traceback__)
