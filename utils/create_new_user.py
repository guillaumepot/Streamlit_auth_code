"""
Generate a new user by providing a username and password.

Example of use:
python3 generate_user_credentials.py --user myusername --password mypassword
"""

# LIBS
import getpass
import json
import os
from passlib.context import CryptContext
import uuid


# Crypt context
crypt_context_scheme = "argon2" 

# Storage user file
users_file = '../src/users.json'



# MAIN FUNCTION
def main() -> None:
    """
    Generate a username and password for a user and add it into the users.json file.
    """
    # Get Username
    username = input('Enter the new username: ')

    # Get password
    while True:
        user_password = getpass.getpass('Enter the password: ')
        confirm_password = getpass.getpass('Confirm the password: ')
        if user_password == confirm_password:
            break
        else:
            print("Passwords don't match, please retry.")


    # Open user file
    try:
        with open(users_file, 'r') as f:
            users_data = json.load(f)
    except:
        print("Users file not found, creating a new one...")
        users_data = {'users': {}}
        with open(users_file, 'w') as f:
            json.dump(users_data, f)
        print("Users file created here: ", os.path.abspath(users_file))
        
    finally:
        # Check if user exists
        if username in users_data['users']:
            raise ValueError(f"User {username} already exists.")

        else:
            # Create user id
            user_id = str(uuid.uuid4())

            # Encrypt password
            pwd_context = CryptContext(schemes=[crypt_context_scheme], deprecated="auto")
            hashed_password = pwd_context.hash(user_password)

            # Add user to the users file
            users_data['users'][username] = {
                'id': user_id,
                'password': hashed_password
            }
            # Save users data
            with open(users_file, 'w') as f:
                json.dump(users_data, f, indent=4)


            # Return success message
            print(f"User {username} succefully registered.")


if __name__ == "__main__":
    main()