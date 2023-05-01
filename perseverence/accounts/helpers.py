from django.conf import settings
import random
import requests


def send_otp_to_phone(phone_number):
    try:
        otp: random.randint(1000, 9999)
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}/OTP'
        response = requests.get(url)
        print(response)
        return otp
    except Exception as e:
        pass
