# MMA-Fighters-ETL-Pipeline
An Airflow-orchestrated ETL pipeline that ingests MMA data from an external API, stages raw records in PostgreSQL, and loads data into cleaned production table for downstream analytics.

# Technologies
- Python
- SQL
- Airflow
- PostgreSQL
- Docker

## Project Structure
'
.
├── src/
│   ├── alert.py          # sends email alert
│   ├── flow.py           # main ETL pipeline
│   ├── ingest.py         # fetches job offers from API
│   ├── transform.py      # transforms API JSON into flat table
│   ├── db_load.py        # loads offers into SQLite
│   ├── utils.py          # helpers & logging
│   └── settings.py       # loads environment variables
│
├── data/                 # raw JSON data
├── db/                   # SQLite database
├── tests/                # pytest test cases
├── .env.example          # environment template
├── Dockerfile            # container build definition
├── docker-compose.yml    # cron-enabled runtime
├── crontab.txt           # scheduled jobs
├── requirements.txt      # dependencies
├── pytest.ini            # adds project root to import path
├── LICENSE               # MIT license
└── README.md             # documentation
'
