import streamlit as st
from welcome import display_welcome_screen
from login import display_login_screen
from transactions import record_transaction, display_transactions
from visualisation import TransactionVisualizer


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
        # Sidebar for navigation
        current_page = st.sidebar.radio(
            "Navigate",
            ["Record Transaction", "Recorded Transactions", "Visualizations"],
        )

        if current_page == "Record Transaction":
            record_transaction()
        elif current_page == "Recorded Transactions":
            display_transactions()
        elif current_page == "Visualizations":
            visualizer = TransactionVisualizer("transactions.csv")
            visualizer.display_transactions()
            visualizer.plot_transaction_amount_distribution()
            visualizer.plot_transaction_amount_over_time()

        # Spacer to push the logout button to the bottom
        st.sidebar.write("")  # Empty line for spacing
        spacer = st.sidebar.empty()  # Create an empty container for spacing
        for _ in range(50):  # Adjust the range value to increase the space
            spacer.write("")  # Add empty lines to the spacer container

        # Logout button
        st.sidebar.write("---")  # Horizontal line for separation
        if st.sidebar.button("Logout"):
            st.session_state["authenticated"] = False
            st.experimental_rerun()  # Rerun the app to update the state

    elif st.session_state["show_login"]:
        # Display the login page if the 'Get Started' button was clicked
        display_login_screen()
    else:
        # Display the welcome screen if the user is not authenticated
        display_welcome_screen()


if __name__ == "__main__":
    main()