# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.base import JobLookupError
# from django_apscheduler.jobstores import DjangoJobStore

# def clear_jobs():
#     scheduler = BackgroundScheduler()
#     scheduler.add_jobstore(DjangoJobStore(),"default")

#     try:
#         # Remove all jobs from the JobStore
#         scheduler.remove_all_jobs()
#     except JobLookupError:
#         pass  # Ignore the error if there are no jobs in the JobStore

#     scheduler.shutdown()

# if __name__ == '__main__':
#     clear_jobs()
