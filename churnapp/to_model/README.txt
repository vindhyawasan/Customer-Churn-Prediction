Customer Churn Prediction - Model Files

1. modelchurn.pkl
This is the trained Machine Learning model used to predict customer churn.
The model predicts whether a customer will churn or not.

2. scaler.pkl
This contains the StandardScaler used during model training.
The same scaler must be used to transform new input data before prediction.

3. columns.pkl
This contains the column names and their order used during model training.
It helps ensure that the input data is provided to the model in the correct order.

Important:
- Do not fit the scaler again when making predictions.
- Use scaler.transform() for new customer data.
- The input column order must match columns.pkl.
