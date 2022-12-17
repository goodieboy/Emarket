from django.conf import settings
import requests


class Flutterwave:
    FLUTTERWAVE_SECRET_KEY = settings.FLUTTERWAVE_SECRET_KEY
    base_url = 'https://api.flutterwave.com'

    def payment_verification(self, transaction_id, *args, **kwargs):
        path = f'/v3/transactions/{transaction_id}/verify'

        headers = {
            'Authorization': f'Bearer {self.FLUTTERWAVE_SECRET_KEY}',
            'Content-Type': 'application/json',
        }
        url = self.base_url + path
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data['status'], response_data['message']
