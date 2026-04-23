import streamlit as st
from datetime import datetime

st.title("User Data Collection")

# Create a form container
with st.form("user_details_form", clear_on_submit=True):
    st.subheader("Enter your details")
    
    # Input fields
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    experience = st.selectbox("Experience Level", ["Student", "Professional", "Other"])
    
    # Submit button
    submitted = st.form_submit_button("Save My Details")

    if submitted:
        if name and email: # Basic validation
            # Format the data string
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user_data = f"[{timestamp}] Name: {name}, Email: {email}, Gender: {gender}, Exp: {experience}\n"
            
            # Save to a text file
            try:
                with open("user_details.txt", "a") as f:
                    f.write(user_data)
                st.success(f"Thank you {name}, your details have been saved!")
            except Exception as e:
                st.error(f"An error occurred while saving: {e}")
        else:
            st.warning("Please fill in both Name and Email.")

# Option to view the data (for the admin)
if st.checkbox("Show collected data"):
    try:
        with open("user_details.txt", "r") as f:
            st.text(f.read())
    except FileNotFoundError:
        st.info("No data collected yet.")