"""data_engineering  pipeline definition."""

from kedro.pipeline import Pipeline, node, pipeline
from housing_prices.pipelines.data_engineering.data_cleaning import data_cleaning

def create_pipeline(**kwargs) -> Pipeline:  
    """Data Engineering pipeline"""
    return pipeline(
        [
            node(
                func=data_cleaning,
                inputs=[
                    "melb_housing@csv",
                ],
                outputs="melb_housing_clean@csv",
                name="melb_housing_data_cleaning",
                tags=["primary", "cleaning"],
            ),
        ]
    )