"""
Project: Personal Diary App
Rating: 7.5/10
Concepts: PyInputPlus (inputDate, inputStr, inputMenu) + File I/O + Pathlib


import pyinputplus as co
from pathlib import Path

folder = Path(__file__).parent

def diary_write():
    date = co.inputDate("Enter today's date: ")
    entry = co.inputStr("Enter your diary entry: ", blank=False)
    filepath = folder / f"{date}.txt"
    with open(filepath, 'a') as f:
        f.write(entry + '\n')
    print("Entry added! ✅")

def diary_read():
    date = co.inputDate("Enter the date to read: ")
    filepath = folder / f"{date}.txt"
    if filepath.exists():
        print(filepath.read_text())
    else:
        print(f"No diary entry found for {date}! ❌")

if __name__ == '__main__':
    menu = co.inputMenu(["Enter an entry", "Read an entry"])
    if menu == "Enter an entry":
        diary_write()
    elif menu == "Read an entry":
        diary_read()
