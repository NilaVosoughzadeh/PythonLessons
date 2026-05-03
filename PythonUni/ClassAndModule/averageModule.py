import averageClass as AC

lesson1 = int(input("Plz enter lesson 1 score : "))
lesson2 = int(input("Plz enter lesson 2 score : "))
lesson3 = int(input("Plz enter lesson 3 score : "))

avgClassImport = AC.AverageClass()
avgDef = avgClassImport.AverageMath(lesson1, lesson2, lesson3)
print(avgDef)