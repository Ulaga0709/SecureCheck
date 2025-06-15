from sqlalchemy import create_engine, text
import pandas as pd

df = pd.read_csv(
    "traffic_stops - traffic_stops_with_vehicle_number.csv",
    dtype={"search_type": str},
    low_memory=False
)

df['search_type'] = df['search_type'].fillna("None")  # Avoid nulls



# Use your Render DB credentials
engine = create_engine("postgresql+psycopg2://securecheck_db_user:1WP1VTR2YZyM9aV49qpJJvghKyXSFBjo@dpg-d1758vmmcj7s73cpt7m0-a.oregon-postgres.render.com/securecheck_db")

with engine.connect() as conn:
    # Optional: Create table schema if not exists
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS traffic_stops (
        stop_date DATE,
        stop_time TIME,
        country_name TEXT,
        driver_gender TEXT,
        driver_age_raw INTEGER,
        driver_age INTEGER,
        driver_race TEXT,
        violation_raw TEXT,
        violation TEXT,
        search_conducted BOOLEAN,
        search_type TEXT,
        stop_outcome TEXT,
        is_arrested BOOLEAN,
        stop_duration TEXT,
        drugs_related_stop BOOLEAN,
        vehicle_number TEXT
    )
    """))
    conn.commit()

# Insert data
df.to_sql("traffic_stops", engine, if_exists="append", index=False)
print("✅ Data inserted to Render DB!")
