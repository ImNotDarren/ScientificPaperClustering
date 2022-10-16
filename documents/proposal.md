# Project Proposal

## Question/Need:

Electronic Health Record (EHR) data carries enormous amounts of medical
treatment information that is not well structured, stored instead as free
text. This data has great potential to provide insight into medical
treatment and to facilitate retrospective studies. This project aims to
proceed natural language processing to analyze these data and use it to
prodict stroke scale score.

## Data Description:
The data comes from [National Institutes of Health Stroke Scale (NIHSS) Annotations for the MIMIC-III Database](https://doi.org/10.13026/gyjg-0t90)

It contains data for 312 stroke patients with 2929 NIHSS items, 2774
measurements, and 2733 item-score relations. There are 7848 free text
sentences in this dataset.

## Tools:

* **Pandas** for exploratory data analysis.
* **Matplotlib** and **Seaborn** for plotting.
* **Scikit Learn** and **Gensim** for modeling and natural language process.
* **Pickle** for saving models in a pickle file.


## MVP Goal:
My MVP goal is to analyze the data to build some virtualizations and a base
model.

