import streamlit as st
import pandas as pd

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="OLA Ride Insights",
    layout="wide"
)

st.title("🚖 OLA Ride Insights Dashboard")

# -------------------------
# LOAD DATA
# -------------------------

df = pd.read_csv("clean_ola_data.csv")

# -------------------------
# SIDEBAR FILTERS
# -------------------------

st.sidebar.header("Filter Data")

vehicle = st.sidebar.multiselect(
    "Vehicle Type",
    options=df["Vehicle_Type"].dropna().unique(),
    default=df["Vehicle_Type"].dropna().unique()
)

payment = st.sidebar.multiselect(
    "Payment Method",
    options=df["Payment_Method"].dropna().unique(),
    default=df["Payment_Method"].dropna().unique()
)

status = st.sidebar.multiselect(
    "Booking Status",
    options=df["Booking_Status"].dropna().unique(),
    default=df["Booking_Status"].dropna().unique()
)

# apply filters
filtered_df = df[
    (df["Vehicle_Type"].isin(vehicle)) &
    (df["Payment_Method"].isin(payment)) &
    (df["Booking_Status"].isin(status))
]

# -------------------------
# KPI METRICS
# -------------------------

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", len(filtered_df))

col2.metric(
    "Total Revenue ₹",
    int(filtered_df["Booking_Value"].sum())
)

col3.metric(
    "Avg Customer Rating",
    round(filtered_df["Customer_Rating"].mean(),2)
)

cancel_rate = (
    len(filtered_df[filtered_df["Booking_Status"] != "Success"])
    / len(filtered_df)
)*100

col4.metric(
    "Cancellation %",
    round(cancel_rate,2)
)

# -------------------------
# FILTERED DATA TABLE
# -------------------------

st.subheader("📄 Filtered Dataset")

st.dataframe(filtered_df)

# -------------------------
# SQL-LIKE INSIGHTS
# -------------------------

st.subheader("📈 Insights")

# avg ride distance
avg_distance = (
    filtered_df
    .groupby("Vehicle_Type")["Ride_Distance"]
    .mean()
    .reset_index()
)

st.write("Average Ride Distance by Vehicle Type")

st.dataframe(avg_distance)

# revenue by payment
revenue = (
    filtered_df
    .groupby("Payment_Method")["Booking_Value"]
    .sum()
    .reset_index()
)

st.write("Revenue by Payment Method")

st.dataframe(revenue)

# top customers
top_customers = (
    filtered_df
    .groupby("Customer_ID")["Booking_Value"]
    .sum()
    .reset_index()
    .sort_values(by="Booking_Value", ascending=False)
    .head(5)
)

st.write("Top 5 Customers by Spending")

st.dataframe(top_customers)

# -------------------------
# POWER BI DASHBOARD IMAGES
# -------------------------

st.subheader("📊 Power BI Dashboards")

st.write("Overall View")
st.image("dashboards/overall.png")

st.write("Vehicle Type Analysis")
st.image("dashboards/vehicle.png")

st.write("Revenue Analysis")
st.image("dashboards/revenue.png")

st.write("Cancellation Analysis")
st.image("dashboards/cancellation.png")

st.write("Ratings Analysis")
st.image("dashboards/ratings.png")
