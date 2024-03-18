import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from .jobs import scheduler_api,whatsapp_message



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduler_api,'interval',seconds=5)
    target_time = datetime.time(18, 41, 10)
    # Get the current date and time
    now = datetime.datetime.now()
    # Combine the current date and the target time to get the target datetime
    
    target_datetime = datetime.datetime.combine(now.date(), target_time)

    if target_datetime < now:
        target_datetime += datetime.timedelta(days=1)

    # Calculate the delay in seconds until the target time
    delay = (target_datetime - now).total_seconds()


    scheduler.add_job(whatsapp_message, 'date', run_date=target_datetime)
    scheduler.start()