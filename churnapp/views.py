from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(
    BASE_DIR,
    'churnapp',
    'to_model',
    'modelchurn.pkl'
)

scaler_path = os.path.join(
    BASE_DIR,
    'churnapp',
    'to_model',
    'scaler.pkl'
    )

columns_path = os.path.join(
    BASE_DIR,
    'churnapp',
    'to_model',
    'columns.pkl'
    )

prediction = None
columns = joblib.load(columns_path)
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# print(columns)


def index(request):

    prediction = None

    if request.method == "POST":

        gender = request.POST.get('gender')
        SeniorCitizen = request.POST.get('SeniorCitizen')
        Partner = request.POST.get('Partner')
        tenure = request.POST.get('tenure')
        PhoneService = request.POST.get('PhoneService')
        InternetService = request.POST.get('InternetService')
        Contract = request.POST.get('Contract')
        PaperlessBilling = request.POST.get('PaperlessBilling')
        PaymentMethod = request.POST.get('PaymentMethod')
        MonthlyCharges = request.POST.get('MonthlyCharges')

        input_data = pd.DataFrame([[
            gender,
            SeniorCitizen,
            Partner,
            tenure,
            PhoneService,
            InternetService,
            Contract,
            PaperlessBilling,
            PaymentMethod,
            MonthlyCharges
        ]], columns=columns)

        input_data = input_data.astype(float)

        input_scaled = scaler.transform(input_data)

        # Model directly returns Yes or No
        prediction = model.predict(input_scaled)[0]

        print("Prediction:", prediction)

    return render(request, 'churn/index.html', {
        'prediction': prediction
    })