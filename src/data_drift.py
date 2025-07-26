
 # Script to detect data drift using the Kolmogorov-Smirnov (KS) statistical test
import numpy as np
from scipy.stats import ks_2samp

def detect_data_drift(reference_data, current_data, threshold=0.1):
    """
    Detects data drift between two datasets using the KS test.
    Returns whether drift is detected, the scores per column, and the overall score.
    """
    drift_scores = {}
    for column in reference_data.columns:
        # Compute the KS statistic for each column
        ks_statistic, p_value = ks_2samp(reference_data[column], current_data[column])
        drift_scores[column] = ks_statistic
        
    # Compute the overall drift score
    overall_drift_score = np.mean(list(drift_scores.values()))
    is_drift = overall_drift_score > threshold
    return is_drift, drift_scores, overall_drift_score