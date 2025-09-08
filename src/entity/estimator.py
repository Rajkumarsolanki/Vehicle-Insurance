import sys
from src.logger import logging
from src.exception import MyException
import pandas as pd


class MyModel:
    def __init__(self, bucket_name: str, model_path: str):
        """
        Loads preprocessing object and trained model object from S3
        """
        try:
            from src.configuration.aws_connection import S3Client
            import pickle

            s3 = S3Client()
            model_obj = s3.read_object(bucket_name, model_path, make_readable=False)

            self.model = pickle.loads(model_obj)
            self.preprocessing_object = self.model["preprocessor"]
            self.trained_model_object = self.model["model"]

            logging.info("Model and preprocessor loaded successfully from S3")

        except Exception as e:
            raise MyException(e, sys) from e

    def predict(self, dataframe: pd.DataFrame):
        """
        Perform prediction with preprocessing alignment
        """
        try:
            logging.info("Starting prediction process.")

            # ✅ Ensure all expected columns exist
            if hasattr(self.preprocessing_object, "feature_names_in_"):
                expected_cols = list(self.preprocessing_object.feature_names_in_)

                # Add missing columns with default 0
                for col in expected_cols:
                    if col not in dataframe.columns:
                        dataframe[col] = 0

                # Keep only required columns in right order
                dataframe = dataframe[expected_cols]

            # Step 1: Apply preprocessing
            transformed_feature = self.preprocessing_object.transform(dataframe)

            # Step 2: Model prediction
            logging.info("Using the trained model to get predictions")
            predictions = self.trained_model_object.predict(transformed_feature)

            return predictions

        except Exception as e:
            logging.error("Error occurred in predict method", exc_info=True)
            raise MyException(e, sys) from e
