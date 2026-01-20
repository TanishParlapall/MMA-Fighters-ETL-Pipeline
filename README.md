# 🥋 MMA-Fighters-ETL-Pipeline
An Airflow-orchestrated ETL pipeline that ingests MMA data from an external API, stages raw records, and loads data into a PostgreSQL table for downstream analytics. Transformed data is then connected to Power BI to build interactive visualizations and perform analytical comparisons.
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
- Schedules weekly execution using Airflow
- Runs using Docker
- Data can be connected to Power BI for interactive visualizations and analysis

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

## 🔄 DAG Overview
![dag structure](https://github.com/TanishParlapall/MMA-Fighters-ETL-Pipeline/blob/main/images/dag-structure.png)

## 🙋 Analytical Questions

This project explores the following questions:
- How does average wingspan compare between champions and non-champions within each weight class?
- Does age differ significantly between champions and non-champions across weight classes?
- Do champions tend to win via different methods (knockouts vs submissions) compared to non-champions?




## 📈 What the data says...
