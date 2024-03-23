import streamlit as st
from welcome import display_welcome_screen
from login import display_login_screen
from record import record_transaction, display_transactions


def main():
    """Control the flow of the application."""
    # Set up page configuration
    st.set_page_config(
        page_title="SavvySpend", page_icon=":money_with_wings:", layout="wide"
    )

    # Initialize session state variables if they don't exist
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "show_login" not in st.session_state:
        st.session_state["show_login"] = False

    if st.session_state["authenticated"]:
        # Sidebar for pagination
        current_page = st.sidebar.radio(
            "Navigate", ["Record Transaction", "Recorded Transactions"]
        )

        if current_page == "Record Transaction":
            record_transaction()
        elif current_page == "Recorded Transactions":
            display_transactions()
    elif st.session_state["show_login"]:
        # Display the login page if the 'Get Started' button was clicked
        display_login_screen()
    else:
        # Display the welcome screen if the user is not authenticated
        display_welcome_screen()


if __name__ == "__main__":
    main()
