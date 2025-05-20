from celery import shared_task
import time
import flask_excel
from models import db, Campaign, Transactions
from Celery.mailer import send_email, send_emailreport, email_report_helper
from flask import render_template

@shared_task(ignore_result=False)
def add(x, y):
    time.sleep(10)
    return x + y

@shared_task(ignore_result=False)
def createcsvcampaign(id):
    filename = f'campaigns_{id}.csv'
    campaigns = Campaign.query.filter_by(sponsor_id = id).all()
    columns_name = [column.name for column in Campaign.__table__.columns]
    print(columns_name)
    csv_out = flask_excel.make_response_from_query_sets(campaigns, columns_name , file_type="csv")
    print(csv_out)

    with open(f'./Celery/userdownloads/{filename}', 'wb') as file:
        file.write(csv_out.data)
    return filename

@shared_task(ignore_result=False)
def createcsvtransaction(id):
    filename = f'transactions_{id}.csv'
    transactions = Transactions.query.filter_by(user_id = id).all()
    columns_name = [column.name for column in Transactions.__table__.columns]
    print(columns_name)
    csv_out = flask_excel.make_response_from_query_sets(transactions, columns_name , file_type="csv")
    print(csv_out)

    with open(f'./Celery/userdownloads/{filename}', 'wb') as file:
        file.write(csv_out.data)
    return filename

@shared_task(ignore_result=True)
def dailyremainder(to, subject, content):
    send_email(to, subject, content)

@shared_task(ignore_result=True)
def monthlyreport():
    email_report_helper()
    print("Monthly report sent")
   