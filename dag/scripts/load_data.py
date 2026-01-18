from airflow.providers.postgres.hooks.postgres import PostgresHook

# load data into production table
def load_into_postgres():
    
    # merge stage and production tables
    postgres_hook = PostgresHook(postgres_conn_id='fighters_connection')
    insert_query = """
        MERGE INTO fighters AS f
        USING stg_fighters AS s
        ON (
            f.uid = s.uid
        )
        WHEN MATCHED THEN
            UPDATE SET
                height = s.height,
                reach = s.reach,
                weight_class = s.weight_class,
                birth_date = s.birth_date,
                title_wins = s.title_wins,
                technical_knockouts = s.technical_knockouts,
                submissions = s.submissions
        WHEN NOT MATCHED THEN
            INSERT (
                first_name, last_name, height, reach, weight_class,
                birth_date, title_wins, technical_knockouts, submissions, uid
            )
            VALUES (
                s.first_name, s.last_name, s.height, s.reach, s.weight_class,
                s.birth_date, s.title_wins, s.technical_knockouts, s.submissions, s.uid
        );

        TRUNCATE TABLE stg_fighters;
    """
    postgres_hook.run(insert_query)
