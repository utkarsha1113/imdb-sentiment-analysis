# 🎬 IMDb Sentiment Analysis using Simple RNN

A Deep Learning project that performs **binary sentiment classification** on IMDb movie reviews using a **Simple Recurrent Neural Network (RNN)**.

The model predicts whether a movie review is **positive** or **negative** based on learned text patterns.

---

## 🚀 Project Overview

This project implements a Recurrent Neural Network (RNN) for Natural Language Processing (NLP) tasks.

The model is trained on the **IMDb Movie Review Dataset** to classify sentiment into:

* Positive (1)
* Negative (0)

---

## 🧠 Model Architecture

* Embedding Layer
* SimpleRNN Layer
* Dense Layer (ReLU)
* Output Layer (Sigmoid)

Loss Function:

* Binary Crossentropy

Optimizer:

* Adam

Evaluation Metrics:

* Accuracy
* Precision
* Recall

---

## 📊 Model Performance

### 🔹 Training Metrics

* Accuracy: **97.33%**
* Loss: 0.0814
* Precision: 96.94%
* Recall: 97.77%

### 🔹 Validation Metrics

* Validation Accuracy: **82.44%**
* Validation Loss: 0.6352
* Validation Precision: 81.88%
* Validation Recall: 82.75%

The model performs strongly on training data and generalizes well on validation data.

---

## 📂 Project Structure

```
imdb-sentiment-analysis/
│
├── main.py
├── prediction.ipynb
├── simpleRnn_project.ipynb
├── word_embeddigs.ipynb
├── SimpleRNN_project.h5
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔍 Workflow

1. Text Preprocessing

   * Tokenization
   * Padding sequences
   * Vocabulary limiting
2. Word Embedding Layer
3. RNN Model Training
4. Model Evaluation
5. Model Saving (.h5 format)

---

## ⚙️ How to Run

1️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

2️⃣ Run main script:

```bash
python main.py
```

---

## 📈 Sample Prediction

Input:

```
"This movie was absolutely fantastic and thrilling!"
```

Output:

```
Positive Review
```

---

## 🛠 Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

---

## 🎯 Key Learnings

* Understanding sequence modeling using RNN
* Handling vanishing gradient limitations of SimpleRNN
* Word embeddings for NLP tasks
* Evaluating classification models using precision and recall

---

## 🔮 Future Improvements

* Replace SimpleRNN with LSTM / GRU
* Add Dropout for better generalization
* Use pre-trained embeddings (GloVe)
* Deploy using Streamlit

---

## 👨‍💻 Author

Utkarsha Mahendra Etam
Artificial Intelligence & Data Science Graduate
Interested in NLP & Deep Learning

---

⭐ If you found this project useful, give it a star!

```
```
