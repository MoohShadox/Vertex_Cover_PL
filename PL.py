from pulp import *
import os
f=open(r"graph_file","r")
L=f.readlines()
nodes=[]
edges=[]
for i in L:
    E=i.strip().split(" ")
    print("E=",E)
    if len(E) == 1:
        nodes.append(E[0])
    else:
        edges.append(tuple(E))
print("nodes",nodes)
print("edges",edges)
incidence = {}



for k in edges:
    if (k[0] in incidence.keys()):
        incidence[k[0]].append(k[1])
    else:
        incidence[k[0]]=[]
        incidence[k[0]].append(k[1])

    if (k[1] in incidence.keys()):
        incidence[k[1]].append(k[0])
    else:
        incidence[k[1]]=[]
        incidence[k[1]].append(k[0])

print(incidence)
prob= LpProblem("Minimum_Vertex_Cover_Problem", LpMinimize)
nodes=LpVariable.dicts("Choice",nodes, cat="Binary")
print(nodes)
prob += lpSum([nodes[n]for n in nodes])
for e in edges:
    prob += nodes[e[1]] + nodes[e[0]]>= 1
prob.solve()    
print(prob.status)
for v in prob.variables():
    print(v.name, "=", v.varValue)