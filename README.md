Overview

This project applies Natural Language Processing (NLP) and Machine Learning to classify text messages as spam or ham (not spam).
It integrates multiple technologies to demonstrate system design and real-world API communication.

Tech stack:

- Python (FastAPI, scikit-learn, pandas, joblib)

- Java (OkHttp, Gson)

- C++ (libcurl, nlohmann/json)

- HTML, CSS, JavaScript (Frontend)

- GitHub + VS Code + IntelliJ + CLion

  Architecture
     Web UI → FastAPI → ML Model (TF-IDF + Naive Bayes)
     Java Client → FastAPI API
     C++ Client → FastAPI API

  Machine Learning Model

     Algorithm: Multinomial Naive Bayes
     Feature extraction: TF-IDF Vectorizer
     Dataset: SMS Spam Collection Dataset

     Model accuracy: ~95-97% on test data.

Project Structure
spam-classifier/
├── ml-core/
│ ├── train.py
│ ├── api.py
│ ├── spam.csv
│ ├── spam_classifier.pkl
│ └── tfidf_vectorizer.pkl
│
├── web-ui/
│ ├── index.html
│ ├── style.css
│ └── app.js
│
├── java-client/
│ ├── build.gradle
│ └── src/main/java/Main.java
│
└── cpp-client/
├── CMakeLists.txt
└── src/main.cpp

