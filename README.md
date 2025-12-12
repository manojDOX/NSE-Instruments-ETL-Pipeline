---

# 📈 NSE ETL Pipeline

A lightweight ETL (Extract–Transform–Load) pipeline that downloads symbol master data from **Upstox** and **Dhan**, cleans & transforms it, stores it in **MongoDB** and **SQLite**, and finally generates comparison reports for analysis.

---

## 🚀 Features

* **Extract**

  * Fetch Upstox symbol master (gzip CSV)
  * Fetch Dhan symbol master (CSV)
* **Transform**

  * Normalize column names
  * Clean trading symbols (trim, uppercase)
  * Filter required columns
  * Prepare comparison-ready datasets
* **Load**

  * **MongoDB** → Upsert Upstox data (`market_data.upstox_nse`)
  * **SQLite** → Store Dhan data (`db/dhan_data.db`)
* **Compare**

  * Find differences between Upstox & Dhan symbol lists
  * Generate 3 reports:

    * `common_stocks.csv`
    * `only_in_upstox.csv`
    * `only_in_dhan.csv`

---

## 📦 Project Structure

```
NSE_ETL_PIPELINE/
│── db/
│   ├── dhan_data.db
│   ├── mongo_setup.py
│   └── sql_setup.sql
│
│── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── compare.py
│   ├── test_extract.py
│   ├── test_transform.py
│   └── __pycache__/
│
│── output/
│   ├── common_stocks.csv
│   ├── only_in_upstox.csv
│   └── only_in_dhan.csv
│
│── main.py
│── README.md
│── requirements.txt
└── .venv/
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/nse_etl_pipeline.git
cd nse_etl_pipeline
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Prerequisites

### ✔ MongoDB

The pipeline loads Upstox data into MongoDB.

Ensure MongoDB is running on:

```
mongodb://localhost:27017/
```

If using Docker:

```bash
docker run -d -p 27017:27017 --name mongo mongo:6.0
```

### ✔ SQLite

No setup needed — the SQLite database (`db/dhan_data.db`) is created automatically.

---

## ▶️ Run the Pipeline

```bash
python main.py
```

This will:

* Download fresh symbol master files
* Apply transformations
* Load data into MongoDB & SQLite
* Compare both datasets
* Generate CSV reports inside the `output/` folder

---

## 📤 Output Files

| File                   | Description                           |
| ---------------------- | ------------------------------------- |
| **common_stocks.csv**  | Symbols present in both Upstox & Dhan |
| **only_in_upstox.csv** | Symbols present only in Upstox        |
| **only_in_dhan.csv**   | Symbols present only in Dhan          |

---

## 🔑 Key Assumptions

* **Trading symbol (`SEM_TRADING_SYMBOL`) is treated as the unique identifier** while comparing.
* Dataset formats from Upstox & Dhan follow their documented schema.
* MongoDB will auto-create the database (`market_data`) and collection (`upstox_nse`) during upsert operations.

---

## 🧪 Testing

Basic tests for extract & transform logic:

```bash
pytest
```

---

## 🛠 Future Enhancements

* Add logging & monitoring for ETL pipeline
* Add incremental updates (avoid full reload)
* Enable cloud database support (Mongo Atlas / Postgres)
* Add Docker Compose for full environment setup
* Integrate Airflow / Prefect for scheduling

---

## 🤝 Contributing

Feel free to open issues or submit PRs!

---
