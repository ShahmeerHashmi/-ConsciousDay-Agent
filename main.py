import streamlit as st
from datetime import date
from agent.reflection_agent import generate_reflection
from db.database import save_entry
import sqlite3  # Add this for DB read

st.title("🧘 ConsciousDay Agent")

with st.form("reflection_form"):
    journal = st.text_area("Morning Journal")
    dream = st.text_area("Dream")
    intention = st.text_input("Intention for the Day")
    priorities = st.text_area("Top 3 Priorities (comma-separated)")

    submitted = st.form_submit_button("Generate Insights")

if submitted:
    with st.spinner("Processing..."):
        result = generate_reflection(journal, dream, intention, priorities)
        save_entry(date.today(), journal, dream, intention, priorities, result)

        st.success(f"✅ Entry saved for {date.today()}!")

        st.subheader("🪞 Inner Reflection")
        st.write(result["reflection"])

        st.subheader("📘 Day Strategy")
        st.write(result["strategy"])

# ✅ View latest saved entry after the form
st.markdown("---")
st.subheader("🔍 View Latest Saved Entry")

if st.button("Show Latest"):
    conn = sqlite3.connect("entries.db")
    c = conn.cursor()
    c.execute("SELECT * FROM entries ORDER BY id DESC LIMIT 1")
    latest = c.fetchone()
    conn.close()

    if latest:
        st.markdown("### 📅 Date")
        st.write(latest[1])
        st.markdown("### 📓 Journal")
        st.write(latest[2])
        st.markdown("### 💤 Dream")
        st.write(latest[3])
        st.markdown("### 🎯 Intention")
        st.write(latest[4])
        st.markdown("### ✅ Priorities")
        st.write(latest[5])
        st.markdown("### 🪞 Reflection")
        st.write(latest[6])
        st.markdown("### 📘 Strategy")
        st.write(latest[7])
    else:
        st.warning("No entries found.")
