<<<<<<< HEAD
# Music Mood AI
=======
# 🎵 Music Mood AI
>>>>>>> ed25cc1 (Updated README with full setup guide and usage instructions)

An AI-based system that classifies music into moods and automatically organizes songs into folders while generating an Excel report.

---

## 🚀 Features

- 🎧 Music Mood Classification (Happy, Sad, Calm, Energetic)
- 📊 Excel Report Generation
- 📁 Automatic File Sorting
- ⚡ Fast Baseline Model (MFCC + Random Forest)
- 🔄 Scalable to Transformer Models (Wav2Vec2)

---

## 🛠️ Tech Stack

- Python
- Librosa
- Scikit-learn
- Pandas
- NumPy

---

## 📦 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/music-mood-ai.git
cd music-mood-ai

## 2. Create Virtual Environment
Windows
python -m venv .venv
.venv\Scripts\activate
Linux / Mac
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
<<<<<<< HEAD

python src/train_model.py

python src/predict_and_sort.py

## Future Work

=======

## 📁 Dataset Structure

Create this inside project:

dataset/
   happy/
   sad/
   calm/
   energetic/

Add .mp3 or .wav files inside each folder.

🧠 Train Model
python src/train_model.py

Model will be saved in:

models/mood_model.pkl
🎯 Run Prediction

Add songs inside:

input_songs/

Then run:

python src/predict_and_sort.py
📊 Output
Sorted Songs
sorted_songs/
   happy/
   sad/
   calm/
   energetic/
Excel Report
results.xlsx
⚠️ Common Errors
Module not found
pip install -r requirements.txt
Permission Error

Close audio files

Run terminal as admin

🔮 Future Improvements

Wav2Vec2 Transformer Upgrade

Streamlit Web UI

Real-time audio input

API deployment

👨‍💻 Author
>>>>>>> ed25cc1 (Updated README with full setup guide and usage instructions)
