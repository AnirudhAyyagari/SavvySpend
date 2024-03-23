import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="SavvySpend", page_icon=":money_with_wings:", layout="wide"
)


def display_ui_elements():
    """Display UI elements for the welcome screen."""
    # Load styles
    st.markdown(
        """
        <style>
            /* CSS for the whole body */
            body {
                margin: 0;
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                background-color: #1e3c72; /* Deep blue background */
                color: #FFFFFF; /* White text color */
                text-align: center;
            }

            /* CSS for the image box */
            .image-box {
                width: 60%; /* Smaller width for the image */
                margin: 2rem auto;
                border: 5px solid #FFFFFF; /* White border */
                border-radius: 15px; /* Rounded corners */
            }

            /* CSS for the button */
            .stButton>button {
                font-size: 1.25rem;
                border-radius: 25px;
                padding: 0.75rem 2rem;
                font-weight: bold;
                background-color: #FF4B4B; /* Button color */
                border: 2px solid #FFFFFF; /* White border */
                color: white;
                margin-top: 2rem;
                display: block;
                width: 20%; /* Width of the button */
                margin-left: auto;
                margin-right: auto;
            }

            /* Hiding the Streamlit hamburger menu and footer */
            #MainMenu, footer {
                display: none;
            }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # Display title and subtitle
    st.markdown('<h1 class="title">SavvySpend</h1>', unsafe_allow_html=True)
    st.markdown(
        '<h2 class="subtitle">Manage your finances easily</h2>', unsafe_allow_html=True
    )
    st.caption("Start monitoring your personal finances and set personalized goals.")

    # Display image
    image_url = "https://www.neverendingvoyage.com/wp-content/uploads/2022/12/top-beautiful-places-new-zealand-tasman-glacier.jpg"
    st.markdown("<div class='image-box'>", unsafe_allow_html=True)
    st.image(image_url, use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Display 'Get Started' button and handle click action
    if st.button("Get Started", key="get_started_welcome"):
        st.session_state["show_login"] = True  # Set the flag to show the login page
        st.experimental_rerun()


def check_credentials(username, password):
    """Check the provided credentials for validity."""
    # Here you should implement your actual authentication logic
    return username == "admin" and password == "password"


def login_page():
    """Display the login page and handle user authentication within a form."""
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


def main():
    """Control the flow of the application between the welcome screen, login page, and main content."""
    # Initialize session state variables if they don't exist
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "show_login" not in st.session_state:
        st.session_state["show_login"] = False

    if st.session_state["authenticated"]:
        # Display the main content of the app if the user is authenticated
        st.success("You are now logged in!")
        st.write("Welcome to SavvySpend!")
        # Here you can add more content for your main app
    elif st.session_state["show_login"]:
        # Display the login page if the 'Get Started' button was clicked
        login_page()
    else:
        # Display the welcome screen if the user is not authenticated
        display_ui_elements()


if __name__ == "__main__":
    main()
