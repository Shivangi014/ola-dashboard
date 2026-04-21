import streamlit as st
import pandas as pd
import plotly.express as px
# page config
st.set_page_config(
    page_title="OLA Ride Insights",
    layout="wide"
)

# load data
df = pd.read_csv("ola_rides.csv")

st.title("🚖 OLA Ride Insights Dashboard")

# SIDEBAR FILTERS
st.sidebar.header("Filters")

vehicle = st.sidebar.multiselect(
    "Select Vehicle Type",
    df["vehicle_type"].unique(),
    default=df["vehicle_type"].unique()
)

payment = st.sidebar.multiselect(
    "Payment Method",
    df["payment_method"].unique(),
    default=df["payment_method"].unique()
)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["date"].min(), df["date"].max()]
)

# filter dataset
filtered_df = df[
    (df["vehicle_type"].isin(vehicle)) &
    (df["payment_method"].isin(payment)) &
    (df["date"] >= str(date_range[0])) &
    (df["date"] <= str(date_range[1]))
]

# KPI SECTION
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Revenue",
    round(filtered_df["booking_value"].sum(),2)
)

col2.metric(
    "Total Rides",
    len(filtered_df)
)

col3.metric(
    "Avg Rating",
    round(filtered_df["driver_rating"].mean(),2)
)

st.divider()

# CHARTS

col1, col2 = st.columns(2)

with col1:
    fig = px.line(
        filtered_df,
        x="date",
        y="booking_value",
        title="Revenue Trend"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig2 = px.pie(
        filtered_df,
        names="payment_method",
        title="Payment Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)

# vehicle analysis
fig3 = px.bar(
    filtered_df,
    x="vehicle_type",
    y="ride_distance",
    title="Ride Distance by Vehicle"
)

st.plotly_chart(fig3, use_container_width=True)

# rating distribution
fig4 = px.histogram(
    filtered_df,
    x="driver_rating",
    title="Driver Rating Distribution"
)

st.plotly_chart(fig4, use_container_width=True)

# powerbi integration
st.subheader("Power BI Dashboard")

powerbi_url = "PASTE_LINK"

st.components.v1.iframe(
    powerbi_url,
    height=600
)
# -------------------------
# POWER BI DASHBOARD IMAGES
# -------------------------

st.subheader("📊 Power BI Dashboards")

st.write("Overall View")
st.image("overall.png.png")

st.write("Vehicle Type Analysis")
st.image("vehicle.png.png")

st.write("Revenue Analysis")
st.image("revenue.png.png")

st.write("Cancellation Analysis")
st.image("cancellation.png.png")

st.write("Ratings Analysis")
st.image("ratings.png.png")
