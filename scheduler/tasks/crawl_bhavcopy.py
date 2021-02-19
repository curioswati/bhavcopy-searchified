'''
Crawler DAG definition.
'''

import os
from datetime import datetime, timedelta
from os import path
from string import Template

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

PROJECT_PATH = path.abspath(path.join(path.dirname(__file__), '../../scraper'))
DATA_PATH = path.abspath(os.environ['SCRAPER_DATA_DIR'])

DEFAULT_ARGS = {
    'owner': 'airflow',
    'start_date': datetime(2021, 2, 8),
    'concurrency': 1,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('crawl_bhavcopy',
         default_args=DEFAULT_ARGS,
         schedule_interval='30 12 * * 0-4',  # the timezone is UTC here.
         catchup=True
         ) as dag:

    CREATE_DIR = BashOperator(
        task_id='create_datasets_dir',
        bash_command="""
            if [ ! -d {path} ]; then mkdir -p {path}/zip {path}/csv; fi
        """.format(path=DATA_PATH)
    )

    # Ref: https://airflow.apache.org/macros.html for the jinja variables used below.
    DOWNLOADER_COMMAND = Template("""
        cd $project_path && python downloader.py {{ (execution_date + macros.timedelta(days=1)).strftime('%d %m %Y') }}
    """)

    DOWNLOADER_TASK = BashOperator(
        task_id='download_zip',
        bash_command=DOWNLOADER_COMMAND.substitute(project_path=PROJECT_PATH),
    )

    EXTRACTOR_COMMAND = Template("""
        cd $project_path && python extractor.py {{ (execution_date + macros.timedelta(days=1)).strftime('%d %m %Y') }}
    """)

    EXTRACTOR_TASK = BashOperator(
        task_id='extract_zip',
        bash_command=EXTRACTOR_COMMAND.substitute(project_path=PROJECT_PATH),
    )

    LOADER_COMMAND = Template("""
        cd $project_path && python loader.py {{ (execution_date + macros.timedelta(days=1)).strftime('%d %m %Y') }}
    """)

    LOADER_TASK = BashOperator(
        task_id='load_into_redis',
        bash_command=LOADER_COMMAND.substitute(project_path=PROJECT_PATH),
    )

CREATE_DIR.set_downstream(DOWNLOADER_TASK)
DOWNLOADER_TASK.set_downstream(EXTRACTOR_TASK)
EXTRACTOR_TASK.set_downstream(LOADER_TASK)
