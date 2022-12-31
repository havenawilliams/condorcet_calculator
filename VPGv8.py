import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import argparse
import os

'''
Hello!

This is my condorcet winner calculator. You can use this script to:

1. Import data on voters' ordinal preferences on candidates.
2. Print a directed graph showing all of the pairwise victories of different policies.
3. You can find the condorcet winner by finding the terminal node.
4. Note that you have to pay attention to look for weak condorcet winners.

I need to work adding argparser to this script, but that's ok!

Also on my to do list is to generate an object that contains the condorcet winner,
as well as any other weak condorcet winners in my script.

Thanks!
'''

#Clear plot from pervious run
plt.cla()

#Instantiate argparser arguments
parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
args = parser.parse_args()

#DEPRECIATED
#Current directory, need to reconfigure this using argparse later
os.chdir("G:\My Drive\R\ON Research Projects\Voting Paradoxes\Cuban Missile Crisis")

#Import the data
df = pd.read_csv(args.inputfile)

#Get all unique candidate names
candidate_names = sorted(np.unique(df.iloc[:,1:].values.tolist()))

#This drops 'nan' values
#The try/except is needed in case there are no nan values to remove
try:
    candidate_names.remove('nan')
except ValueError:
    pass

#Create a dataframe to load in results
electoral_results = pd.DataFrame(columns = candidate_names, index = candidate_names)

for col in electoral_results.columns:
    electoral_results[col].values[:] = 0

#Iterate over the set of votes and make a matrix of victories
votes_from_voters = np.array(df.iloc[:,1:5])

#Adding into our array the number of victories one policy has over another
#A victory is whenever one policy if preferred more than another
for vote_vector in votes_from_voters:
    for i in vote_vector:
        for j in vote_vector:
            if i == j:
                pass
            else:
                if np.where(vote_vector == i) < np.where(vote_vector == j):
                    electoral_results.loc[[i], [j]] += 1

#I'll explain this step
#The changes to the dataframe we've made already involve a,b victories but also b,a victories
#But in a condorcet election, we're interested in the net victories that one option has over another
#So here's I'm subtracting the upper triangular results from the lower so the net number of victories
#is only in the lower half.
winners_array = np.tril(electoral_results) - np.tril(electoral_results.T)
winners_dataframe = pd.DataFrame(winners_array, columns = candidate_names, index = candidate_names)

#Gathering index for only lower diagonal entries (non-zero entries)
#These indexes will tell us where to look for nodes in our directed graph
#Without this we would scan the entire dataset, when we only need the lower triangular
low_diagonal_entries = []
for i in range(len(winners_dataframe)):
    for j in range(len(winners_dataframe)):
        if i > j:
            low_diagonal_entries += [(i, j)]

#Instantiating directed graph object
Graph_Output = nx.DiGraph()

#Gathering the edge names and their weights
for i in range(len(low_diagonal_entries)):
    if winners_dataframe.iat[low_diagonal_entries[i][0],low_diagonal_entries[i][1]] < 0:
        Graph_Output.add_edges_from([(winners_dataframe.columns[low_diagonal_entries[i][0]], 
        winners_dataframe.index[low_diagonal_entries[i][1]])],
        label = abs(winners_dataframe.iat[low_diagonal_entries[i][0], low_diagonal_entries[i][1]]))
    else:
        Graph_Output.add_edges_from([(winners_dataframe.columns[low_diagonal_entries[i][1]], 
        winners_dataframe.index[low_diagonal_entries[i][0]])],
        label = winners_dataframe.iat[low_diagonal_entries[i][0], low_diagonal_entries[i][1]])


#Positions, networkx requirement
pos = nx.spring_layout(Graph_Output)

#Edge labels, networkx requirement, straight from example code
edge_labels=dict([((u,v,),d['label'])
                 for u,v,d in Graph_Output.edges(data=True)])

'''
The code below draws and plots the graph object
'''

#Gather labels
node_labels = {node:node for node in Graph_Output.nodes()}; nx.draw_networkx_labels(G = Graph_Output, pos = pos, labels = node_labels) #straight from example code

#Apply labels
nx.draw_networkx_edge_labels(G = Graph_Output, 
                            pos = pos, 
                            edge_labels = edge_labels,
                            rotate = False,
                            font_size = 20)

#Draw actual graph
nx.draw(G = Graph_Output, 
        pos = pos, 
        node_size = 2000)

#Plots the graph
plt.show()