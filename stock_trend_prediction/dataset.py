from stock_trend_prediction.my_func import Dataset

# Entry point to ensure this block runs only when executed directly
if __name__ == '__main__':
    # Define stock ID to process (can be modified for different stocks)
    stock_id = "POWERGRID.NS"

    # Create an instance of Dataset class and perform a series of data operations
    (
        Dataset(stock_id)  # Initialize a Dataset object by fetching data with the stock id
        .basic_clean()  # Perform basic data cleaning (e.g., remove multi_index, sorting columns)
        .add_missing_dates()  # Add any missing dates to maintain continuity in time series
        .fill_missing_value()  # Fill any missing values using appropriate strategies
        .save_data()  # Save the cleaned and processed data to a file
    )





