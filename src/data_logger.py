import pandas as pd
import os


class DataLogger:

    DATA_FILE = "data/agriculture_data.csv"
    MAX_ROWS = 1000

    @classmethod
    def save_data(cls, record):

        new_df = pd.DataFrame([record])

        if os.path.exists(cls.DATA_FILE):

            try:
                old_df = pd.read_csv(cls.DATA_FILE)

                combined = pd.concat(
                    [old_df, new_df],
                    ignore_index=True
                )

            except Exception:
                combined = new_df

        else:
            combined = new_df

        # Keep only latest 1000 records
        if len(combined) > cls.MAX_ROWS:

            combined = combined.iloc[-cls.MAX_ROWS:]

        combined.to_csv(
            cls.DATA_FILE,
            index=False
        )