<div align="center">

# AI Agent Hackathon

**Explore · Engineer · Train · Ship**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Agent-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE)

*Build a machine learning model. Wrap it in an AI agent. Get evaluated automatically.*

</div>

---

## Overview

In this hackathon you will work through a real-world dataset end-to-end — from raw exploration through to a deployed, interactive AI agent. Your submission is scored automatically on metrics **and** reviewed by an AI judge for prediction quality, generalisation, and business usability.

```
Dataset → Exploration → Feature Engineering → Model Training → Predictions
                                                                    ↓
                                                         AI Agent (Streamlit)
                                                                    ↓
                                                         Evaluation + AI Judge
                                                                    ↓
                                                              Leaderboard
```

---

## Project Structure

```
ai-agent-hackathon/
│
├── data/
│   ├── train.csv                        # Training dataset
│   └── test.csv                         # Test dataset
│
├── notebooks/
│   ├── 01_generate_dataset.ipynb        # Dataset generation
│   ├── 02_data_exploration.ipynb        # Phase 1 — Explore
│   ├── 03_feature_engineering.ipynb     # Phase 2 — Engineer
│   ├── 04_model_training.ipynb          # Phase 3 — Train
│   └── 05_generate_predictions.ipynb    # Phase 4 — Predict
│
├── models/
│   └── model.pkl                        # Your saved model goes here
│
├── outputs/
│   └── YOURNAME_predictions.csv         # Your submission goes here
│
├── evaluations/
│   └── evaluate.py                      # Evaluation logic
│
├── app/
│   ├── app.py                           # Phase 5 — AI Agent (Streamlit)
│   └── leaderboard_app.py               # Phase 6 — Leaderboard
│
└── requirements.txt
```

---

## Quickstart

```bash
# Clone the repo
git clone https://github.com/harshitboots/ai-agent-hackathon.git
cd ai-agent-hackathon

# Install dependencies
pip install -r requirements.txt

# Run your AI agent
streamlit run app/app.py

# Run the leaderboard
streamlit run app/leaderboard_app.py
```

---

## Step 0 — Choose Your Target

Pick **one** target variable before opening any notebook. Your choice determines model type and evaluation metrics.

| Target | Task | Evaluation Metrics |
|---|---|---|
| `target_churn` | Classification | Accuracy, F1, AI Judge |
| `target_fraud` | Classification | Accuracy, F1, AI Judge |
| `target_revenue` | Regression | MSE, R², AI Judge |

---

## Phase Guide

### Phase 1 — Data Exploration
> `notebooks/02_data_exploration.ipynb`

Understand the dataset before touching any model code.

- Examine column types, distributions, and missing values
- Identify correlations and relationships between variables
- Confirm your target variable choice

---

### Phase 2 — Feature Engineering
> `notebooks/03_feature_engineering.ipynb`

> **This is the most impactful phase.** Better features beat better models every time.

- Clean missing values and handle outliers
- Encode categorical variables
- Construct new features from existing ones

**Example features to try:**

```python
df['activity_score']      = df['logins'] * df['session_duration']
df['engagement_ratio']    = df['clicks'] / df['impressions']
df['spend_per_transaction'] = df['total_spend'] / df['num_transactions']
```

---

### Phase 3 — Model Training
> `notebooks/04_model_training.ipynb`

Train, compare, and save your best model.

| Type | Models |
|---|---|
| Baseline | Logistic Regression, Linear Regression |
| Tree-based | Random Forest, Gradient Boosting |
| Advanced | XGBoost |

Save your best model:

```python
import pickle
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
```

---

### Phase 4 — Generate Predictions
> `notebooks/05_generate_predictions.ipynb`

Load your model and predict on test data.

**Output format — strictly enforced:**

```
actual,prediction
1,1
0,0
1,0
...
```

**File naming — strictly enforced:**

```
outputs/YOURNAME_predictions.csv

# Example
outputs/harshit_predictions.csv
```

> Any deviation in format or naming will cause evaluation to fail.

---

### Phase 5 — Build Your AI Agent
> `app/app.py`

Wrap your model in a Streamlit interface.

```bash
streamlit run app/app.py
```

Your agent should:
- Accept user inputs for each feature
- Load the saved model and run inference
- Display the prediction and confidence score
- Handle edge cases gracefully

---

### Phase 6 — Evaluation + Leaderboard
> `app/leaderboard_app.py`

```bash
streamlit run app/leaderboard_app.py
```

Click **Run Evaluation**. Scores are computed automatically and the leaderboard updates in real time.

---

## Scoring

### Classification (`target_churn`, `target_fraud`)

| Metric | Weight |
|---|---|
| Accuracy | 50% |
| F1 Score | 30% |
| AI Judge | 20% |

### Regression (`target_revenue`)

| Metric | Weight |
|---|---|
| MSE (lower is better) | 60% |
| R² Score | 20% |
| AI Judge | 20% |

### AI Judge

Your model is also evaluated by an AI on three dimensions:

- **Prediction quality** — how well predictions match ground truth patterns
- **Generalisation** — does it perform consistently or does it overfit?
- **Business usability** — are the predictions actionable and interpretable?

---

## Rules

**Allowed**
- Any model or algorithm
- Custom-engineered features
- Customising your Streamlit agent
- Using AI tools (ChatGPT, Claude, Copilot) to assist

**Not allowed**
- Changing the output file format
- Incorrect file naming
- Multiple submissions after the deadline

---

## Useful AI Prompts

Copy these into any AI assistant to accelerate your work.

```
# Feature engineering
Suggest 5 advanced features for a churn prediction dataset with transactional and behavioural columns

# Model selection
Which model is best for binary classification with imbalanced tabular data?

# Hyperparameter tuning
How do I tune XGBoost to improve F1 score on an imbalanced dataset?

# Debugging
My Random Forest overfits training data — what should I try?

# Streamlit agent
Write a Streamlit app that loads a pickled sklearn model and shows prediction with confidence score

# Improving F1
What techniques improve F1 score for a churn classification problem?
```

---

## Pro Tips

- **Feature engineering first** — spend at least 40% of your time here
- Try at least two model types and compare validation metrics before picking one
- Check feature importances — drop anything with near-zero importance
- Start simple, get the full pipeline working end-to-end, then iterate
- The AI judge notices edge case handling — test your agent with unusual inputs

---

## Pre-Submission Checklist

```
□ Model trained and saved as models/model.pkl
□ Predictions generated on the test dataset
□ File saved inside outputs/ directory
□ File named correctly: YOURNAME_predictions.csv
□ CSV has exactly two columns: actual, prediction
□ Streamlit agent runs without errors
□ Submitted before the deadline
```

---

<div align="center">

*"Your model is your brain. Your agent is your product."*

**Good luck — build something worth deploying.**

</div>
