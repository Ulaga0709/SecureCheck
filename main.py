import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import urllib.parse

# --- DATABASE CONNECTION (Cloud Ready) ---
# Replace this with your Render DB URL if deploying
password = urllib.parse.quote_plus("1WP1VTR2YZyM9aV49qpJJvghKyXSFBjo")
db_url = f"postgresql+psycopg2://securecheck_db_user:{password}@dpg-d1758vmmcj7s73cpt7m0-a.oregon-postgres.render.com/securecheck_db"
engine = create_engine(db_url)

# --- LOAD DATA ---
@st.cache_data(ttl=600)
def load_data():
    return pd.read_sql("SELECT * FROM traffic_stops", engine)

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔎 Filter Data")
country = st.sidebar.multiselect("🌍 Country", df['country_name'].unique(), default=df['country_name'].unique())
gender = st.sidebar.multiselect("🚻 Gender", df['driver_gender'].unique(), default=df['driver_gender'].unique())
violation = st.sidebar.multiselect("⚠️ Violation", df['violation'].unique(), default=df['violation'].unique())

filtered_df = df[
    (df['country_name'].isin(country)) &
    (df['driver_gender'].isin(gender)) &
    (df['violation'].isin(violation))
]

# --- TITLE ---
st.title("🚨 Traffic Stops Dashboard")
st.markdown("An interactive dashboard to explore traffic stop trends.")

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("👮 Total Stops", len(filtered_df))
col2.metric("🚓 Arrests", int(filtered_df['is_arrested'].sum()))
col3.metric("💊 Drug-Related Stops", int(filtered_df['drugs_related_stop'].sum()))

# --- DATA TABLE ---
st.subheader("📋 Filtered Traffic Stop Records")
st.dataframe(filtered_df, use_container_width=True)

# --- CHARTS ---
st.subheader("📊 Violation Frequency")
st.bar_chart(filtered_df['violation'].value_counts())

st.subheader("🧑 Driver Race Distribution")
st.bar_chart(filtered_df['driver_race'].value_counts())

st.subheader("🚻 Gender Breakdown")
gender_counts = filtered_df['driver_gender'].value_counts()
fig, ax = plt.subplots()
ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Optional: Trends Over Time (Uncomment if needed)
# st.subheader("📈 Stops Over Time")
# df['stop_date'] = pd.to_datetime(df['stop_date'])
# timeline = df.groupby('stop_date').size()
# st.line_chart(timeline)
