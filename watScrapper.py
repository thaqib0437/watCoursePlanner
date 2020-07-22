import requests
import re

class scrapper(object):
    def __init__(self, url):
        self.url = url
        r  = requests.get(url)
        self.data = r.text

    def getCourses(self, text):
        courseRe = re.compile('(<a name=[\w|"]*)')
        allCourses = courseRe.findall(text)
        result = []
        for item in allCourses:
            result.append(item[9:])
        return result
    def getPrereqs(self, text):
        preReqReg = re.compile("(<i>[/\n|\s]*Prereq:[\w|\s|\d|/\n|.|,|&|;|\%|\(|\)]*)")
        preReqs = preReqReg.findall(text)
        result = []
        for item in preReqs:
            result.append(item[3:])
        return result

        
    def getAllText(self):
        return self.data