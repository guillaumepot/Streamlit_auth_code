"""
Streamlit example page with simple oauth authentication
"""


# LIBRARIES
import streamlit as st


from authentication_functions import validate_credentials, decode_jwt





# PAGE INITIALIZATION


# Use session state to store the access token and the selected account.
if 'access_token' not in st.session_state:
    st.session_state.access_token = None




## SIDEBAR

# Title
st.sidebar.title("Authentication example")

# Subheader
st.sidebar.subheader("Authentication")


# If not logged in
if st.session_state.access_token == None:  # Display login form if not logged in and an error message on the main page

    # Display error message if not logged in
    st.error("Please Log In to access the app.")


    # Activate the login form in the sidebar
    login_username = st.sidebar.text_input("Username")                      # Username text input
    login_password = st.sidebar.text_input("Password", type="password")     # Password text input

    # Define login_data
    login_data = {
        "username": login_username,
        "password": login_password,
    }

    # Request function on submitted Log In button
    st.sidebar.button("Log In", on_click=validate_credentials, args=(login_data,)) # Try to log in with the provided credentials, refers to validate_credentials function
    st.stop()


# If logged in successfully
else:
    # Logout button (release access token from session state)
    st.sidebar.empty()
    if st.sidebar.button("Log Out", key="sidebar_logout_button"):
        st.session_state.pop('access_token', None)
        st.rerun()

    pages=["Overview", "Credits"]
    page=st.sidebar.radio("Navigation", pages)


## END OF SIDEBAR


## PAGES

# Overview
if page == pages[0]:

    logged_username = decode_jwt(st.session_state.access_token)
    st.title(f"Welcome {logged_username} !")


if page == pages[1]:
    st.title("Credits")
    st.write("This app was made for educational purposes, do not use it in production !.")

    st.write("""
        <style>
        .reportview-container .main footer {visibility: hidden;}
        </style>
        """, unsafe_allow_html=True)

    footer="""
     <footer style="margin-top: 100px;">
        <p>Author: Guillaume Pot</p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/062guillaumepot/" target="_blank">Click Here</a></p>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)