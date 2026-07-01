# 🚀 Career Readiness AI Placement Prediction System


---

# 🌐 Live Demo

The model has been integrated with a Flask web application and deployed on Render for public access.

🔗 **Try the Application:**

[Click Here to Predict House Prices](https://careerreadiness-ai-placement-prediction.onrender.com/)

> **Note:** Predictions are based on the features used during model training and should be considered as an estimation of placement readiness.

---

# 📌 Project Overview

The Career Readiness AI Placement Prediction System is an end-to-end Machine Learning project designed to predict whether a student is placement-ready based on academic performance, technical skills, aptitude, communication skills, internships, projects, certifications, and other career-related factors.

The project includes the complete machine learning workflow, starting from data preprocessing and exploratory data analysis to feature engineering, model training, evaluation, hyperparameter tuning, and deployment.

The final trained model is integrated with a FastAPI web application and an HTML/CSS/JavaScript frontend, allowing users to receive instant placement readiness predictions through a user-friendly interface.

---

# 🎯 Business Problem

Educational institutions and students often struggle to identify placement readiness early enough for improvement.

This project aims to:

* Predict whether a student is placement-ready.
* Identify important factors influencing placements.
* Help students understand areas requiring improvement.
* Support placement cells in monitoring student performance.
* Assist trainers in designing personalized learning plans.

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* FastAPI
* Jinja2 Templates
* HTML
* CSS
* JavaScript
* Joblib
* Uvicorn
* pydantic

---

# 📊 Dataset

Dataset Used:

```text
Data/placement_dataset_2026.csv
```

The dataset contains student-related attributes such as:

* CGPA
* Programming Skills
* Aptitude Score
* Communication Skills
* Projects Completed
* Internship Experience
* Certifications
* Technical Skills
* Soft Skills
* Placement Status (Target Variable)


---

# 🔄 Project Workflow

```text
Load Data
    ↓
Understand Data
    ↓
Exploratory Data Analysis
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Train-Test Split
    ↓
Baseline Modeling
    ↓
Model Comparison
    ↓
Hyperparameter Tuning
    ↓
Final Model Selection
    ↓
FastAPI Deployment
```

---

# 🧪 Project Phases

## Phase 1 — Data Loading

* Load the dataset.
* Inspect dataset dimensions.
* Identify feature types.

## Phase 2 — Understanding Data

* Analyze feature distributions.
* Check missing values.
* Detect duplicate records.
* Generate descriptive statistics.

## Phase 3 — Exploratory Data Analysis (EDA)

* Univariate Analysis
* Bivariate Analysis
* Correlation Analysis
* Target Variable Analysis

## Phase 4 — Data Cleaning

* Handle missing values.
* Remove duplicate records.
* Correct inconsistent values.

## Phase 5 — Feature Engineering

* Encode categorical variables.
* Scale numerical features.
* Prepare data for machine learning.

## Phase 6 — Train-Test Split

* Split the dataset into training and testing sets.

## Phase 7 — Baseline Modeling

Train multiple classification algorithms.

## Phase 8 — Model Comparison

Compare model performance using evaluation metrics.

## Phase 9 — Hyperparameter Tuning

Optimize the best-performing models.

## Phase 10 — Deployment

Deploy the final model using FastAPI with an HTML user interface.

---

# 🤖 Machine Learning Models Used

The following classification algorithms were trained and evaluated:

| Model |
|-------|
| Logistic Regression |
| Decision Tree Classifier |
| Random Forest Classifier |
| K-Nearest Neighbors (KNN) |
| Support Vector Machine (SVM) |
| Naive Bayes |
| XGBoost Classifier |
| Voting Classifier |
| Stacking Classifier |

---

# 🏆 Best Performing Models

After evaluating all classification algorithms, the following models produced the best performance:

* Random Forest Classifier
* Support Vector Machine (SVM)

---

# ⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed on the top-performing models to improve prediction accuracy.

After evaluation, the best-performing model was selected as the final production model.

---

# 🎯 Final Model

**Selected Model**

```text
Random Forest Tuned 
```

**Saved Model Location**

```text
Models/RandomForest_Tuned.pkl
```

The trained model can be loaded for future predictions without retraining.

---

# 💻 Web Application

The prediction system has been developed using:

* FastAPI Backend
* HTML
* CSS
* JavaScript
* Jinja2 Templates

Users simply enter the required student details, and the model instantly predicts whether the student is placement-ready.

---

# 📈 Key Insights

### 1. Academic Performance

Students with higher academic scores generally have better placement readiness.

### 2. Technical Skills

Programming and technical proficiency strongly influence placement outcomes.

### 3. Internship Experience

Students with internship experience demonstrate higher placement success.

### 4. Projects and Certifications

Completing multiple projects and industry certifications positively impacts employability.

### 5. Communication Skills

Strong communication skills significantly improve placement readiness.

---

# ✅ Conclusion

This project successfully developed an end-to-end machine learning pipeline for predicting student placement readiness.

Multiple classification algorithms were evaluated, compared, and optimized through hyperparameter tuning.

The final model was integrated into a FastAPI web application, providing users with real-time placement readiness predictions through a clean and interactive web interface.

The system can assist students, educational institutions, and placement coordinators in making informed decisions and improving placement outcomes.

---

# 📂 Project Structure

```text
CareerReadiness-AI-Placement-Prediction/
│
├── Data/
├── src/
├── Models/
├── notebooks/
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 👨‍💻 Author

**Vamshi Dunna**

**LinkedIn:** https://www.linkedin.com/in/vamshi-dunna-7a56a8275

**GitHub:** https://github.com/imdvamshi