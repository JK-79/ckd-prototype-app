# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 16:20:10 2025

@author: Jayyant Kakkar
"""

import streamlit as st

st.set_page_config(page_title="CKD Care App Prototype", layout="wide")

# Sidebar for navigation
st.sidebar.title("CKD Care App")
section = st.sidebar.radio(
    "Go to",
    ("Dashboard", "Diet & Lifestyle", "Consultations", "Medication", "Community", "Records & Reports")
)

st.markdown(f"# {section}")

if section == "Dashboard":
    st.subheader("Welcome!")
    st.write(
        """
        - Track your health progress at a glance
        - View upcoming consultations
        - Catch daily CKD tips
        """
    )
    st.metric("Today's BP", "128/82 mmHg", "+2")
    st.metric("Weight", "68 kg", "-0.4")
    st.metric("Glucose", "105 mg/dL", "Stable")
    st.progress(70)
    st.info("Remember: Stay hydrated, but follow your doctor's limits!")
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=500&q=60", width=300, caption="Stay Active")

elif section == "Diet & Lifestyle":
    st.subheader("Personalized Diet Plan")
    st.write("Sample meal: Dalia, Lauki curry, low-salt chapati, bowl of papaya")
    st.markdown("### Foods to monitor:")
    st.warning("High potassium: Bananas, oranges, coconut water")
    st.success("Low potassium: Apples, grapes, pineapples")
    st.write("**Daily log:**")
    meal = st.text_input("What did you eat today?")
    if meal:
        st.success(f"Meal logged: {meal}")
    st.markdown("#### Recipes & Tips")
    st.write("- Try 'Lauki Soup' with mild spices")
    st.write("- Avoid pickles, salted snacks, and processed cheese.")

elif section == "Consultations":
    st.subheader("Book a Consultation")
    st.write("Available experts:")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://randomuser.me/api/portraits/men/32.jpg", width=100)
        st.write("Dr. Ravi Kumar, Nephrologist")
        if st.button("Book with Dr. Ravi"):
            st.success("Consultation booked! You'll be contacted soon.")
    with col2:
        st.image("https://randomuser.me/api/portraits/women/86.jpg", width=100)
        st.write("Ms. Priya Singh, Dietitian")
        if st.button("Book with Priya"):
            st.success("Appointment set with Dietitian Priya.")

elif section == "Medication":
    st.subheader("Medication Tracker")
    st.write("Add your current medications:")
    med = st.text_input("Medication name")
    dose = st.text_input("Dosage & Timing")
    if st.button("Add Medication"):
        if med and dose:
            st.success(f"Added: {med} ({dose})")
        else:
            st.error("Please fill all medication info.")
    st.write("**Example:** Sevelamer 800mg, 1 tablet morning & evening")

elif section == "Community":
    st.subheader("CKD Support Group")
    st.write("Ask questions, share tips, or support others:")
    msg = st.text_area("Type your message")
    if st.button("Post Message"):
        if msg:
            st.info(f"You posted: {msg}")
        else:
            st.error("Message cannot be empty.")
    st.write("**Recent posts:**")
    st.write("- _How do I manage fatigue on dialysis? - Suresh_")
    st.write("- _Share your favorite CKD-friendly Indian snacks! - Anita_")

elif section == "Records & Reports":
    st.subheader("Your Health Records")
    st.write("Upload new prescriptions, lab reports or download/share with your care team.")
    uploaded = st.file_uploader("Upload PDF or image", type=['pdf', 'jpg', 'png'])
    if uploaded:
        st.success(f"Uploaded: {uploaded.name}")
    st.write("**Example records available:**")
    st.download_button("Sample Report", data="Sample data", file_name="ckd_report.pdf")

st.sidebar.markdown("---")
st.sidebar.write("Demo version for investor review. UX and content are for illustration only.")
