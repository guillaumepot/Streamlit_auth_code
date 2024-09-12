from datetime import datetime, timedelta
import json
import jwt
import streamlit as st
from passlib.context import CryptContext



# Auth variables (/!\ Prefer to use env variables sor security measures)
crypt_context_scheme = 'argon2'
pwd_context = CryptContext(schemes=[crypt_context_scheme], deprecated="auto")
algorithm = 'HS256'
access_token_expiration = 60 #(minutes)
jwt_secret_key = "fa61daz1f6az5f16DAFf#s4abv!65a1f65afGLxUz6-fpz?zF1ahM6x5816a5f"

# Streamlit variables
login_placeholder = st.sidebar.empty()



def validate_credentials(login_data: dict) -> None:
    """
    This function will be called when the "Log In" button is pressed
    """

    # Load existing user datas from table
    with open('../users.json', 'r') as f:
        users_data = json.load(f)

    # Check if the username is correct
    if login_data['username'] not in users_data['users']:
        st.sidebar.error("Incorrect Username or Password.")
        return
    
    # Check if the password is correct
    if not pwd_context.verify(login_data['password'], users_data['users'][login_data['username']]['password']):
        st.sidebar.error("Incorrect Username or Password.")
        return

    # Set token
    token_expiration = timedelta(minutes=access_token_expiration)
    expire = datetime.now() + token_expiration
    data__to_encode = {"sub": login_data['username'], "exp": expire}
    encoded_jwt = jwt.encode(data__to_encode, jwt_secret_key, algorithm=algorithm)

    # Set the access token in the session state
    st.session_state.access_token = encoded_jwt


    # Clear the login form
    login_placeholder.empty()
    # Empty the sidebar
    st.sidebar.empty()




def decode_jwt(access_token: str) -> dict:

    try:
        payload = jwt.decode(access_token, jwt_secret_key, algorithms=[algorithm])
        username = payload.get("sub")
    except Exception as e:
        raise e
    
    return username
