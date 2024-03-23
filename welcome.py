import streamlit as st


def display_welcome_screen():
    """Display the welcome screen."""
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
