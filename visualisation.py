import streamlit as st
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap


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

    def plot_transaction_amount_distribution(self):
        st.title("Transaction Amount Distribution")
        hist_fig = figure(
            title="Transaction Amount Distribution",
            x_axis_label="Amount",
            y_axis_label="Frequency",
        )
        hist_fig.quad(
            top=self.transactions_df["Amount"].value_counts(),
            bottom=0,
            left=self.transactions_df["Amount"].value_counts().index - 0.4,
            right=self.transactions_df["Amount"].value_counts().index + 0.4,
            fill_color="navy",
        )
        st.bokeh_chart(hist_fig)

    def plot_transaction_amount_by_category(self):
        st.title("Transaction Amount by Category")
        box_fig = figure(
            title="Transaction Amount by Category",
            x_axis_label="Category",
            y_axis_label="Amount",
            x_range=self.transactions_df["Category"].unique(),
        )
        box_fig.vbar(
            x=self.transactions_df["Category"],
            top=self.transactions_df["Amount"],
            width=0.9,
        )
        st.bokeh_chart(box_fig)

    def plot_transaction_amount_over_time(self):
        st.title("Transaction Amount Over Time")
        line_fig = figure(
            title="Transaction Amount Over Time",
            x_axis_label="Date",
            y_axis_label="Amount",
            x_axis_type="datetime",
        )
        line_fig.line(
            self.transactions_df["Date/Time"],
            self.transactions_df["Amount"],
            line_width=2,
        )
        st.bokeh_chart(line_fig)

    def interactive_visualizations(self):
        st.title("Interactive Visualizations")
        self.interactive_histogram()
        self.interactive_box_plot_by_category()
        self.transaction_amount_over_time_by_category()
        self.interactive_date_range_plot()
        self.interactive_time_series_plot_by_category()

    def interactive_histogram(self):
        st.subheader("Interactive Histogram")
        amount_range = st.slider(
            "Select a range of transaction amounts",
            float(self.transactions_df["Amount"].min()),
            float(self.transactions_df["Amount"].max()),
            (
                float(self.transactions_df["Amount"].min()),
                float(self.transactions_df["Amount"].max()),
            ),
        )
        filtered_df = self.transactions_df[
            (self.transactions_df["Amount"] >= amount_range[0])
            & (self.transactions_df["Amount"] <= amount_range[1])
        ]
        hist_fig = figure(
            title="Filtered Transaction Amount Distribution",
            x_axis_label="Amount",
            y_axis_label="Frequency",
        )
        hist_fig.quad(
            top=filtered_df["Amount"].value_counts(),
            bottom=0,
            left=filtered_df["Amount"].value_counts().index - 0.4,
            right=filtered_df["Amount"].value_counts().index + 0.4,
            fill_color="green",
        )
        st.bokeh_chart(hist_fig)

    def interactive_box_plot_by_category(self):
        st.subheader("Interactive Box Plot by Category")
        selected_category = st.selectbox(
            "Select a category", self.transactions_df["Category"].unique()
        )
        category_df = self.transactions_df[
            self.transactions_df["Category"] == selected_category
        ]
        box_fig = figure(
            title=f"Transaction Amount for {selected_category}",
            x_axis_label="Category",
            y_axis_label="Amount",
            x_range=[selected_category],
        )
        box_fig.vbar(x=[selected_category], top=category_df["Amount"], width=0.9)
        st.bokeh_chart(box_fig)

    def transaction_amount_over_time_by_category(self):
        st.title("Transaction Amount Over Time by Category")
        line_fig = figure(
            title="Transaction Amount Over Time by Category",
            x_axis_label="Date",
            y_axis_label="Amount",
            x_axis_type="datetime",
        )
        line_fig.line(
            self.transactions_df["Date/Time"],
            self.transactions_df["Amount"],
            line_width=2,
            legend_label="Total",
        )
        for category in self.transactions_df["Category"].unique():
            category_df = self.transactions_df[
                self.transactions_df["Category"] == category
            ]
            line_fig.line(
                category_df["Date/Time"],
                category_df["Amount"],
                line_width=2,
                legend_label=category,
                color=Spectral6[
                    self.transactions_df["Category"].unique().tolist().index(category)
                ],
            )
        line_fig.legend.location = "top_left"
        st.bokeh_chart(line_fig)

    def interactive_date_range_plot(self):
        st.subheader("Interactive Date Range Plot")
        start_date, end_date = st.date_input(
            "Select a date range",
            [self.transactions_df["Date"].min(), self.transactions_df["Date"].max()],
        )
        date_filtered_df = self.transactions_df[
            (self.transactions_df["Date"] >= start_date)
            & (self.transactions_df["Date"] <= end_date)
        ]
        line_fig = figure(
            title="Transaction Amount Over Selected Date Range",
            x_axis_label="Date",
            y_axis_label="Amount",
            x_axis_type="datetime",
        )
        line_fig.line(
            pd.to_datetime(date_filtered_df["Date"]),
            date_filtered_df["Amount"],
            line_width=2,
        )
        st.bokeh_chart(line_fig)

    def interactive_time_series_plot_by_category(self):
        st.subheader("Interactive Time Series Plot by Category")
        selected_category_time_series = st.selectbox(
            "Select a category for the time series plot",
            self.transactions_df["Category"].unique(),
        )
        time_series_filtered_df = self.transactions_df[
            self.transactions_df["Category"] == selected_category_time_series
        ]
        time_series_fig = figure(
            title=f"Transaction Amount Over Time for {selected_category_time_series}",
            x_axis_label="Date",
            y_axis_label="Amount",
            x_axis_type="datetime",
        )
        time_series_fig.line(
            time_series_filtered_df["Date/Time"],
            time_series_filtered_df["Amount"],
            line_width=2,
            color="red",
        )
        st.bokeh_chart(time_series_fig)


def main():
    visualizer = TransactionVisualizer("transactions.csv")
    visualizer.display_transactions()
    visualizer.plot_transaction_amount_distribution()
    visualizer.plot_transaction_amount_by_category()
    visualizer.plot_transaction_amount_over_time()
    visualizer.interactive_visualizations()


if __name__ == "__main__":
    main()
