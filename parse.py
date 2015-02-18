import csv
import json
courselist = ["English", "Physics", "Chemistry", "Mathematics", "ComputerScience", "Biology", "PhysicalEducation", "Economics", "Accountancy" , "BusinessStudies"]
with open('training.json', 'r') as training:
    for line in enumerate(training):
        if line[0] == 0:
            out=open('train.csv', 'w+')
            print >> out, ",".join(["serial"]+courselist)
            continue
        else:
            pl = json.loads(line[1])
            print >> out, ",".join([str(pl["serial"])]+[ str(pl[course]) if course in pl else "0" for course in courselist])