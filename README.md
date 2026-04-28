# Bias Classifier App

An interactive application for detecting bias in text using natural language processing (NLP), combined with visual analytics.

This project was developed as part of a **hackathon**, focusing on ethical AI and bias detection in textual data.

---

## 📌 Overview

The Bias Classifier App allows users to:

* input arbitrary text
* analyse it for bias using a pretrained model
* visualise the bias score interactively

The application combines machine learning with a graphical user interface (GUI) to make bias detection accessible and intuitive.

---

## 🧠 How It Works

The system uses components from the **Dbias library**:

* **Bias Recognition** – identifies biased patterns
* **Bias Classification** – assigns a bias score
* **Bias Masking** – (optional) removes biased content

Core implementation:
👉 

---

## 🎯 Features

* 📝 Text input via GUI (Tkinter)
* 🤖 Bias classification using NLP models
* 📊 Visualisation of bias score:

  * Gauge chart (Plotly)
  * Pie chart (Matplotlib)
* ⚡ Real-time analysis

---

## 🖥️ User Interface

The application includes:

* Input field for text
* "Analyse" button
* Result display (label + score)
* Visual charts for interpretation

---

## 📊 Output

For each input text, the app provides:

* **Bias label** (e.g. biased / non-biased)
* **Confidence score**
* Visual breakdown:

  * Bias vs non-bias proportion
  * Gauge representation of severity

---

## ⚙️ Requirements

* Python 3.9+

Required libraries:

* tkinter
* matplotlib
* plotly
* Dbias

Install dependencies:

```bash
pip install matplotlib plotly
```

(Note: `tkinter` is usually included with Python)

---

## 🚀 Usage

Run the application:

```bash
python "Bias Classifier.py"
```

Then:

1. Enter text into the input field
2. Click **Analyse**
3. View classification results and charts

---

## 📂 Project Structure

```
.
├── Bias Classifier.py
└── README.md
```

---

## 🧠 Key Learnings

* Application of NLP for bias detection
* Integration of machine learning into a GUI
* Visualisation of model outputs
* Rapid prototyping in a hackathon setting

---

## ⚠️ Limitations

* Model performance depends on training data
* Bias detection can be subjective
* Scores should be interpreted cautiously

---

## 🔍 Future Improvements

* Add real-time text highlighting for biased words
* Support multiple languages
* Improve model accuracy with fine-tuning
* Deploy as a web application (Streamlit / Flask)

---
