'''
A program that generates a graph with cliques of different sizes and shapes in a CSV file.
How to run the program: "python3 graph_clique_generator.py method=linear/geometric shape=tree/cyclic"

Author: Sikder Tahsin Al-Amin
Update:  4/8/18 - takes the total number of edges as input.
             16/4/18- changed the generated csv filename

'''
import sys
from random import randint
import pandas as pd
import csv
import string
from sympy import *
import math

sys.argv = ["graph_cluqe_generator.py", "method=linear", "shape=cyclic","total_edge=1000000"]
##checking the arguments
if len(sys.argv) != 4:
    print("Not correct arguments. Call by script_name.py method=linear/geometric shape=tree/cyclic");
    sys.exit()

arg2=sys.argv[1]
arg2=arg2.split('=')
method=arg2[1] ##which method we are generating the cliques, geometric or linear

arg3=sys.argv[2]
arg3=arg3.split('=')
shape=arg3[1] ##shape of the graph: tree or cyclic

arg4=sys.argv[3]
arg4=arg4.split('=')
total_edges=int(arg4[1] )##total edges to be generated
#print(type(total_edges))

list_clique_size=[]  #stores the clique sizes
all_edges=[]    #stores all the edges to print in a csv file
cost=1   #cost of each edge
#total_edges=int(input("Enter total number of edges:"))
#method="linear"  ##which method we are generating the cliques, geometric or linear


#####finding total number of cliques ####
def find_total_clique(total_edges,method):
    total=0
    i=1
    if method=='linear':
        while total<=total_edges:
            total=total+(i*(i-1))+i
            i=i+1
        total_clique=i-1        
    elif method=='geometric':
        while total<=total_edges:
            total=total+((2**i)*((2**i)-1))+i
            i=i+1
        total_clique=i-1
    else:
        print("couldn't compute total cliques")
    return total_clique


#####creating the individual cliques#####
def createClique(total_clique,cost,method):
    i=1
    v=cost
    for j in range(1,total_clique+1,1):
        if method=="geometric":
            clique_size=2**j;
        elif method=="linear":
            clique_size=j
        list_clique_size.append(clique_size)
        print("clique size=",clique_size)
        start=i
        end=i+clique_size-1
        for p in range(start,end+1,1):
            for q in range(p+1,end+1,1):
                #print(p,"->",q)
                #print(q,"->",p)
                list_1=[p,q,v]
                list_2=[q,p,v]
                all_edges.append(list_1)
                all_edges.append(list_2)
        i=end+1

#####connect cliques in a tree shape#####
def MTreeClique(total_clique,cost):
    count_clique=0;
    a=1
    i=0
    j=1
    v=cost
    while count_clique<total_clique:
        i=i+list_clique_size[count_clique]
        j=j+list_clique_size[count_clique]
        #print(i,"->",j)
        list_1=[i,j,v]
        all_edges.append(list_1)
        count_clique=count_clique+1

#####connect cliques in a cycle shape#####
def MCycleClique(total_clique,cost):
    count_clique=0;
    a=1
    i=0
    j=1
    v=cost
    while count_clique<total_clique:
        i=i+list_clique_size[count_clique]
        j=j+list_clique_size[count_clique]
        #print(i,"->",j)
        list_1=[i,j,v]
        all_edges.append(list_1)
        count_clique=count_clique+1
    #print(j,"->","1")
    last_edge=list
    all_edges.append(list([j,1,v]))


total_clique=find_total_clique(total_edges,method) ##finding the total cliques
print("total clique=",total_clique)
print("Create clique...")
createClique(total_clique,cost,method)

if shape=="tree":
    print("Create Treeclique...")
    MTreeClique(total_clique,cost)
elif shape=="cyclic":
    print("Create Cyclecliqe..")
    MCycleClique(total_clique,cost)
else:
    print("Give shape as tree or cyclic")
    
print("Clique Sizes=",list_clique_size)
print("Total edges=",len(all_edges))

####writing to the csv file#####
df=pd.DataFrame(all_edges)
file_name=shape+"clique"+method+str(len(all_edges))+".csv"
print("CSV File Generated= ",file_name)
df.to_csv(file_name,index=False,header=False)
