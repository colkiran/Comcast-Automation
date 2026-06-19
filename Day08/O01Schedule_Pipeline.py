
import schedule
import time

def run_pipeline():
    print("Pipeline execution started.....")
    time.sleep(3)
    print("Pipeline completed execution successfully.....")

schedule.every().day.at("10:37").do(run_pipeline)

while True:
    schedule.run_pending()
    time.sleep(1)
