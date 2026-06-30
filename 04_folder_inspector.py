"""
Project: Folder Inspector
Rating: 9.5/10
Concepts: os.listdir + os.path.getsize + os.path.splitext + JSON reporting
"""

import json
import os
import pyinputplus as co
from pathlib import Path as path


def inspector():
    folder_name = co.inputStr("Enter the folders names you wants to find out")
    folder = path(f"G:/python_code/automate_boring_stuff_with_python/{folder_name}")

    if folder.exists():
        data = os.listdir(folder)
        py, txt, png, total, total_size = 0, 0, 0, 0, 0

        for item in data:
            file = os.path.join(folder, item)
            if os.path.isfile(file):
                total += 1
                name = item
                suffix = os.path.splitext(item)[1].lower()
                if suffix == ".py":
                    py += 1
                elif suffix == ".txt":
                    txt += 1
                elif suffix == ".png":
                    png += 1
                size = os.path.getsize(file) / 1024
                total_size += size
                print(f"name : {name} type :{suffix} size : {size:.2f} KB")

        final_data = (f"total files: {total}\n py : {py} \n txt {txt} \n png {png} \n total size: {total_size:.2f} KB")
        print(final_data)

        try:
            with open("report.txt", "r") as f:
                data = json.load(f)
        except:
            data = {}

        data[folder_name] = [final_data]
        with open("report.txt", "w") as f:
            json.dump(data, f, indent=4)
    else:
        print("no such folder exists please try again later ")


if __name__ == '__main__':
    inspector()
