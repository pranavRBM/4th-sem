import numpy as np 
import pandas as pd

#Loading Data from a CSV File

file_name='ML/enjoysport.csv'
#Replace with your actual file name 
data=pd.DataFrame(data=pd.read_csv(file_name)) 
print(data)

#Separating concept features from Target 
concepts=np.array(data lloc[:,0:-1]) 
print(concepts)

#Isolating target into a separate DataFrame

#copying last column to target array

target= np.array(data.iloc[:,-1])

print(target)

def learn(concepts, target):
    '''''

    learn() function implements the learning method of the Candidate elimination algorithm.

    Arguments:

        concepts-a data frame with all the features

        target a data frame with corresponding output values
    '''

#Initialise 50 with the first instance from concepts

#copy() makes sure a new list is created instead of just pointing to the same memory location
specific_h=concepts[0].copy()

print("\nInitialization of specific_h and general ")

print(specific_h)

general_h= [["?" for i in range(len(specific_h))] for i in range(len(specific_h ))]
print(general_h)

#The learning iterations

for i, h in enumerate(concepts):

    # Checking if the hypothesis has a positive target

    if target[i] == "Yes":

        for x in range(len(specific_h)):

            #Change values in 5 & G only if values change

            if h[x] != specific_h[x]:

                specific_h[x]='?'

                general_h[x][x] = '?'

    #Checking if the hypothesis has a positive target

    if target[i] = "No":

        for x in range(len(specific_h)]:

            #For negative hyposthesis change values only in G

            if h[x] != specific_hx

                general_h[x][x]=specific_h[x]

            else:

                general_h[x][x]="?"

    print("\nSteps of Candidate Elimination Algorithm",i+1)

    print(specific_h)

    print(general_h)

#find indices where we have empty rows, meaning those that are unchanged

Indices= [i for i, val in enumerate(general_h) if val == [?,?, ?, ?, ?, ?]]

for i in indices:

    #remove those rows from general h

    general h.remove([?,?,?,?,?,?])

    # Return final values

    return specific_h, general_h

s_final, g_final = learn (concepts, target)

print("\nFinal Specific_h:", s_final, sep="\n")

print("\nFinal General_h:", g_final, sep="\n")