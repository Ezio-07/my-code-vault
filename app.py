import streamlit as st
import os
import time

# Password configuration
PASSWORD = "Mukund07"
EXPIRY_SECONDS = 60 * 24 * 60 * 60  # 60 days

st.title("My Python Code Vault")

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    pwd = st.text_input("Enter Password to access vault:", type="password")
    if st.button("Unlock"):
        if pwd == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Incorrect password")
else:
    st.success("Access Granted")
    # Simple storage simulation
    uploaded_file = st.file_uploader("Upload Python File", type=['py'])
    
    if uploaded_file:
        # Save file with timestamp
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write(f"Saved: {uploaded_file.name}")

    # Display files that are less than 60 days old
    st.subheader("Your Stored Codes:")
    for file in os.listdir("."):
        if file.endswith(".py") and file != "app.py":
            file_age = time.time() - os.path.getmtime(file)
            if file_age < EXPIRY_SECONDS:
                with open(file, "r") as f:
                    st.code(f.read(), language="python")
            else:
                os.remove(file) # Auto-delete