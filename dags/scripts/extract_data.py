import os
import pandas as pd
import requests
from airflow.providers.postgres.hooks.postgres import PostgresHook

# extract and stage MMA data
def fetch_MMA_data():
    
    # using the Sports Data API for MMA data
    key = os.getenv("SPORTS_API_KEY")
    url = f"https://api.sportsdata.io/v3/mma/scores/json/FightersBasic?key={key}"
    response = requests.get(url)
    fighters = response.json()

    df = pd.DataFrame(fighters)
    records = df.to_dict('records')

    # stage fighters for transformation
    postgres_hook = PostgresHook(postgres_conn_id='fighters_connection')
    stg_query = """
    
    CREATE TABLE IF NOT EXISTS stg_fighters (
            first_name TEXT,
            last_name TEXT,
            height DECIMAL,
            reach DECIMAL,
            weight_class TEXT,
            birth_date DATE,
            title_wins INTEGER,
            technical_knockouts INTEGER,
            submissions INTEGER,
            uid INTEGER
        );

    INSERT INTO stg_fighters (first_name, last_name, height, reach, weight_class, birth_date, title_wins, technical_knockouts, submissions, uid)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for fighter in records:

        # ensure all columns exist in record
        if (fighter['FirstName'] is not None and 
           fighter['LastName'] is not None and
           fighter['Height'] is not None and
           fighter['Reach'] is not None and
           fighter['WeightClass'] is not None and
           fighter['BirthDate'] is not None and
           fighter['TitleWins'] is not None and
           fighter['TechnicalKnockouts'] is not None and
           fighter['Submissions'] is not None and
           fighter['FighterId'] is not None):
            postgres_hook.run(stg_query, parameters=(fighter['FirstName'], 
                                                        fighter['LastName'], 
                                                        fighter['Height'], 
                                                        fighter['Reach'],
                                                        fighter['WeightClass'],
                                                        fighter['BirthDate'],
                                                        fighter['TitleWins'],
                                                        fighter['TechnicalKnockouts'],
                                                        fighter['Submissions'],
                                                        fighter['FighterId']))
