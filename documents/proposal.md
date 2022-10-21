# Project Proposal

## Question/Need:

There are a lot of scientific papers online with different topics.
Clustering papers that shares similar topics can provide researchers
paper recommendations to help them find papers that they would be
interested in and also to group the papers into categories so they
can be looked up more easily.

## Data Description:
The data comes from [arXiv Dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv).

It contains data for 2,142,715 scientific papers including authors,
title, doi, categories, abstract, etc. I have filtered the dataset
into a smaller one that only contains 379,985 papers that the last
version was published after 2020.

## Tools:

* **Pandas** for exploratory data analysis.
* **Matplotlib** and **Seaborn** for plotting.
* **Scikit Learn** and **Gensim** for modeling and natural language process.
* **Pickle** for saving models in a pickle file.


## MVP Goal:
My MVP goal is to analyze the data to build some virtualizations and a base
model.
