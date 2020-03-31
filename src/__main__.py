import os
import datetime
import argparse
import json

from scimagojr.scraping import load_data

todaystr = datetime.date.today().isoformat()


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--dir",
        help="base directory to store csv files",
        default=todaystr,
        type=str,
    )

    parser.add_argument(
        "-a", "--areas", help="areas json file", default="areas.json", type=str,
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = arg_parse()
    res_file_path = os.path.join(args.dir, f"scimagojr_full_{todaystr}.csv")
    with open(args.areas, "r") as f:
        areas = json.load(f)
    load_data(areas, res_file_path)
