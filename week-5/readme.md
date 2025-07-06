
# 📦 Data Pipeline: Export & Copy Between Databases with Automation

This project demonstrates a complete data pipeline workflow that includes:

1. Exporting data from a relational database into multiple formats
2. Automating the pipeline with schedule and event triggers
3. Copying full database tables from source to destination
4. Selective table and column-level copying for targeted migration

---

## 📌 Features

### ✅ 1. Export to Multiple Formats
- **CSV**: For general use and compatibility
- **Parquet**: For efficient analytics
- **Avro**: For compact serialization and schema evolution

### ✅ 2. Automation with Triggers
- **Scheduled Trigger**: Automates periodic pipeline execution
- **Event-Based Trigger**: Watches a folder and reacts to new file arrivals

### ✅ 3. Full Database Replication
- Copies all tables and data from a source SQLite database to a destination
- Maintains schema and ensures backup/migration readiness

### ✅ 4. Selective Table & Column Copying
- Transfer specific tables with only the needed columns
- Reduces data volume and enhances compliance with data minimization principles

---

## 🛠️ Tech Stack

- Python 3.12
- SQLite3
- Pandas
- SQLAlchemy
- FastAvro (for Avro export)
- PyArrow (for Parquet export)
- Watchdog (for folder monitoring)

---

## 🧪 How to Run

### ▶️ Step 1: Install Required Packages

```bash
pip install pandas sqlalchemy fastavro pyarrow watchdog
````

## ▶️ Step 2: Run Export Script

```bash
python exportfiles.py
```

## ▶️ Step 3: Run Event Trigger (Watches for CSV Files)

```bash
python eventtrigger.py
```

## ▶️ Step 4: Run Full Table Copy

```bash
python copymydatabase.py
```

## ▶️ Step 5: Run Selective Column Copy

```bash
python selectivedatatransfer.py
```

---

## 🧾 File Structure

```
├── mydatabase.db                # Source SQLite database
├── exportfiles.py              # Script to export data to CSV, Parquet, Avro
├── eventtrigger.py                  # Event trigger using watchdog
├── copymydatabase.py          # Full DB replication
├── selectivedatatransfer.py   # Targeted column-level copy
├── README.md                   # This file
```


