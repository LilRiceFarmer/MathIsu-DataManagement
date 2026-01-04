import os
import hashlib

PASS_DIR = "data/passwords"
os.makedirs(PASS_DIR, exist_ok=True) # Make a folder to store password files if it doesn't exist

def _hash(pw):
    return hashlib.sha256(pw.encode()).hexdigest()
    """   
    Turn a password into a fixed-length string of letters and numbers (a hash) using SHA-256.
    Hashing is NOT the same as encrypting — it is one-way:
        - You cannot get the original password back from the hash.
        - This makes it safe to store passwords without keeping them in plain text.
    When checking a password later, we hash the input and compare it to the stored hash.
    """
def set_password(name, pw):
    # Save a password for a given spreadsheet name
    # The password is hashed first so the plain text is never stored
    with open(f"{PASS_DIR}/{name}.txt", "w") as f:
        f.write(_hash(pw))# Write only the hashed version

def check_password(name, pw):
    # Check if a given password matches the saved password for a spreadsheet

    try:
        with open(f"{PASS_DIR}/{name}.txt") as f:
        # Hash the input password and compare it to the stored hash

            return f.read() == _hash(pw)
    except:
    # If file doesn't exist or any error occurs, treat as wrong password
        return False

def delete_password(name):
 # Delete the password file for a spreadsheet
    path = f"{PASS_DIR}/{name}.txt"
    if os.path.exists(path):
        os.remove(path) #removes file safely
