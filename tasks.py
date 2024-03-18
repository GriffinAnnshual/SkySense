from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.contrib.auth.models import User
from .models import Profile
from twilio.rest import Client
from .views import datas,alerts

def whatsapp_message():
    users = list(User.objects.all())
    for user in users:
        profile=Profile.objects.get(user_id=user.id)
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
            print(f'failed to send sms for user {profile.user}')

        try:

            account_sid = 'ACab0736136e82a45256bdb3e56ee9a20d'
            auth_token = '3fa3dd0f864aeaeead60737316c6f423'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
            from_='whatsapp:+14155238886',
            body="""Hello! This is Sky Sense, your trusted weather companion.\n🌤️ Weather Forecast for Today - {} 🌤️""".format(str(profile.landmark))+str(mes),
            to='whatsapp:+91'+str(profile.phone_no)
            )

        except:
            print(f'failer to send whatsapp message for user {profile.user}')

            







def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(whatsapp_message, 'cron', hour=0,minute=9,second=10)

    scheduler.start()

    try:
        # This is an infinite loop, which keeps the main thread alive.
        # It is required as the scheduler runs in the background as a separate thread.
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()