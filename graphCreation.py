import watScrapper
from bs4 import BeautifulSoup


ws = watScrapper.scrapper('http://www.ucalendar.uwaterloo.ca/2021/COURSE/course-CS.html')

site = ws.getAllText()
soup = BeautifulSoup(site, 'html.parser')

contentTable  = soup.find_all('center') 
# c = contentTable.prettify()
# L = ws.getPrereqs(c)
# print(L)
courseGraph = dict()
for course in contentTable:
    txtForm = course.prettify()
    crc = ws.getCourses(txtForm)
    crc[0] = crc[0].replace('"','')
    preReq = ws.getPrereqs(txtForm)
    courseGraph[crc[0]] = preReq

print(courseGraph)