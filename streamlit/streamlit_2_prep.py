import streamlit as st
import time as t
import pandas as pd
import numpy as np

# Page Config (Sets the browser tab title and icon)
st.set_page_config(page_title="Anil Reddy Site", page_icon=":rocket:", layout="centered")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Navigation")
    st.image("https://via.placeholder.com/150") # Placeholder for profile pic
    st.write("### Welcome to Anil's Site")
    st.text_input("Mail Address")
    st.text_input("Password", type="password")
    st.button("Login")
    st.divider()
    st.radio("Professional Status", ["Student", "Professional", "Other"])

# --- HEADER SECTION ---
st.title("🚀 ANIL REDDY SITE")
st.header("Welcome to my web page")
st.subheader("Explore the interactive components below")

# --- FEEDBACK MESSAGES (In Columns) ---
col1, col2 = st.columns(2)
with col1:
    st.info("Information available here.")
    st.success("Task completed successfully!")
with col2:
    st.warning("Please check your input.")
    st.error("System encountered an error.")

# --- TABS FOR ORGANIZATION ---
tab1, tab2, tab3 = st.tabs(["Profile & Text", "Input Widgets", "Data Visualization"])

with tab1:
    st.markdown("### User Profile")
    st.write("**Employee Name:** Anil Reddy")
    st.caption("Site Administrator & Developer")
    
    st.divider()
    st.markdown("#### Markdown Demo")
    st.markdown("Normal Text | # Header 1 | ## Header 2")
    st.markdown(":moon: :star: :sunny:")
    
    st.text("Technical Notes: Learning Streamlit Framework")
    st.latex(r'''a + bx^2 + c = 0''')

with tab2:
    st.markdown("### Interactive Widgets")
    
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox('Stay logged in')
        st.button("Click Me")
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        choice = st.selectbox("Course Choice", ["ML", "Cloud", "Cyber Security"])
    
    with c2:
        st.multiselect("Department", ["Content", "Sales", "Marketing"])
        st.select_slider("Rating", ["Bad", "Good", "Excellent", "Outstanding"])
        st.slider("Experience Level", 0, 100, 50)
        # Fixed syntax error: added comma and value
        st.number_input("Pick a number", 0, 100)

    st.divider()
    st.text_input("Email Address", placeholder="example@mail.com")
    st.date_input("Select Date")
    st.time_input("Select Time")
    st.text_area("Feedback/Comments")
    st.file_uploader("Upload your documents")
    st.color_picker("Pick a brand color")

with tab3:
    st.title("Data Insights")
    # Fixed data display
    chart_data = pd.DataFrame(np.random.randn(50, 2), columns=["Metric A", "Metric B"])
    
    st.subheader("Bar Chart Analysis")
    st.bar_chart(chart_data)
    
    st.subheader("Area Trend")
    st.area_chart(chart_data)
    
    st.subheader("Raw Data Preview")
    st.dataframe(chart_data, use_container_width=True)

# --- LOADING STATES ---
st.divider()
progress_bar = st.progress(0)
for percent_complete in range(100):
    t.sleep(0.01)
    progress_bar.progress(percent_complete + 1)

with st.spinner("Finalizing layout..."):
    t.sleep(1)

st.balloons()
st.toast("Welcome aboard!", icon='🎉')