# SC1015 Mini-Project

## Description

As part of the mini-project for SC1015, our group has decided to explore the dataset of Singapore restaurants found on the website [OpenRice](https://sg.openrice.com/en/singapore), with an eye towards recommending people novel, interesting and enjoyable experiences. 

## Problem Statement & Solution.

The problem statement we came up with is as follows.

> using just our OpenRice data and the restaurant history of a user, how well can we recommend them a restaurant which is going to be an novel and interesting experience for them – that is, in some important way different from their past choices, but in other regards similar enough that they won’t have too much of a “culture shock” and will be able to enjoy themselves?

After our EDA, we decided to use clustering to satisfy the "important way different" criterion, as a clustering algorithm ultimately seeks to find clusters which are in some respect substantially distinct from each other.

Having trained our clustering model and labelled our data, we decided to try the following steps to recommend users restaurants.

1. Take a list of the restaurants a user has already visited.

2. Find a few clusters they are collectively furthest from -- This is the step of finding "novelty" or "important way different".

3. From within those clusters, recommend restaurants  -- This is the "in other regards similar" step.

4. Reduce the importance of further-back history items by application of a scaling factor and put a cap on the length of history considered, as otherwise it would become the case that as their history grows new restaurants a user visits would have a progressively smaller impact on distances and cause a correspondingly small change in recommendations, resulting in staleness.

We simulated 250 users making use of this procedure for recommendation, starting them off with a random restaurant in their history and having them go to restaurants we suggest as we iterated on the simulation. We also devised certain metrics, which showed our model to not be performing that well.

We then identified the issue through comparision with a previous visualisation and reacted by modifying step 2 to simply find random clusters the user has not visited. This consequently improved our metrics substantially.

More elaboration on what we did is in our video.


## Prereqs

You will need to install certain packages. For this, go into Anaconda Navigator and create a new conda environment. Then, through Anaconda  Navigator open a terminal in this conda environment and run the following commands.

1. `conda install geopandas jupyter nb_conda_kernels scikit-learn pandas seaborn matplotlib`.

2. `conda install -c conda-forge LightGBM shap kmodes umap-learn`

In order to start a notebook in this environment, run `conda activate <environment name>` in an Anaconda prompt, then run `python -m notebook`.

Warning: For unknown reasons, on my system, after following this process, the first time the button to rerun all cells from the beginning is pressed will cause Jupyter to have issues and require manual killing and restarting. The button to individually run cells works fine.

## Contents

1. [Web Scraping](http://github.com/adilhasan927/SC1015-Project/Web%20Scraping/Scraping.md)
2. [Produced Dataset](https://github.com/adilhasan927/SC1015-Project/Data/features.csv)
3. [Data Cleaning](https://github.com/adilhasan927/SC1015-Project/blob/main/Datasets/Data%20Cleaning.ipynb)
4. [Exploratory Data Analysis](https://github.com/adilhasan927/SC1015-Project/blob/main/EDA/Exploratory%20Data%20Analysis.ipynb)
5. [Clustering Model](https://github.com/adilhasan927/SC1015-Project/blob/main/Clustering%20Model/Clustering.ipynb)
6. [Model Application](https://github.com/adilhasan927/SC1015-Project/blob/main/Model%20Application/Model%20Application.ipynb)


## Project Flow

- Implemented web-scraping to save web-pages from [OpenRice](https://sg.openrice.com/en/singapore)
- Used Beautiful Soup python library to parse web-pages.
- Performed data cleaning. Dealt with duplicated data and missing data, as well as data encoded in inconvenient forms. Price was transformed from an interval to the midpoint of the interval. Cuisine was transformed from a string of tags seperated by slashes and commas to a) a list of indices into a list of cuisines and b) 52 columns containing either 1 or 0.
- Trained K-Prototypes
- Made use of UMAP visualisation to visualise clusters
- Trained classifier to predict K-Prototypes labels, used classifer to measure cluster distinctiveness and relative importance of features.
- Implemented an attempt at a recommender system
- Simulated useage of recommender system, used visualisation and metrics to identify issue.
- Fixed recommender system and noted improved metrics.
- Project conclusion.

## Learning Outcomes

- Web-scraping and parsing of scraped HTML web-pages
- Useage of an online API to automatically convert street addresses to GPS coords.
- Geographic map visualisation.
- Implementation of K-Prototypes clustering.
- UMAP visualisation.
- Objectively & empirically judging distinctiveness of clusters by training classifier to predict them.
- Useage of SHAP feature importance
- Experience designing and testing an application which makes use of an ML model.
- Practical recommendation to avoid duplication of effort in recommender system, elaborated on at end of video.

## References

- https://pypi.org/project/kmodes/
- https://geopandas.org/en/stable/
- https://lightgbm.readthedocs.io/en/latest/
- https://umap-learn.readthedocs.io/en/latest/
- https://antonsruberts.github.io/kproto-audience/
- https://positionstack.com/
- https://github.com/hartator/wayback-machine-downloader
- https://towardsdatascience.com/the-k-prototype-as-clustering-algorithm-for-mixed-data-type-categorical-and-numerical-fe7c50538ebb
- https://towardsdatascience.com/evaluation-metrics-for-recommender-systems-df56c6611093
- https://medium.com/analytics-vidhya/customer-segmentation-using-k-prototypes-algorithm-in-python-aad4acbaaede
