import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import urllib.parse

# Encode password
password = urllib.parse.quote_plus("54321")
engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost:5432/securecheck_db")

# Load Data
df = pd.read_sql("SELECT * FROM traffic_stops", engine)

# Sidebar Filters
st.sidebar.header("🔎 Filter Data")
country = st.sidebar.multiselect("🌍 Country", df['country_name'].unique(), default=df['country_name'].unique())
gender = st.sidebar.multiselect("🚻 Gender", df['driver_gender'].unique(), default=df['driver_gender'].unique())
violation = st.sidebar.multiselect("⚠️ Violation", df['violation'].unique(), default=df['violation'].unique())

filtered_df = df[
    (df['country_name'].isin(country)) &
    (df['driver_gender'].isin(gender)) &
    (df['violation'].isin(violation))
]

# Title
st.title("🚨 Traffic Stops Dashboard")
st.markdown("An interactive dashboard to monitor traffic stop data.")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("👮 Total Stops", len(filtered_df))
col2.metric("🚓 Arrests", filtered_df['is_arrested'].sum())
col3.metric("💊 Drug Stops", filtered_df['drugs_related_stop'].sum())

# Data Preview
st.subheader("📋 Filtered Data")
st.dataframe(filtered_df, use_container_width=True)

# Violation Bar Chart
st.subheader("📊 Violation Count")
violation_counts = filtered_df['violation'].value_counts()
st.bar_chart(violation_counts)

# Driver Race Chart
st.subheader("🧑 Driver Race Count")
race_counts = filtered_df['driver_race'].value_counts()
st.bar_chart(race_counts)

# Gender Pie Chart
st.subheader("🚻 Gender Distribution")
gender_counts = filtered_df['driver_gender'].value_counts()
fig, ax = plt.subplots()
ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Optional: Line chart of stops over time
# df['stop_date'] = pd.to_datetime(df['stop_date'])
# line_df = df.groupby('stop_date').size()
# st.line_chart(line_df)
