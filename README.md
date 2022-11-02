# Scientific Paper Clustering

## Table of Contents
- [Abstract](#link-part-1)
- [Design](#link-part-2)
- [Data](#link-part-3)
- [Algorithm](#link-part-4)
- [Tools](#link-part-5)
- [Communication](#link-part-6)
- [**How to run**](#link-part-7)
- [Reference](#link-part-8)

## <a name="link-part-1">Abstract</a>

There are a lot of scientific papers online with different topics.
Clustering papers that shares similar topics can provide researchers
paper recommendations to help them recommend papers that they would be
interested in and also to group the papers into categories so they
can be looked up more easily.

## <a name="link-part-2">Design</a>

This project originates from the [arXiv Dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv). Clustering scientific
papers would enable scientific paper recommendation function to help
researchers find papers that are similar to their research interests,
or papers that are not in their research interests but they might be
interested in. Looking for and reading papers can cost lots of time and
this recommendation system can definately save time for researchers.

## <a name="link-part-3">Data</a>

The data comes from [arXiv Dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv).

It contains data for 2,142,715 scientific papers including authors,
title, doi, categories, abstract, etc. I have filtered the dataset
into a smaller one that only contains 379,985 papers that the last
version was published after 2020, and then sampled 50,000 rows from
the filtered dataset for clustering.

## <a name="link-part-4">Algorithm</a>

**Data Cleaning:**

- Convert the original JSON file into a dataframe.
- Only select papers which the latest versions are released after 2020.
- Drop duplicate rows.
- Randomly ample 50,000 rows from the filtered dataframe.
- Get rid of all the '\n' characters in their abstracts.
- Get stop words from package spacy.lang.en.stop_words and add customized
stop words.
- Get punctuations from package string.punctuations.
- Use package en_core_sci_lg from spacy for lemmatization and filter all
stop words and punctuations.

**Word to Vector:**

- Use TfidfVectorizer to turn abstracts into vectors. (min_df=0.016, max_df
=0.05)

**Topic Modeling:**

Use LSA to turn the words into 20 topics.

Some topic examples:
- 2d, background, detector, imaging, light, reconstruction, resolution,
sensitivity, sensor, ...
- answer, gravitational, language, natural, production, question, resource,
scalar, search, social, ...
- channel, link, metric, platform, software, technology, user, ...

**Models:**

- **DBSCAN model**:

- - Epsilon: 0.15

- - min_samples: 5

- - Final clusters:

<img src="/imgs/DBSCAN.png" style="width: 400px;" />

- **K-means model**:

- - Selecting number of clusters:

<img src="/imgs/selecting_clusters.png" style="width: 400px;" />

- - Final number of clusters: 14

- - Final clusters:

<img src="/imgs/KMeans.png" style="width: 400px;" />


**Model Evaluation and Selection:**

K-means model's clustering makes more sense and is better at clustering datasets
like this. Many of the papers with in a same cluster are in the same category and
show big similarity. Here are some examples:

Paper "Fast and Reliable Probabilistic Face Embeddings in the Wild", "Event and
Activity Recognition in Video Surveillance for Cyber-Physical Systems", and "
Transfer Learning from an Artificial Radiograph-landmark Dataset for Registration
of the Anatomic Skull Model to Dual Fluoroscopic X-ray Images" are in cs.CV category
and are pretty similar.


## <a name="link-part-5">Tools</a>

* **Pandas** for exploratory data analysis.
* **Matplotlib** and **Seaborn** for plotting.
* **Scikit Learn** and **spaCy** for modeling and natural language process.
* **Pickle** for saving models in a pickle file.

## <a name="link-part-6">Communication</a>

For the paper **"On Whitehead's cut vertex lemma"** written by Rylee Alanza and Lyman, the
recommender recommends the following papers from the same cluster:

- **"Local rainbow colorings for various graphs"**
- **"Even vertex $\zeta$-graceful labeling on Rough Graph"**
- **"Revisiting and improving upper bounds for identifying codes"** 

And paper from different clusters:

- **"Numerical Solution of the 3-D Travel Time Tomography Problem"**
- **"On irreducible representations of a class of quantum spheres"**

<img src="/imgs/Recommender.png" style="width: 600px;" />

The project proposal is shown [here](/documents/proposal.md).

The MVP document is shown [here](/documents/MVP.md).

The slides are shown [here](/documents/slides.pdf).

## <a name="link-part-7">How to run</a>

cd into [/recommender](/recommender):
```
cd recommender
```

Run the recommender by:
```
python3 recommender.py $(paper_id)
```

For example:
```
python3 recommender.py 2205.06071
```

## <a name="link-part-8">Reference</a>
- [1]: [Cornell University, Joe T., Devrishi, & Brian M. ArXiv Dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv)
