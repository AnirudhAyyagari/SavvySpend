import streamlit as st
import pandas as pd
import logging
from datetime import datetime

# Set up logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def record_transaction():
    """Record a new transaction with various details and append it to a CSV file."""
    st.title("Record a New Transaction")
    transaction_df = pd.DataFrame(
        columns=[
            "Date/Time",
            "Amount",
            "Category",
            "Merchant",
            "Payment Method",
            "Location",
            "Description/Notes",
            "Frequency",
        ]
    )
    if transaction_df.empty:
        transaction_df = pd.DataFrame(
            columns=[
                "Date/Time",
                "Amount",
                "Category",
                "Merchant",
                "Payment Method",
                "Location",
                "Description/Notes",
                "Frequency",
            ]
        )

    with st.form(key="transaction_form"):
        # Collect transaction details from user input
        date = st.date_input("Date/Time", value=datetime.today())
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        category = st.selectbox(
            "Category",
            ["Groceries", "Rent", "Utilities", "Transportation", "Other"],
        )
        merchant = st.text_input("Merchant")
        payment_method = st.selectbox(
            "Payment Method",
            ["Cash", "Credit Card", "Debit Card", "Other"],
        )
        location = st.text_input("Location")
        description = st.text_area("Description/Notes")
        frequency = st.selectbox(
            "Frequency",
            ["One-time", "Daily", "Weekly", "Monthly"],
        )
        submit_button = st.form_submit_button(label="Record Transaction")

        if submit_button:
            # Create a dictionary with the transaction details
            transaction = {
                "Date/Time": date,
                "Amount": amount,
                "Category": category,
                "Merchant": merchant,
                "Payment Method": payment_method,
                "Location": location,
                "Description/Notes": description,
                "Frequency": frequency,
            }
            # Append the transaction to the transaction DataFrame
            new_row = pd.DataFrame([transaction])
            try:
                transaction_df = pd.concat([transaction_df, new_row], ignore_index=True)
                # Save the updated transaction DataFrame to CSV
                transaction_df.to_csv("transactions.csv", index=False, mode="a")
                st.success("Transaction recorded successfully!")
                logging.info("Transaction recorded successfully.")
            except Exception as e:
                st.error("Error recording transaction: {}".format(str(e)))
                logging.error("Error recording transaction: {}".format(str(e)))


def display_transactions():
    """Display the recorded transactions in a table by reading from a CSV file."""
    st.title("Recorded Transactions")
    try:
        transaction_df = pd.read_csv("transactions.csv")
        if not transaction_df.empty:
            st.dataframe(transaction_df)
        else:
            st.write("No transactions recorded yet.")
    except FileNotFoundError:
        st.write("No transactions recorded yet.")
        logging.info("No transactions recorded yet.")


if __name__ == "__main__":
    display_transactions()
    record_transaction()