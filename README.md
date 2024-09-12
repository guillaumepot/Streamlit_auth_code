# Streamlit_auth_code
Simple example for Streamlit auth

/!\
JWT secret key, algorithm, crypt context scheme are HARDCODED for educational purpose !
Do not use the code as it is in production
/!\

## 1 - Create a python venv with the requirements

- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

## 2 - Generate users

- Use the script 'create_new_user.py' (./utils) to generate users
- Users are generated in ./src/user.json


## 3 - Streamlit

- Start streamlit (streamlit run ./src/streamlit/main.py)
- Use user credentials to connect