import streamlit as st

def check_credentials(username, password):
    """Check the provided credentials for validity."""
    return username == "admin" and password == "password"

def display_login_screen():
    """Display the login page and handle user authentication."""
    with st.form(key="login_form"):
        st.title("Login")
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        submit_button = st.form_submit_button(label="Login")

        if submit_button:
            if check_credentials(username, password):
                # Set the session state to indicate the user is authenticated
                st.session_state["authenticated"] = True
                st.success("You are logged in!")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")
