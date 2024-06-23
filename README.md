# Search-Engine

This repository implements a search engine that utilizes BERT (Bidirectional Encoder Representations from Transformers) for semantic document retrieval.


# Download or clone the repository

To clone the repository, use the following command:

```
git clone https://github.com/hemang2002/Search-Engine.git
```


# Key Features:

1) Semantic Retrieval: Leverages BERT to understand the meaning behind search queries and documents, retrieving results most relevant to the user's intent.
2) Two-Stage Retrieval:
    Retriever pre-filters documents based on keywords.
    Results are then re-ranked based on their semantic similarity to the query using BERT.


# Tech Stack Used

Framework - Flask
Technologies - ![image](https://github.com/hemang2002/WhataApp-Chat-Analysis/assets/66712880/4edb6cc5-4fbd-4c51-81c1-5817ff56ccb4) ![image](https://github.com/hemang2002/WhataApp-Chat-Analysis/assets/66712880/355d0129-e9df-455c-a61e-cd67153503f5)


# Ideal for:

Users seeking a deeper understanding of search topics.
Applications requiring high-precision information retrieval.


# Getting Started:

```
1) pip install virtualenv
```
```
2) cd path/to/save (in this case WhataApp-Chat-Analysis)
```
```
3) virtualenv venv
```
```
4) venv\Scripts\activate
```
```
5) pip install -r requirements.txt
```
```
6) python app.py
```


# Further details:

The repository includes pre-trained BERT models.
Feel free to contribute by adding support for different languages or experimenting with various BERT models.
