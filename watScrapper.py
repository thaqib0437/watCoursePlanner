import requests
import re

class WatScrapper(object):
    def __init__(self, url):
        self.url = url
        r  = requests.get(url)
        self.data = r.text

    def getCourses(self):
        courseRe = re.compile('(<a name\s=\s[\w|"]*)')
        allCourses = courseRe.findall(self.data)
        result = []
        for item in allCourses:
            result.append(item[10::])
        return result
    def getPrereqs(self):
        preReqReg = re.compile("(<i>Prereq:[\w|\s|\d|/\n|.|,|&|;|\%]*)")
        preReqs = preReqReg.findall(self.data)
        result = []
        for item in preReqs:
            result.append(item[3:])
        return result

