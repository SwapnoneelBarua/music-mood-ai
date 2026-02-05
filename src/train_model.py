import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from feature_extractor import extract_mfcc

DATASET_PATH = "dataset"

X, y = [], []

for mood in os.listdir(DATASET_PATH):
    mood_path = os.path.join(DATASET_PATH, mood)
    for file in os.listdir(mood_path):
        file_path = os.path.join(mood_path, file)
        features = extract_mfcc(file_path)
        if features is not None:
            X.append(features)
            y.append(mood)

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

joblib.dump(model, "models/mood_model.pkl")
