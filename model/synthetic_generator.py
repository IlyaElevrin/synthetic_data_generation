import pandas as pd
import numpy as np
from sdv.single_table import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata
import warnings

warnings.filterwarnings('ignore')

class SyntheticDataGenerator:
    def __init__(self, model_path=None):
        self.model_path = model_path
        self.model = None
        self.metadata = None
        self.original_columns = []

    def _validate_input(self, data):
        required_columns = ['subject', 'verb', 'object']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"The mandatory column '{col}' is missing from the data")
        self.original_columns = data.columns.tolist()  # preserving the original speakers

    def _generate_dummy_columns(self, data):
        # One-hot for 'verb' and 'object'
        for col in ['verb', 'object']:
            for value in data[col].unique():
                dummy_col = f"{col}_{value}"
                data[dummy_col] = (data[col] == value).astype(int)

        # fictitious numeric columns
        data['amount'] = np.random.uniform(10, 1000, size=len(data))
        data['transaction_id'] = np.arange(len(data))

        # timestamps
        data['timestamp'] = pd.to_datetime('2023-01-01') + pd.to_timedelta(
            np.random.randint(0, 365, len(data)), 'days'
        )

        # masks and flags
        data['is_valid'] = 1
        data['fraud_flag'] = 0

        return data

    def _train_model(self, data, epochs=100):
        self.metadata = SingleTableMetadata()
        self.metadata.detect_from_dataframe(data)
        self.model = CTGANSynthesizer(self.metadata, epochs=epochs)
        self.model.fit(data)

        if self.model_path:
            self.model.save(self.model_path)

    def generate(self, input_data, num_rows=100, retrain_on_error=True):
        try:
            self._validate_input(input_data)
            enriched_data = self._generate_dummy_columns(input_data.copy())

            if not self.model:
                if self.model_path:
                    self.model = CTGANSynthesizer.load(self.model_path)
                else:
                    self._train_model(enriched_data)

            synthetic_data = self.model.sample(num_rows=num_rows)

            # restore original values from one-hot
            for col_type in ['verb', 'object']:
                for col in synthetic_data.columns:
                    if col.startswith(f"{col_type}_"):
                        mask = synthetic_data[col] == 1
                        synthetic_data.loc[mask, col_type] = col.replace(f"{col_type}_", "")

            # filtering of source columns only
            result = synthetic_data[self.original_columns].copy()

            return result

        except Exception as e:
            if retrain_on_error:
                print(f"Error: {str(e)}\nBegin retraining the model...")
                self._train_model(enriched_data)
                return self.generate(input_data, num_rows, retrain_on_error=False)
            else:
                raise RuntimeError("Failed to generate data after retraining")