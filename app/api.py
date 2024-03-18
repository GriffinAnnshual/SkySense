from geopy.geocoders import Nominatim
import geocoder
def get_user_location():
    g = geocoder.ip('me')
    latitude = g.latlng[0]
    longitude = g.latlng[1]
    print(latitude, longitude)

get_user_location()









    # from twilio.rest import Client


    # account_sid = 'ACab0736136e82a45256bdb3e56ee9a20d'
    # auth_token = '3fa3dd0f864aeaeead60737316c6f423'
    # client = Client(account_sid, auth_token)

    # phone_number = '+1234567890'

    # twilio_phone_number = "+14155238886"

    # new_phone_number = client.incoming_phone_numbers.create(
    #     phone_number=phone_number,
    #     sms_url='https://example.com/sms',
    #     sms_method='POST'
    # )