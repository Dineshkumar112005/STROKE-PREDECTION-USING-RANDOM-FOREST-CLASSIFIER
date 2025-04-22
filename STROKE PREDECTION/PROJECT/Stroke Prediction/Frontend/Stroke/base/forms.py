from django import forms

class StrokePredictionForm(forms.Form):
    gender = forms.ChoiceField(choices=[(0, 'Male'), (1, 'Female')], label='Gender')
    age = forms.FloatField(label='Age', min_value=0)
    hypertension = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Hypertension')
    heart_disease = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Heart Disease')
    ever_married = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Ever Married')
    work_type = forms.ChoiceField(
        choices=[(0, 'Children'), (1, 'Govt Job'), (2, 'Never Worked'), (3, 'Private'), (4, 'Self-employed')],
        label='Work Type'
    )
    residence_type = forms.ChoiceField(choices=[(0, 'Urban'), (1, 'Rural')], label='Residence Type')
    avg_glucose_level = forms.FloatField(label='Average Glucose Level', min_value=0)
    bmi = forms.FloatField(label='BMI', min_value=0)
    smoking_status = forms.ChoiceField(
        choices=[(0, 'Never Smoked'), (1, 'Formerly Smoked'), (2, 'Smokes'), (3, 'Unknown')],
        label='Smoking Status'
    )
