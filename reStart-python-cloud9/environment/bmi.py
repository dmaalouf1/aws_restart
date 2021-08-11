# with no header
def calulate_BMI(height,weight):
    BMI = weight/(height*height)
    return BMI
    
import csv

lineCount = 0
with open('a.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            Name = row[0]
            height = row[1]
            weight = row[2]
            print("\nHi ",Name)
            print(float(height))
            print(float(weight))
            BMI = calulate_BMI(float(height),float(weight))
            print(BMI)
            if BMI > 30 :
                print("you are obese.")
            elif BMI > 25 and BMI < 30:
                print("you are overweight.")
            elif BMI > 18.5 and BMI <24.9:
                print(" you have a healthy weight range for young and middle-aged adults.")
            else:
                print("you are very underweight and possibly malnourished.")