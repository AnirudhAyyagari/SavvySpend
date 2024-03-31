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
                "Description/Notes": description,
                "Frequency": frequency,
            }
            # Append the transaction to the transaction DataFrame
            new_row = pd.DataFrame([transaction])
            try:
                # Read existing data and append new transaction
                existing_data = pd.read_csv("transactions.csv")
                updated_data = pd.concat([existing_data, new_row], ignore_index=True)
                # Save the updated transaction DataFrame to CSV
                updated_data.to_csv("transactions.csv", index=False)
                st.success("Transaction recorded successfully!")
                logging.info("Transaction recorded successfully.")
            except FileNotFoundError:
                # Create a new CSV file with the transaction if the file does not exist
                new_row.to_csv("transactions.csv", index=False)
                st.success("Transaction recorded successfully in a new file!")
                logging.info("Transaction recorded successfully in a new file.")
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
        st.write(
            "No transactions recorded yet. Please record a transaction to create the file."
        )
        logging.info(
            "No transactions recorded yet. CSV file will be created upon recording the first transaction."
        )


if __name__ == "__main__":
    display_transactions()
    record_transaction()
