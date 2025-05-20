from celery.schedules import crontab
from flask import current_app as app, render_template

from Celery.tasks import dailyremainder, monthlyreport
from models import db, user_datastore, User, Campaign, Adrequest, Role, RolesUsers, Ad, Transactions
import datetime
from jinja2 import Environment, FileSystemLoader
import pdfkit


celery_app = app.extensions["celery"]

def influencerremainder(sender):
    users = User.query.all()
    for user in users:
        if user.roles[0].name == 'Influencer':
                        if user.last_login_at == None or (datetime.now() - user.last_login_at).days>=2:
                                sender.add_periodic_task(30.0, dailyremainder.s(user.email,'We Miss Your Presence! Discover What\'s New',f'''
                                                                                                          <div style="width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden;">
                                                                                                            <div style="background-color: #009688; color: #ffffff; padding: 20px; text-align: center;">
                                                                                                                <h1>We Miss You!</h1>
                                                                                                            </div>
                                                                                                            <div style="padding: 20px;"> 
                                                                                                                <p>Hi <b>{user.name}</b>,</p>
                                                                                                                <p>We noticed that you haven't logged into your account for a couple of days. We hope everything is okay. We've missed you and there's so much happening on our platform that we don't want you to miss out!</p>
                                                                                                                <p>Check out the new campaigns and ad requests waiting for you. There's always something exciting happening!</p>
                                                                                                                <p>If you have any questions or need any assistance, feel free to reach out to our support team.</p>
                                                                                                                <p>Best regards,<br>CreativeMerge</p>
                                                                                                            </div>
                                                                                                            <div style="background-color: #009688; color: #ffffff; text-align: center; padding: 10px; font-size: 12px;">
                                                                                                                <p>&copy; 2024 CreativeMerge. All rights reserved.</p>
                                                                                                            </div>
                                                                                                        </div>'''), name = 'DailyLoginInfluReminder')
                        adrequests = Adrequest.query.filter_by(user_id=user.id).all()
                        x=[]
                        for adrequest in adrequests:
                                if adrequest.status == 'Requested' or adrequest.status=='InProgress':
                                        x.append(adrequest)
                        if len(x)>0:     
                            #crontab(hour=23,minute=3)
                            sender.add_periodic_task(30.0,dailyremainder.s(user.email,"New Ad Requests Awaiting Your Attention!",
                                                                                                            f'''<div style="width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden;">
                                                                                                                <div style="background-color: #009688; color: #ffffff; padding: 20px; text-align: center;">
                                                                                                                    <h1>Pending Ad Requests Await!</h1>
                                                                                                                </div>
                                                                                                                <div style="padding: 20px;">
                                                                                                                    <p>Hi <b>{user.name}</b>,</p>
                                                                                                                    <p>We noticed that you have some ad requests pending review. These are valuable opportunities that we don't want you to miss out on!</p>
                                                                                                                    <p>Please log in to your account to review and respond to these ad requests.</p>
                                                                                                                    <p>If you have any questions or need any assistance, our support team is here to help.</p>
                                                                                                                    <p>Best regards,<br>CreativeMerge</p>
                                                                                                                </div>
                                                                                                                <div style="background-color: #009688; color: #ffffff; text-align: center; padding: 10px; font-size: 12px;">
                                                                                                                    <p>&copy; 2024 CreativeMerge. All rights reserved.</p>
                                                                                                                </div>
                                                                                                            </div>''' ), name='DailyRequestInfluReminder')
    

                                

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    #sender.add_periodic_task(10.0, test.s('hello'))
    #sender.add_periodic_task(10.0, dailyremainder.s('Teacher@creative','remainder to login','<h1> Login to Site</h1>'))
    
    # Daily Remainder
    #sender.add_periodic_task(crontab(hour=18,minute=41), dailyremainder.s('Student@creative','remainder to login','<h1> Login to Site at 6</h1>'), name = 'DailyReminder')
   
    # Weekly Remainder
    #sender.add_periodic_task(crontab(hour=18,minute=41, day_of_week='Monday'), dailyremainder.s('Student@creative','remainder to login','<h1> Login to Site at 6</h1>'), name = 'WeeklyReminder')
    
    # Checking if a user logged in or not / has a incomplete request
    influencerremainder(sender)
   
    # Sending Monthly Report
   
    sender.add_periodic_task(10.0,monthlyreport.s(),name='MonthlyReport')
    #sender.add_periodic_task(crontab(hour=23,minute=12),monthlyreport.s(),name='MonthlyReport')

 