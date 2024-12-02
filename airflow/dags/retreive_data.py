from airflow import DAG
from datetime import datetime, date, timedelta
from airflow.operators.python import PythonOperator
import subprocess

def retreive_hashtag():
    print("finsihed task")
    currDate = date.today()
    
    result = subprocess.run(
        ["python", "/opt/airflow/dags/selenium_twitter_scraper_master/scraper", "--query=stocks invest finance min_faves:1000",  "--latest"],
        # ["python", "dags\selenium_twitter_scraper_master\scraper", "-ht=stocks"],
        # ["ls", "/opt/airflow/dags"],
        capture_output=True,  # Captures stdout and stderr
        text=True       
    )
    
    print(result.stdout)
    print(result.stderr)
    print("finsihed task")


default_args = {
    'owner': 'nou',  # Set the owner here
    'start_date': datetime(2024, 11, 10),
    'catchup': False
}


with DAG("retreival_x_data", 
         default_args=default_args, 
         schedule='@daily') as dag:
    task1 = PythonOperator(
        task_id="hashtag_retreive",  # Corrected the typo
        python_callable=retreive_hashtag
    )
