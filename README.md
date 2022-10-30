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
paper recommendations to help them find papers that they would be
interested in and also to group the papers into categories so they
can be looked up more easily.

## <a name="link-part-2">Design</a>



## <a name="link-part-3">Data</a>



## <a name="link-part-4">Algorithm</a>

**Data Cleaning:**



**Feature Engineering:**


**Models:**



**Model Evaluation and Selection:**


**Final scores:**



## <a name="link-part-5">Tools</a>

* **Pandas** for exploratory data analysis.
* **Matplotlib** and **Seaborn** for plotting.
* **Scikit Learn** for modeling and natural language process.
* **Pickle** for saving models in a pickle file.

## <a name="link-part-6">Communication</a>

The project proposal is shown [here](/documents/proposal.md).

The MVP document is shown [here](/documents/MVP.md).

## <a name="link-part-7">How to run</a>

cd into [recommender](/recommender):
```
cd recommender
```

Run the recommender by:
```
python3 recommender.py $(paper_index)
```

For example:
```
python3 recommender.py 3
```

## <a name="link-part-8">Reference</a>
- [1]: [Cornell University, Joe T., Devrishi, & Brian M. ArXiv Dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv)
