import csv
import pandas as pd
import random

n=int(input("Enter number of vertices:"))
v=1 #cost
data_list=[]


with open('complete.csv','w') as myfile:
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            if i!=j:
                random.seed()
                v = random.randint(1,501)
                data=[]
                data.append(i)
                data.append(j)
                data.append(v)
                #data_list=[]
                data_list.append(data)
                #print(data_list)
                #writer=csv.writer(myfile,delimiter =',')
                #writer.writerows(data_list)

    
myfile.close()  
print("Total edges=",len(data_list))                
####writing to the csv file
df=pd.DataFrame(data_list)
file_name="complete"+str(len(data_list))+".csv"
print("CSV File Generated= ",file_name)
df.to_csv(file_name,index=False,header=False)
