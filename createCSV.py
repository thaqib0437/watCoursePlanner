import csv
from graphCreation import dictExct 

gc = dictExct('http://www.ucalendar.uwaterloo.ca/2021/COURSE/course-MATH.html')
G = gc.makeGraph()
K = G.keys()
with open('temp.csv','w') as file:
    writer = csv.writer(file)
    for key in K:
        writer.writerow([key,G[key]])
    