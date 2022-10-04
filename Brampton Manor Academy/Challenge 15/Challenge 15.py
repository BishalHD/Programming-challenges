from operator import index
import csv 
from pathlib import Path 

def read_html(path):
    with open (path, 'r') as file:
        html_file = file.read()
        return html_file


def read_csv(csv_path):
    csv_contents = []
    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)
        for row in reader:
            csv_contents.append(row)
    return csv_contents

def process(csv, html):
    indexNameList = [[0,'link'], [1,'initials'], [2,'name']]
    for currentItem in indexNameList:
        for x in range (5):
            Name = currentItem[1] + str(x+1)
            html = html.replace (Name,csv[x][currentItem[0]])
    return html

def write_html(path, html):
    with open (path,'w') as htmlfile:
        htmlfile.write(html)


if __name__ == "__main__":
    csv = read_csv(csv_path='south.csv')
    html = read_html(path='south.html')
    html = process(csv, html)
    write_html(path="south_final.html", html=html)
