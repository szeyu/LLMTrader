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

    def plot_forecast(self, df, forecast, column_name="closed price"):
        forecast_index = range(len(df), len(df) + forecast.shape[2])
        low, median, high = np.quantile(forecast[0].numpy(), [0.1, 0.5, 0.9], axis=0)

        plt.figure(figsize=(12, 6))
        plt.plot(df[column_name], color="royalblue", label="historical data")
        plt.plot(forecast_index, median, color="tomato", label="median forecast")
        plt.fill_between(forecast_index, low, high, color="tomato", alpha=0.3, label="80% prediction interval")
        plt.legend()
        plt.grid()
        plt.title(f"Forecast for {self.model_name}")
        plt.xlabel("Time")
        plt.ylabel(column_name)
        plt.show()

    @staticmethod
    def print_predict_docstring():
        print(ChronosPipeline.predict.__doc__)
