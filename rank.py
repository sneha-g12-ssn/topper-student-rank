import csv
import sys
from operator import itemgetter

def find_topper(students,mark,i):
  toppers=[]
  for j in range(0,len(students)):
        if students[j][i]==mark:
            toppers.append(students[j][0])
  

  return toppers
  
  
 

file_to_open=sys.argv[1]

with open(file_to_open, 'r') as this_csv_file:
 this_csv_reader = csv.reader(this_csv_file, delimiter=",")
 header = next(this_csv_reader)
 n_subjects=len(header)-1
 #print(n_subjects) 

 students=[]
 total=0
 for line in this_csv_reader: 
  tup=list()
  tup.append(line[0])
  total=0
  for i in range(1,n_subjects+1):
    total+=int(line[i])
    tup.append(int(line[i]))
  tup.append(total)
  students.append(tuple(tup))
 #print(students[0])

 toppers_subjectwise=[]

 for i in range(1,n_subjects+1):
   max_mark=max(students, key = itemgetter(i))[i] 
   topper=find_topper(students,max_mark,i)
   toppers_subjectwise.append(topper)


 class_toppers=sorted(students, key = lambda x: x[7],reverse=True)
 
 
 for i in range(1,n_subjects+1):
   toppers=[a for a in toppers_subjectwise[i-1]]
   print("Topper(s) in ",header[i],"is(are):",end=" ")
   print(*toppers,sep=", ")
 
 print("\nBest students in class are")
 for i in range(0,3):
   print(i+1,":",class_toppers[i][0],"(%d)" %class_toppers[i][7])

print("\nTime complexity of the algorithm is O(m*n)")
print("m-no.of subjects\nn-no. of students")
