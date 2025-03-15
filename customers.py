import pandas as pd
import plotly.express as px
import streamlit as st
import db

min_date, max_date = db.fetch_date_boundaries()

with st.sidebar:
    st.write('---')
    st.write('Main filter')
    edate = st.date_input(
        label = 'Select report date',
        min_value = min_date,
        max_value = max_date,
        value = max_date
    )

custs_df = db.fetch_customers(edate)
min_duration, max_duration = custs_df['duration'].agg(['min', 'max'])

selected_duration = st.sidebar.number_input(
    label = 'Select duration of customer experience',
    min_value = min_duration,
    max_value = max_duration,
    value = max_duration
)

duration_filter = f"duration <= {selected_duration}"

filter = f"{duration_filter}"

custs_filtered = custs_df.query(filter)

unique_custs_number = custs_df['customer_key'].nunique()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(
    'Number of customers',
    unique_custs_number
)

col2.metric(
    'Average customer age',
    int(custs_filtered['age'].mean())
)

col3.metric(
    'Median customer age',
    int(custs_filtered['age'].median())
)



r2_col1, r2_col2 = st.columns(2)

genders_breakdown = custs_filtered['gender'].value_counts().to_frame().reset_index()
genders_pie = px.pie(
    data_frame=genders_breakdown,
    values='count',
    names='gender',
    title='Customers breakdown by gender'
)
r2_col1.plotly_chart(genders_pie)


marital_breakdown = custs_filtered['marital_status'].value_counts().to_frame().reset_index()
marital_donut = px.pie(
    data_frame=marital_breakdown,
    values='count',
    names='marital_status',
    hole=.5,
    title='Customers breakdown by marital status'
)
r2_col2.plotly_chart(marital_donut)

ages_hist = px.histogram(
    data_frame=custs_filtered,
    x = 'age',
    color='gender',
    title='Customer ages distribution'
)
st.plotly_chart(ages_hist)