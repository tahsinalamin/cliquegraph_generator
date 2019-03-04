####A Python Program that generates a tree graph with different edges###
####Sikder Tahsin Al-Amin#####
import pandas as pd
import random

start_vertex=1
end_vertex= input("Enter end vertex = ")
end_vertex=int(end_vertex)
cost=1
number_of_edges=0
tree=[]
i=1
while(i<end_vertex):
   i=i
   j=i+1
   #print(i," ",j)
   random.seed()
   cost=random.randint(1,501)
   list_1=[i,j,cost]
   tree.append(list_1)
   i=i+1
#print(tree)


####writing to the csv file
df=pd.DataFrame(tree)
file_name="tree"+str(end_vertex)+".csv"
print("CSV File Generated= ",file_name)
df.to_csv(file_name,index=False,header=False)

