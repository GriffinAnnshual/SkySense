from django .conf import settings
import json
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.contrib.auth.models import User
from whatsapp_bot.models import Profile
from twilio.rest import Client
from whatsapp_bot.views import datas,alerts


def scheduler_api():
    print("done")

def whatsapp_message():
    users = list(User.objects.all())
    for user in users:
        profile=Profile.objects.get(user_id=user.id)
        print(profile.user)
        first=datas(user)
        print(first)
        x=first[0]
        mes=alerts(x)
        try:
            if profile.sms_enabled:
                
                account_sid = 'ACab0736136e82a45256bdb3e56ee9a20d'
                auth_token = '3fa3dd0f864aeaeead60737316c6f423'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                from_='+18145262902',
                body="""Hello! This is Sky Sense, your trusted weather companion.\n🌤️ Weather Forecast for Today - {} 🌤️""".format(str(profile.landmark))+str(mes),
                to='+91'+str(profile.phone_no)
                )

                print(message.sid)
        except:
            print(f'user is not enabled for sms services {profile.user}')

        # from twilio.rest import Client

        account_sid = 'ACab0736136e82a45256bdb3e56ee9a20d'
        auth_token = '3fa3dd0f864aeaeead60737316c6f423'
        client = Client(account_sid, auth_token)

        client.messages.create(
        from_='whatsapp:+14155238886',
        body="""Hello! This is Sky Sense, your trusted weather companion.\n🌤️ Weather Forecast for Today - {} 🌤️""".format(str(profile.landmark))+str(mes),
        to='whatsapp:+91'+str(profile.phone_no)
        )

