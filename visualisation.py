import streamlit as st
import pandas as pd
import plotly.express as px

class TransactionVisualizer:
    def __init__(self, csv_path):
        self.transactions_df = pd.read_csv(csv_path)
        self.transactions_df["Date/Time"] = pd.to_datetime(
            self.transactions_df["Date/Time"]
        )
        self.transactions_df["Date"] = self.transactions_df["Date/Time"].dt.date
        self.transactions_df["Amount"] = pd.to_numeric(
            self.transactions_df["Amount"], errors="coerce"
        )

    def display_transactions(self):
        st.title("Recorded Transactions")
        st.dataframe(self.transactions_df)

    def plot_transaction_amount_over_time(self):
        st.title("Cumulative Transaction Amount Over Time")
        # Calculate the cumulative sum of amounts for each category over time
        self.transactions_df['Cumulative Amount'] = self.transactions_df.groupby('Category')['Amount'].cumsum()
        fig = px.line(
            self.transactions_df,
            x="Date",
            y="Cumulative Amount",
            color="Category",
            title="Cumulative Transaction Amount Over Time by Category",
        )
        st.plotly_chart(fig)

    def plot_transaction_amount_distribution(self):
        st.title("Transaction Amount Distribution by Category")
        fig = px.box(
            self.transactions_df,
            x="Category",
            y="Amount",
            color="Category",
            title="Transaction Amount Distribution by Category",
            notched=True,  # Adds notches to the boxes for a better estimation of the median
        )
        st.plotly_chart(fig)


