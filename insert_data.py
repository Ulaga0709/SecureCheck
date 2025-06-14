print("🚀 Script started...")

import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote

try:
    print("👉 Reading CSV file...")
    df = pd.read_csv("traffic_stops - traffic_stops_with_vehicle_number.csv")
    print(f"✅ CSV loaded! Rows: {len(df)}")

    password = quote("54321")
    engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost:5432/securecheck_db")
    print("✅ DB engine created!")

    with engine.connect() as conn:
        with open("schema.sql", "r") as f:
            conn.execute(text(f.read()))
        conn.commit()
    print("✅ Table created (if not already)")

    print("👉 Inserting data into 'traffic_stops' table...")
    df.to_sql("traffic_stops", engine, if_exists="append", index=False)
    print("✅ Data inserted!")

    with engine.connect() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM traffic_stops")).scalar()
        print(f"✅ Total rows in DB: {count}")

except Exception as e:
    print("❌ Error occurred:", e)
