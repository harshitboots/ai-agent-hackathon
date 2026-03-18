import pandas as pd
import os
from sklearn.metrics import accuracy_score, mean_squared_error, f1_score

# ==========================================================
# CONFIG — CHANGE IF NEEDED
# ==========================================================

PROBLEM_TYPE = "classification"  
# options: classification / regression / fraud

TARGET_COLUMN = "target_churn"

# ==========================================================
# LOAD TRUE LABELS
# ==========================================================

true_df = pd.read_csv("../data/test.csv")

results = []

submissions_path = "../submissions"

# ==========================================================
# LOOP THROUGH STUDENT SUBMISSIONS
# ==========================================================

for student in os.listdir(submissions_path):

    student_path = os.path.join(submissions_path, student)

    if os.path.isdir(student_path):

        file_path = os.path.join(student_path, "predictions.csv")

        if os.path.exists(file_path):

            try:
                pred_df = pd.read_csv(file_path)

                # Align rows
                merged = true_df.merge(pred_df, on="customer_id")

                y_true = merged[TARGET_COLUMN]
                y_pred = merged["prediction"]

                # ==================================================
                # CALCULATE SCORE
                # ==================================================

                if PROBLEM_TYPE == "classification":
                    score = accuracy_score(y_true, y_pred)

                elif PROBLEM_TYPE == "fraud":
                    score = f1_score(y_true, y_pred)

                elif PROBLEM_TYPE == "regression":
                    score = mean_squared_error(y_true, y_pred, squared=False)

                else:
                    score = 0

                results.append({
                    "student": student,
                    "score": round(score, 4)
                })

            except Exception as e:
                print(f"Error processing {student}: {e}")

# ==========================================================
# CREATE LEADERBOARD
# ==========================================================

leaderboard = pd.DataFrame(results)

if PROBLEM_TYPE == "regression":
    leaderboard = leaderboard.sort_values("score")  # lower is better
else:
    leaderboard = leaderboard.sort_values("score", ascending=False)

# Save leaderboard
leaderboard.to_csv("../leaderboard/leaderboard.csv", index=False)

print("\n🏆 Leaderboard Updated!\n")
print(leaderboard)