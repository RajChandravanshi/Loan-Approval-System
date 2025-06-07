# Loan Approval Classification Project Report

**Author**: Raj Chandravanshi

---

## 📌 Objective
Predict the likelihood of loan approval using demographic, financial, and credit history features via various machine learning and deep learning models.

---

## 📊 Dataset Overview
- **Rows**: 45,000  
- **Columns**: 14  
- **Target Variable**: `loan_status`

### Features
- **Demographics**: `person_age`, `person_gender`, `person_education`  
- **Financial**: `person_income`, `loan_amnt`, `loan_percent_income`, `credit_score`  
- **Employment**: `person_emp_exp`  
- **Credit History**: `cb_person_cred_hist_length`, `previous_loan_defaults_on_file`  
- **Loan Info**: `loan_intent`, `loan_int_rate`, `person_home_ownership`

---

## 🧹 Data Cleaning
- No missing or duplicate values
- Detected **15,438 outliers** (not removed to retain label integrity)

---

## 📈 Exploratory Data Analysis (EDA)

### Categorical Variables
- Count plots were generated to assess loan approval distribution across categorical features.

### Numerical Variables
- Skewness observed in: `person_income`, `loan_int_rate`
- Strong influence from: `credit_score`, `loan_amnt`

### Correlation
- Heatmap analysis showed `credit_score` and `loan_int_rate` are highly influential.

---

## 🛠️ Feature Engineering
- One-hot encoding for categorical features
- Used `ColumnTransformer`
- Train-test split: **80/20**

---

## 🤖 Modeling (Before SMOTE)

### Models Used
- Decision Tree
- Random Forest
- Extra Trees
- XGBoost
- Gradient Boosting

### 📋 Model Performance (Before SMOTE)

| Model              | Accuracy | Precision | Recall  | ROC AUC |
|--------------------|----------|-----------|---------|---------|
| Decision Tree      | 0.8991   | 0.7707    | 0.7766  | 0.8553  |
| Random Forest      | 0.9264   | 0.8919    | 0.7607  | 0.9731  |
| Extra Trees        | 0.9152   | 0.8537    | 0.7458  | 0.9660  |
| **XGBoost**        | **0.9324** | **0.8822** | **0.8026** | **0.9774** |
| Gradient Boosting  | 0.9233   | 0.8765    | 0.7621  | 0.9717  |

---

## ⚖️ Class Imbalance Handling (SMOTE)
- SMOTE applied to balance the classes  
- Dataset expanded to **70,000 samples**

### 📋 Model Performance (After SMOTE)

| Model              | Accuracy | Precision | Recall  | ROC AUC |
|--------------------|----------|-----------|---------|---------|
| Decision Tree      | 0.9270   | 0.9258    | 0.9286  | 0.9270  |
| Random Forest      | 0.9524   | 0.9601    | 0.9441  | 0.9922  |
| Extra Trees        | 0.9492   | 0.9522    | 0.9460  | 0.9916  |
| **XGBoost**        | **0.9563** | **0.9648** | **0.9472** | **0.9936** |
| Gradient Boosting  | 0.9439   | 0.9440    | 0.9439  | 0.9900  |

---

## 🧠 Deep Learning Models
### Keras-based ANN
- 4 hidden layers (ReLU, BatchNorm, Dropout)
- Optimizer: Adam  
- Loss: Binary Crossentropy  
- Trained for 500 epochs with Early Stopping(71 epochs) 
- Recall on validation dataset is 0.9229
---

## ✅ Conclusions
- **Best Model**: XGBoost (after SMOTE)
- **Best Metric**: ROC AUC = 0.9936
- **Important Features**: `credit_score`, `loan_amnt`, `loan_int_rate`, `previous_loan_defaults_on_file`
- **Recommendation**: Use tree-based ensemble models like **XGBoost** in production

---
