import streamlit as st
import pandas as pd

def set_category_budgets():
    """Set budget for each category and save it to a CSV file."""
    st.title("Set Category Budgets")

    # Define the categories
    categories = [
        "Food & Beverages",
        "Groceries",
        "Transportation",
        "Housing",
        "Personal Care",
        "Subscriptions & Memberships",
        "Miscellaneous"
    ]

    # Initialize a dictionary to hold the budgets
    budgets = {}

    # Check if the budgets CSV file exists
    try:
        existing_budgets = pd.read_csv("category_budgets.csv")
        if "Category" not in existing_budgets.columns:
            raise FileNotFoundError  # Raise error to trigger the except block
    except FileNotFoundError:
        existing_budgets = pd.DataFrame(columns=["Category", "Budget"])

    # Create input fields for each category and populate the dictionary
    for category in categories:
        existing_budget = existing_budgets[existing_budgets["Category"] == category]["Budget"].max()
        budgets[category] = st.number_input(
            f"Budget for {category}:",
            value=float(existing_budget) if pd.notna(existing_budget) else 0.0,
            min_value=0.0,
            format="%.2f",
        )

    # Save the budgets to a CSV file
    if st.button("Save Budgets"):
        budgets_df = pd.DataFrame(list(budgets.items()), columns=["Category", "Budget"])
        budgets_df.to_csv("category_budgets.csv", index=False)
        st.success("Budgets saved successfully!")


def check_budgets(transactions_df):
    try:
        budgets_df = pd.read_csv("category_budgets.csv")
    except FileNotFoundError:
        st.warning("No budgets set. Please set budgets first.")
        return []

    exceeded_categories = []

    for _, row in budgets_df.iterrows():
        category = row["Category"]
        budget = row["Budget"]
        spent = transactions_df[transactions_df["Category"] == category]["Amount"].sum()
        if spent > budget:
            exceeded_categories.append(category)

    return exceeded_categories
