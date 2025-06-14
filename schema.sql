DROP TABLE IF EXISTS traffic_stops;

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
);
