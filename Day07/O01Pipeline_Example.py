import pandas as pd
import numpy as np
import logging
from datetime import  datetime

# setup the logging config
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s   -    %(message)s")


def extract_data(file_path: str) -> pd.DataFrame:
    logging.info(f"Extracting data from file {file_path}")
    return pd.read_csv(file_path)

def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    # Impute unnecessary data from the dataframe
    df = df.copy()
    # if price is null or negative the assign median
    median_val= df['price'].median()
    df['price'] = np.where((df['price'].isna()) | (df['price'] <= 0), median_val, df['price'])
    return df

def apply_business_rules(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['margin_status'] = np.where(df['price'] > 500, 'High Margin', 'standard')
    return df

def filter_records(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['status']]

def load_data(df: pd.DataFrame, output_path: str) -> None:
    df.to_csv(output_path, index=False)
    logging.info(f"Sucessfully automated pipeline, output saved to {output_path}")

def run_pipeline():
    try:
        raw_data_path = "raw_input.csv"
        processed_data_path = f"output_{datetime.now().strftime('')}.csv"

        raw_df = extract_data(raw_data_path)

        final_df = (
            raw_df
            .pipe(clean_missing_values)
            .pipe(apply_business_rules)
            .pipe(filter_records)
        )
        load_data(final_df, processed_data_path)

    except Exception as e:
        logging.error(f"Pipeline failed : {str(e)}")

if __name__ == '__main__':
    run_pipeline()
