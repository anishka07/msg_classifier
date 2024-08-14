# SMS Spam Detection

## Overview

This project focuses on detecting spam messages using machine learning. It emphasizes on Exploratory Data Analysis (EDA) to enhance model performance.

## Project Structure

```plaintext
.
├── README.md
├── data/
│   ├── new_spam.csv
│   └── spam.csv
├── notebooks/
│   ├── eda_msg_spam.ipynb
│   ├── lstm_model_building.ipynb
│   └── model_building.ipynb
├── pkls/
│   ├── model.pkl
│   ├── modelv1.pkl
│   ├── vec.pkl
│   └── vectorizerv1.pkl
├── requirements.txt
├── scripts/
│   ├── __init__.py
│   └── app.py
└── settings.py
```


## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/anishka07/msg_classifier.git
cd msg_classifier
pip install -r requirements.txt
```


## EDA
Explore the notebooks/eda_msg_spam.ipynb for data exploration and analysis.

## Useage
Run the Streamlit app to classify SMS messages:
```bash
streamlit run src/app.py
```

## Future Work
- Model Improvement 
- Model Deployment