
# 🚦 SecureCheck: Traffic Stop Analysis Dashboard

SecureCheck is a powerful data dashboard that visualizes traffic stop records, violations, and arrest patterns using interactive Streamlit components.

---

## 📊 Features

- 🔍 **Explore full traffic stop data**
- 📈 **Visualizations** of violation types, arrest patterns, and search conduct
- 🌍 **Country-wise analysis**
- 🧠 **Insightful summaries** of driver demographics
- 🗃️ Backed by **PostgreSQL** database
- ⚡ Built using **Streamlit**, **pandas**, **SQLAlchemy**, **psycopg2**

---

## 🧰 Technologies Used

| Tool         | Purpose                         |
|--------------|----------------------------------|
| Streamlit    | Web app / dashboard              |
| pandas       | Data manipulation                |
| SQLAlchemy   | Database ORM layer               |
| psycopg2     | PostgreSQL connection            |
| PostgreSQL   | Database                         |
| matplotlib   | Charts (optional)                |

---

## 🏁 How to Run Locally

1. 🔽 Clone this repo:
   ```bash
   git clone https://github.com/Sivakami/SecureCheck.git
   cd SecureCheck
   ```

2. ⚙️ Set up virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. 🛢️ Configure DB connection inside `main.py`:
   ```python
   engine = create_engine("postgresql+psycopg2://postgres:<your_password>@localhost:5432/securecheck_db")
   ```

4. 🚀 Run the app:
   ```bash
   streamlit run main.py
   ```

---

## 📦 Folder Structure

```
SecureCheck/
│
├── traffic_stops - traffic_stops_with_vehicle_number.csv
├── insert_data.py         # Script to insert CSV into DB
├── main.py                # Streamlit dashboard
├── requirements.txt       # Python dependencies
└── README.md              # Project info
```

---

## 👩‍💻 Author

**Sivakami**  
GitHub: [github.com/Sivakami](https://github.com/Sivakami)

---

## 📄 License

MIT License – use freely for learning and development!
