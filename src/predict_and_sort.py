import os
import shutil
import pandas as pd
import joblib
from feature_extractor import extract_mfcc

INPUT_FOLDER = "input_songs"
SORTED_FOLDER = "sorted_songs"
MODEL_PATH = "models/mood_model.pkl"

model = joblib.load(MODEL_PATH)

results = []

for file in os.listdir(INPUT_FOLDER):
    file_path = os.path.join(INPUT_FOLDER, file)
    features = extract_mfcc(file_path)

    if features is None:
        continue

    prediction = model.predict([features])[0]
    confidence = max(model.predict_proba([features])[0])

    dest_folder = os.path.join(SORTED_FOLDER, prediction)
    os.makedirs(dest_folder, exist_ok=True)

    shutil.move(file_path, os.path.join(dest_folder, file))

    results.append({
        "Song": file,
        "Mood": prediction,
        "Confidence": round(confidence, 2)
    })

df = pd.DataFrame(results)
df.to_excel("results.xlsx", index=False)

print("Processing Complete!")
