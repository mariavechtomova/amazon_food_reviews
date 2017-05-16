# CNN text classification on Amazon reviews

Purpose of this project is to understand how CNN can be applied for different text classification problems:

- basic binary classification problem (review sentiment)
- multiclass classification problem (review category classification)
- hierarchical classification problem (predicting category and subcategory of the review)

## Code

- `1. Get data`. Automatically downloads, transforms the data and saves the result as csv.
- `2. Data preparation`. Prepares the dataset for modelling and saves the result as a pickle.
- `3a. Sentiment base model`. Implement a baseline model (Random Forest with TF-IDF features) to predict the review sentiment based on the review text. 
- `3b. Sentiment CNN`. Implement a CNN to predict the review sentiment based on the review text.
- `4a. Category1 base model`. Implement a baseline model (Random Forest with TF-IDF features) to predict the first level category of the product in the review.
- `4b. Category1 CNN model`. Implement a CNN to predict the first level category of the product in the review.
- `5a. Category2 base model`. Implement a baseline model (Random Forest with TF-IDF features) to predict the second level category of the product in the review.
- `5b. Category2 CNN model simple`. Implement a simple CNN to predict the second level category of the product in the review.
- `5c. Category2 CNN model advanced`. Implement an advanced CNN to predict the second level category of the product in the review.

Helper functions can be found in `helpers.py` file.

## Folders

If you want to be able to run all the scripts without errors, your `amazon_food_reviews` folder should include the following folders:
- data (not included in the git repository)
- ipynb
- models (not included in the git repository)
- tensorflow_logs (not included in the git repository)

## Dataset

From https://archive.org/download/amazon-reviews-1995-2013 the following is downloaded:
- gourmet foods
- pet supplies
- toys & games
- beauty
- health
- baby
- metadata

## Install

This project requires **Python 3.5** and packages listed in requirements.txt (correct package versions are **very** important)

## Literature/ inspirations

Literature on CNNs for NLP tasks:

1) http://www.wildml.com/2015/11/understanding-convolutional-neural-networks-for-nlp/

2) https://arxiv.org/pdf/1404.2188.pdf

3) https://arxiv.org/pdf/1408.5882.pdf

4) http://cs224d.stanford.edu/reports/RhodesDylan.pdf

5) http://cs224d.stanford.edu/reports/DufourNick.pdf


Word2vec explained:
- http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/
- http://stats.stackexchange.com/questions/244616/how-sampling-works-in-word2vec-can-someone-please-make-me-understand-nce-and-ne/245452#245452

How to use tensorboard:
- http://ischlag.github.io/2016/06/04/how-to-use-tensorboard/

Inspired by:
- http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/
- https://agarnitin86.github.io/blog/2016/12/23/text-classification-cnn