import streamlit as st

st.title("User Detail Collector")

with st.form("user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    role = st.selectbox("Role", ["Developer", "Student", "Manager"])
    submitted = st.form_submit_button("Prepare File")

if submitted:
    if name and email:
        # Create the string content for the text file
        data_content = f"User Details:\nName: {name}\nEmail: {email}\nRole: {role}"
        
        # Create a download button
        st.download_button(
            label="Click here to download txt.txt",
            data=data_content,
            file_name="txt.txt",
            mime="text/plain"
        )
    else:
        st.error("Please fill in all fields.")