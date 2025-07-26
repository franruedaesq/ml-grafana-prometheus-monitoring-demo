# Script to detect concept drift based on model performance (MSE)
from sklearn.metrics import mean_squared_error
import numpy as np

def detect_concept_drift(
    model_pipeline, X_reference, y_reference, X_current, y_current, threshold=0.1
):
    """
    Detects concept drift by comparing model performance (MSE) on reference and current data.
    Returns whether drift is detected and the relative performance decrease.
    """
    # Predict on reference and current data
    y_pred_reference = model_pipeline.predict(X_reference)
    y_pred_current = model_pipeline.predict(X_current)

    # Calculate MSE for both periods
    mse_reference = mean_squared_error(y_reference, y_pred_reference)
    mse_current = mean_squared_error(y_current, y_pred_current)
    
    # Compute relative performance decrease
    relative_performance_decrease = (mse_current - mse_reference) / mse_reference
    is_drift = relative_performance_decrease > threshold
    return is_drift, relative_performance_decrease