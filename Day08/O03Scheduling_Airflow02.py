from prefect import flow

@flow
def run_pipeline():
    print("Running modern data pipeline...")

if __name__ == "__main__":
    # Schedules the script directly using a cron string
    run_pipeline.serve(name="daily-pipeline", cron="0 0 * * *")





