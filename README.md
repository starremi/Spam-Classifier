# Spam Email / SMS Classifier

A full-stack machine learning project that detects **spam messages** using:

- Python (FastAPI backend + ML model)
- Java client
- C++ client
- Web UI (HTML/CSS/JS)

This project demonstrates an end-to-end system integrating Machine Learning, API communication, and multi-language clients.

---

## Overview

This project applies Natural Language Processing (NLP) and Machine Learning to classify text messages as **spam** or **ham** (not spam).  
It demonstrates full-stack concepts:

- Model training and evaluation  
- Serving predictions through a FastAPI REST API  
- Consuming that API using Java + C++ clients  
- Interactive web-based frontend  

---

## Tech Stack

- **Python** — FastAPI, scikit-learn, pandas, joblib  
- **Java** — OkHttp, Gson  
- **C++** — libcurl, nlohmann/json  
- **Frontend** — HTML, CSS, JavaScript  
- **Tools** — GitHub, VS Code, IntelliJ, CLion  

---

## Architecture
- Web UI → FastAPI → ML Model (TF-IDF + Naive Bayes)  
- Java Client → FastAPI API  
- C++ Client → FastAPI API

## Machine Learning Model

- **Algorithm:** Multinomial Naive Bayes  
- **Feature Extraction:** TF-IDF Vectorizer  
- **Dataset:** SMS Spam Collection Dataset  
- **Accuracy:** ~95–97% on test data  


---

## Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/spam-classifier.git
cd spam-classifier



