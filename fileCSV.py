import csv
from statistics import mean
with open('N:\\grades.csv') as fileCSV :
    reader = csv.reader(fileCSV)
    for row in reader :
        #print row
        name = row[0]
        theseGrades = list()
        for grade in row[1:] :
            theseGrades.append(int(grade))
            #print(name, grade, theseGrades)
        print("Average of %s is %f" %(name, mean(theseGrades)))