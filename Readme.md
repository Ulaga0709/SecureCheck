# 🚨 Traffic Stops Dashboard

A powerful interactive dashboard built with **Streamlit** and connected to a **PostgreSQL** database. The app lets users explore traffic stop data with real-time filters, charts, and statistics.

---

## 🌐 Live URLs

- **Frontend App (Streamlit):**  
  🔗 [https://securecheck.streamlit.app](https://securecheck.streamlit.app)

- **Backend Database (Render - PostgreSQL):**  
  🔗 `postgresql://securecheck_db_user:1WP1VTR2YZyM9aV49qpJJvghKyXSFBjo@dpg-d1758vmmcj7s73cpt7m0-a.oregon-postgres.render.com/securecheck_db`

> **Note**: The backend URL is private and should be used securely inside environment variables or `secrets.toml`.

---

## 📊 Features

- 📋 View full traffic stop dataset
- 🔎 Filter by country, gender, and violation
- 📈 Bar charts for violations & driver race
- 🧁 Pie chart for gender distribution
- 📅 (Optional) Time trend line chart
- ⚡ Real-time updates via Streamlit UI

---

## 🛠️ Tech Stack

| Layer       | Tech             |
|-------------|------------------|
| Frontend    | Streamlit        |
| Backend     | PostgreSQL (Render) |
| ORM         | SQLAlchemy       |
| Data        | Pandas           |
| Viz         | matplotlib, Streamlit Charts |

---

## 🚀 Getting Started Locally

### 1. Clone the repository
```bash
git clone https://github.com/Ulaga0709/traffic-stops-dashboard.git
cd traffic-stops-dashboard
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.streamlit/secrets.toml`
```toml
DB_URL = "postgresql+psycopg2://securecheck_db_user:1WP1VTR2YZyM9aV49qpJJvghKyXSFBjo@dpg-d1758vmmcj7s73cpt7m0-a.oregon-postgres.render.com/securecheck_db"
```

### 4. Run the app
```bash
streamlit run main.py
```

---

## 📂 Project Structure

```
.
├── main.py                 # Streamlit app
├── insert_data.py          # CSV to DB upload script
├── requirements.txt        # Python dependencies
├── schema.sql              # Table schema
├── README.md               # You're here
├── .streamlit/
│   └── secrets.toml        # Contains DB credentials
```

---

## 📷 Screenshot

![Dashboard Screenshot](screenshot.png)

---

## 👤 Author

**Sivakami (Ulaga0709)**  
🔗 GitHub: [https://github.com/Ulaga0709](https://github.com/Ulaga0709)

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use and modify it for your own projects.
