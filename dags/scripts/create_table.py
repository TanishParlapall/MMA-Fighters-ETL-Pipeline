from airflow.providers.postgres.hooks.postgres import PostgresHook

# create production table if none exists
def create_table():
    hook = PostgresHook(postgres_conn_id="fighters_connection")
    hook.run("""
        CREATE TABLE IF NOT EXISTS fighters (
            id SERIAL PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            height DECIMAL,
            reach DECIMAL,
            weight_class TEXT,
            birth_date DATE,
            title_wins INTEGER,
            technical_knockouts INTEGER,
            submissions INTEGER,
            uid INTEGER NOT NULL,
            CONSTRAINT fighter_unique UNIQUE (uid)
        );
    """)
