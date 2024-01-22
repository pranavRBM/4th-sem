import pandas as pd
#Load data

file_name='ML/enjoysport.csv'

data = pd.read_csv(file_name)

#Initialize the hypothesis

hypothesis = ['%' for _ in range(len(data.columns) - 1)]

# Filter positive examples (where PlayGolf is 'Yes')

positive_examples = data[data['EnjoySport']=='Yes'].iloc[:, :-1].values.tolist()

#Apply the FIND-S algorithm

for example in positive_examples:

    for i in range(len(example)):

        if hypothesis[i] != "%"and hypothesis[i] != example[i]:

            hypothesis[i] = "?"

        else:

            hypothesis[i] = example[i]

#Print the maximally specific hypothesis

print("The maximally specific Find-S hypothesis for the given training examples is:")

print(hypothesis)