if [ ! -d "$SCRAPER_DATA_DIR" ]; then
    mkdir -p $SCRAPER_DATA_DIR/zip $SCRAPER_DATA_DIR/csv
fi

airflow db init

airflow users create \
    --username $AIRFLOW_ADMIN \
    --firstname $AIRFLOW_ADMIN_FNAME \
    --lastname $AIRFLOW_ADMIN_LNAME \
    --role Admin \
    --email $AIRFLOW_ADMIN_EMAIL
