
# Veggie Tales

## Overview of the project

### App

We built a Streamlit app structured in three main sections. In the first, the user can upload an image or take a picture of a vegetable that will then be classified according to a list of 16 classes. The second is intended for kids; based on the detected vegetable, openai API creates four facts and a story that are meant for the user to learn about the ingredient. The third is intended for a broader audience. The user gets five specific facts (historical, cultural, health, fun and bad) and a recipe suggestion. 

For details on dependencies and libraries check [requirements.txt](). For getting your own API key for openai, follow [this](https://platform.openai.com/docs/api-reference/authentication) link.

### Image classification model

Classification is performed via the pre-trained deep learning model [InceptionV3](https://www.tensorflow.org/api_docs/python/tf/keras/applications/inception_v3) from Tensorflow. We unfroze the last 15 layers and trained them on 16 classes of the  [dataset](https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition) Fruits and Vegetables Image Recognition from kaggle. For details see the related [notebook]().

Previously, we built up our own deep learning model trained on only two classes. In order to increase the accuracy, we used a different [dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset) with a larger number of training images. For details see the related [notebook]().


### Outlook
* Add text to speech option for listening to the text parts of the app
* Increase the number of classes within the vegetable category and/or other categories (like fruits)
* Add personalized text generation 

### Resources


* [Tutorial on InceptionV3](https://github.com/akbarhuseynov23/Dog-Breed-Identification---ML-final-project/blob/main/dog-breed-identification-final%20(1).ipynb)
* [Streamlit multi-page app tutorial](https://medium.com/codex/create-a-multi-page-app-with-the-new-streamlit-option-menu-component-3e3edaf7e7ad)
* [Deep learning tutorial](https://www.youtube.com/playlist?list=PLeo1K3hjS3uu7CxAacxVndI4bE_o3BDtO)
* [CNN classifier tutorial](https://www.tensorflow.org/tutorials/images/classification)



### The authors

Almuth Hattwich: [GitHub](https://github.com/0x6168) | [LinkedIn](https://www.linkedin.com/in/almuth-hattwich/)


Gian Andrea Inkof: [GitHub](https://github.com/ginkof) | [LinkedIn](https://www.linkedin.com/in/inkof/)
