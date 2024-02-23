""" Functions to clean data for modeling """\

from typing import List, Any
import pandas as pd

def data_cleaning(model_df : pd.DataFrame) -> pd.DataFrame:
    """ 
    """
    # Conversion of selected set of columns to Int64
    columns_to_int = ['Price', 'Bedroom2', 'Bathroom', 'Car', 'YearBuilt', 'Landsize']

    for column in columns_to_int:
        model_df[column] = model_df[column].astype('Int64')

    # Date conversion
    model_df['Date'] = pd.to_datetime(model_df['Date'], dayfirst=True)

    # Conversion of columns to CAPS
    model_df.columns = [col.upper() for col in model_df.columns]

    return model_df