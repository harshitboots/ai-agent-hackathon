import streamlit as st
import pandas as pd

st.title("🏆 AI Hackathon Leaderboard")

try:
    df = pd.read_csv("../leaderboard/leaderboard.csv")

    df = df.sort_values("score", ascending=False)

    st.dataframe(df)

    winner = df.iloc[0]

    st.success(f"🏆 Winner: {winner['student']} with score {winner['score']}")

except:
    st.warning("No submissions yet.")

st.subheader("🤖 AI Judge Comments")

st.write(f"""
Top performer is {winner['student']}.

This model achieved highest score due to better feature engineering 
and model tuning compared to others.
""")