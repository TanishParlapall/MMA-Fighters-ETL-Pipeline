# MMA-Fighters-ETL-Pipeline
An Airflow-orchestrated ETL pipeline that ingests MMA data from an external API, stages raw records in PostgreSQL, and loads data into cleaned production table for downstream analytics.

# Technologies
- Python
- SQL
- Airflow
- PostgreSQL
- Docker

## Project Structure
```
MMA-Fighters-ETL-Pipeline/
├── dags/
│   ├── mma_etl_dag.py
│   └── scripts/
│       ├── create_table.py
│       ├── extract_data.py
│       └── load_data.py
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
```
