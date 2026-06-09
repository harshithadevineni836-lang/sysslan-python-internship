import os

files = ["report.pdf", "photo.jpg", "notes.txt"]

for file in files:
    extension = file.split(".")[-1]
    print(f"{file} -> {extension} folder")