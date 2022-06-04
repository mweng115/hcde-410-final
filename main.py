# import relevant python libraries
import pandas as pd
import matplotlib.pyplot as plt

# read in data
covid_data = pd.read_excel(r"covid_misinfo.xlsx")

# change excel file to csv
covid_data.to_csv("covid_misinfo.csv", index=None, header=True)
df = pd.DataFrame(pd.read_csv("covid_misinfo.csv"))
# print(df.keys())

# exclude columns not necessary for analysis, keeping only: main narrative, motive, country, publication date
analysis_data = df[['Publication_Date', 'Primary_Country', 'Main_Narrative', 'Motive']]
# print(analysis_data)

# keep only stories from the United States
us_data = analysis_data[analysis_data['Primary_Country'] == 'United States']

# find the most popular main narrative and motive for the disinformation stories in the dataset
print(us_data['Main_Narrative'].describe())
print(us_data['Motive'].describe())

# graph references
New_Colors = ['green','blue','purple','brown','teal']

# create a graph of the count of each main narrative
narratives = pd.unique(us_data['Main_Narrative'])
narrative_dict = {}
for value in narratives:
    narrative_dict[value] = 0

for row in us_data['Main_Narrative']:
    narrative_dict[row] = narrative_dict[row] + 1

narratives = [narrative.replace(' ', '\n') for narrative in narratives]
plt.bar(narratives, list(narrative_dict.values()), color=New_Colors)
plt.title('Main Narratives in Disinformation Stories by Count', fontsize=14)
plt.xlabel('Main Narrative', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.show()

# create a graph of the count of each motive
motives = pd.unique(us_data['Motive'])
motive_dict = {}

for value in motives:
    motive_dict[value]=0

for row in us_data['Motive']:
    motive_dict[row]=motive_dict[row]+1

motives = [motive.replace(' ', '\n') for motive in motives]
plt.bar(motives, list(motive_dict.values()), color=New_Colors)
plt.title('Motives in Disinformation Stories by Count', fontsize=14)
plt.xlabel('Motives', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.show()