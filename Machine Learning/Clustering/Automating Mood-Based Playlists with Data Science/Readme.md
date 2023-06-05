# Automating Mood-Based Playlists with Data Science

This repository contains code and associated files for creating an algoritm to cluster songs defined by Spotify Features.

Project Overview

In this project, we build an automated playlist creation system for Moosic, a startup specializing in curated playlists. The goal is to utilize data science techniques by leveraging a dataset of Spotify's audio features. Using the K-Means clustering algorithm, we aim to divide the songs into clusters that represent different playlists. The main objectives are to assess the ability of Spotify's audio features in identifying similar songs based on humanly detectable criteria and to evaluate the effectiveness of K-Means for playlist creation. Ultimately, we will present the generated clusters to the team and engage in discussions to shape the future direction of the project.

This project is broken down into two main notebooks:

**Notebook 1: 1.audio_features_analysis**

* Perform unsupervised machine learning analysis on a dataset of audio features of songs ([data](https://github.com/ginkof/Data-Science-Portfolio/tree/main/Machine%20Learning/Clustering/Automating%20Mood-Based%20Playlists%20with%20Data%20Science/Data) and [feature description](https://round-caution-74a.notion.site/Feature-description-743db18aa7324597a2648cbc25dce632?pvs=4))
* Scale data and calculate pairwise distances between the scaled features.
* Explore correlations between features and plots pairs of features with strong correlation.
* Apply Principal Component Analysis (PCA) on selected features, determines the optimal number of clusters using elbow and silhouette methods, performs K-means clustering, and visualizes the clusters using treemaps and heatmaps.

**Notebook 2: 2.creating_spotify_playlists**

* Import the required libraries and load the songs data from a CSV file into a DataFrame.
* Configure authentication and initialize the Spotify API object.
* Create playlists for each cluster:
  * Filter the songs DataFrame for each cluster.
  * Generate a unique playlist name and create a public playlist using the Spotify API.
  * Search for each song in the cluster using the Spotify API and add the found track IDs to the playlist.
* Repeat step 3 for all clusters.

All the results are summarized in the [presentation](https://github.com/ginkof/Data-Science-Portfolio/blob/main/Machine%20Learning/Clustering/Automating%20Mood-Based%20Playlists%20with%20Data%20Science/Results.pptx) (Use of PPT recommended to enjoy visualization).
