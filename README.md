# 🥋 MMA-Fighters-ETL-Pipeline
An Airflow-orchestrated ETL pipeline that ingests MMA data from an external API, stages raw records, and loads data into a PostgreSQL table for downstream analytics.

---

## 🤖 Technologies
- `Python`
- `SQL`
- `Airflow`
- `PostgreSQL`
- `Docker`

## 🚀 Features
- Fetches MMA data from the Sports Data API
- Transforms and loads data into PostgreSQL
- Schedules weekly execution with Airflow
- Runs using Docker

## 🧱 Project Structure
```
MMA-Fighters-ETL-Pipeline/
├── dags/
│   ├── dag.py
│   scripts/
│   ├── create_table.py
│   ├── extract_data.py
│   └── load_data.py
│   └── __init__.py
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
```

![dag structure](https://github.com/TanishParlapall/MMA-Fighters-ETL-Pipeline/blob/main/images/dag-structure.png)
