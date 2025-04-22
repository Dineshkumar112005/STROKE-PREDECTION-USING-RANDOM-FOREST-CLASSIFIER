from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
import joblib
from .forms import StrokePredictionForm

# Home Page
def HomePage(request):
    return render(request, 'home.html')

# Portfolio Page
def PortfolioPage(request):
    return render(request, 'portfolio.html')

# Signup Page
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

# Demo Page
def demo_view(request):
    return render(request, 'demo.html')

# About Page
def about_view(request):
    return render(request, 'about.html')

# Login Page
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!")

    return render(request, 'login.html')

# Logout Page
def LogoutPage(request):
    logout(request)
    return redirect('home')

# Stroke Prediction Index Page
@login_required(login_url='login')
def index(request):
    """
    This view handles stroke prediction input and displays the result.
    """
    if request.method == 'POST':
        form = StrokePredictionForm(request.POST)

        if form.is_valid():
            # Extract the cleaned data from the form
            input_data = {
                "gender": float(form.cleaned_data['gender']),
                "age": float(form.cleaned_data['age']),
                "hypertension": float(form.cleaned_data['hypertension']),
                "heart_disease": float(form.cleaned_data['heart_disease']),
                "ever_married": float(form.cleaned_data['ever_married']),
                "work_type": float(form.cleaned_data['work_type']),
                "Residence_type": float(form.cleaned_data['residence_type']),
                "avg_glucose_level": float(form.cleaned_data['avg_glucose_level']),
                "bmi": float(form.cleaned_data['bmi']),
                "smoking_status": float(form.cleaned_data['smoking_status']),
            }

            # Convert input data into a pandas DataFrame
            input_df = pd.DataFrame([input_data])

            try:
                # Load the model
                rf_model_loaded = joblib.load('random_forest_model.pkl')

                # Make the prediction
                prediction = rf_model_loaded.predict(input_df)

                # Determine the result message
                if prediction == 1:
                    result_message = "The person has had a stroke."
                else:
                    result_message = "The person has not had a stroke."
            except Exception as e:
                result_message = f"Error occurred during prediction: {str(e)}"

            # Pass the prediction and the form back to the result page
            return render(request, 'result.html', {'result': result_message, 'form': form})
    else:
        form = StrokePredictionForm()

    return render(request, 'index.html', {'form': form})

# Result Page
def result(request):
    """
    This view is responsible for displaying the result of the prediction.
    """
    return render(request, 'result.html')
