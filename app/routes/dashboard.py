from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import requests
import os

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        api_key = os.getenv('WEATHER_API_KEY')

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'

        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
        else:
            error = 'Cidade não encontrada. Tente novamente.'

    return render_template('dashboard.html', user=current_user, weather=weather_data, error=error)
