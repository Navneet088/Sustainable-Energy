
# Sustainable Energy Prediction Pipeline
import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor

MODEL_FILE = "model.pkl"


# Load preprocessed data
df = pd.read_csv("sustainable_energy_preprocessed.csv")


# Define all target columns
target_cols = [
    'Value_co2_emissions_kt_by_country',
    'Renewable energy share in the total final energy consumption (%)',
    'Electricity from renewables (TWh)'
]
num_features = [col for col in df.select_dtypes(include=[np.number]).columns if col not in target_cols]

# Features and targets
X = df[num_features].copy()
y = df[target_cols].copy()


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train or load model
if not os.path.exists(MODEL_FILE):
    print("Training model...")
    model_rf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42))
    model_rf.fit(X_train, y_train)
    joblib.dump(model_rf, MODEL_FILE)
    print("✅ Model trained and saved as 'model.pkl'")
else:
    print("Loading saved model...")
    model_rf = joblib.load(MODEL_FILE)

# Save test features
X_test.to_csv("input.csv", index=False)
print("✅ 'input.csv' saved (test features only).")


# Run inference
print("Running inference...")
predictions = model_rf.predict(X_test)

# Save predictions and actuals for all targets
output_df = X_test.copy()
for i, col in enumerate(target_cols):
    output_df[f'Predicted_{col}'] = predictions[:, i]
    output_df[f'Actual_{col}'] = y_test[col].values
output_df.to_csv("output1.csv", index=False)
print("✅ 'output1.csv' saved (test features + predictions for all targets).")
