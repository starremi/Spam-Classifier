# ----------------------------------------------------------
# train.py — Trains the Spam Email Classifier
# ----------------------------------------------------------

# 1️⃣ Import libraries
import pandas as pd                       # python library for tabular data (spreadsheet)
from sklearn.model_selection import train_test_split #Helps split data into training and testing sets 
from sklearn.feature_extraction.text import TfidfVectorizer #Turns text into numbers based on how important each word is in each message
from sklearn.naive_bayes import MultinomialNB #Algorithm for spam detection and other text classifiations tasks
from sklearn.metrics import accuracy_score, classification_report #Evaluate model performance : predictions, precision, recall, and F1 score
import joblib                             # Library to save and load models to file

# 2️⃣ Load dataset (CSV downloaded from Kaggle)
print("Loading dataset")
df = pd.read_csv("spam.csv", encoding="latin-1")[["v1", "v2"]] # (1) encoding="latin-1" ensures it can handle special characters in the file. 
#(2) [["v1", "v2"]] selects only the two relevant columns from the dataset.
df.columns = ["label", "message"]          # rename for clarity : v1 - label (spam), v2 - message (text of the SMS/email)
print(df.head()) # Prints first 5 rows to confirm it loaded correctly

# 3️⃣ Converts the text labels into numbers 
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# 4️⃣ Split into training and testing sets
# (1) 80% training and 20% testing of the data (2) Random_state=42 ensures the split is reproducible every time you run it.
X_train, X_test, y_train, y_test = train_test_split(
    df["message"], df["label"], test_size=0.2, random_state=42
)

# 5️⃣ Convert text → numeric TF-IDF vectors
# Creates a TF-IDF vectorizer that: (1) Removes common English words (stop_words="english") & (2) Keeps the 3,000 most frequent words
vectorizer = TfidfVectorizer(stop_words="english", max_features=3000)
# 
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf  = vectorizer.transform(X_test)

# 6️⃣ Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# 7️⃣ Evaluate accuracy 
y_pred = model.predict(X_test_tfidf) # Uses the trained model to predict whether each message in the test set is spam or not
# Accuracy and detailed report
print("\n✅ Model performance:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=["ham","spam"]))

# 8️⃣ Save model + vectorizer for later use
joblib.dump(model, "spam_classifier.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
print("Saved model and vectorizer successfully!")
