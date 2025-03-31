import yfinance as yf
import datetime as dt
import numpy as np
import pandas as pd
import os


class Dataset:
    def __init__(self,stock_id):
        start_time = dt.datetime(2020, 1, 1)
        end_time = dt.datetime.now()

        self.dataset = yf.download(stock_id, start_time, end_time)

    def basic_clean(self):
        df_ = (self.dataset.reset_index()
                .copy())
        df_.columns = [col for col, ticker in df_.columns.values]
        self.dataset = df_.rename(columns=lambda x: x.lower())
        return self

    def add_missing_dates(self):
        first_date = self.dataset["date"].min()
        last_date = self.dataset["date"].max()
        # Create date range and convert to DataFrame
        date_range = pd.date_range(start=first_date, end=last_date, freq="D").to_frame(index=False, name="date")
        # Merge with the original DataFrame to include all dates
        df_ = self.dataset.merge(date_range, how="right", on="date").reset_index(drop=True).copy()
        df_["day"] = df_["date"].dt.day_name()
        self.dataset = df_[~df_["day"].isin(["Saturday", "Sunday"])].drop(columns="day").reset_index(drop=True).copy()
        return self

    def fill_missing_value(self):
        self.dataset = self.dataset.copy().ffill()
        return self

    def save_data(self):
        self.dataset.to_csv(os.path.join(os.getcwd(), "data", "interim", "data.csv"),index=False)

