# Restaurant Clustering Model

## Description

As part of the mini-project for SC1015, our group has decided to explore the different clusters of restaurant found on the website [OpenRice](https://sg.openrice.com/en/singapore)

## Contents

1. [Data Cleaning](https://github.com/adilhasan927/SC1015-Project/blob/main/Datasets/Data%20Cleaning.ipynb)
2. [Exploratory Data Analysis](https://github.com/adilhasan927/SC1015-Project/blob/main/EDA/Exploratory%20Data%20Analysis.ipynb)
3. [Location EDA](https://github.com/adilhasan927/SC1015-Project/blob/main/EDA/Location%20EDA.ipynb)
4. [Clustering Model](https://github.com/adilhasan927/SC1015-Project/blob/main/Clustering%20Model/Clustering.ipynb)

## Problem

- To identify groups of restaurants that are similar based on variables such as pricing, cuisine and location
- To recommend a suitable restaurant using the clusters generated

## Project Flow

- Implemented web-scrapping to gather data from [OpenRice](https://sg.openrice.com/en/singapore)
- Data consisted of numerical and categorical data types which needed to be cleaned
- Certain categorical data consisted of a few variable which needed to be one-hot encoded
- Performed EDA on each vairables starting from univariate to bivariate analysis
- Location data loaded into a new file to utilise Folium package
- Clustering analysis implemented the K-modes model
- Began with normalising dataset and plotting the elbow curve to find suitable number of clusters
- Utilised the UMAP and Spaghetti to visualise the clusters generated

## Learning Outcomes

- Web-scrapping using API
- Folium package for map visualisation
- Implementation of K-Modes modelling
- UMAP visualisation
- Spaghetti visualisation

## References

- https://pypi.org/project/kmodes/
- https://towardsdatascience.com/the-k-prototype-as-clustering-algorithm-for-mixed-data-type-categorical-and-numerical-fe7c50538ebb
- https://towardsdatascience.com/evaluation-metrics-for-recommender-systems-df56c6611093
- https://medium.com/analytics-vidhya/customer-segmentation-using-k-prototypes-algorithm-in-python-aad4acbaaede
- https://antonsruberts.github.io/kproto-audience/
- https://medium.com/analytics-vidhya/fastest-way-to-install-geopandas-in-jupyter-notebook-on-windows-8f734e11fa2b
- https://medium.com/datasciencearth/map-visualization-with-folium-d1403771717