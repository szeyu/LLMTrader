import pandas as pd
import torch
import numpy as np
import matplotlib.pyplot as plt
from chronos import ChronosPipeline

class ChronosEngine:
    def __init__(self, model_name):
        self.model_name = model_name
        self.pipeline = ChronosPipeline.from_pretrained(
            self.model_name,
            device_map="cpu",
            torch_dtype=torch.bfloat16,
        )

    def predict(self, df, column_name="closed price", prediction_length=12, num_samples=20):
        # Convert the specified column to a tensor
        context = torch.tensor(df[column_name].values)

        # Make prediction
        forecast = self.pipeline.predict(
            context=context,
            prediction_length=prediction_length,
            num_samples=num_samples,
        )

        return forecast

    @staticmethod
    def print_predict_docstring():
        print(ChronosPipeline.predict.__doc__)
