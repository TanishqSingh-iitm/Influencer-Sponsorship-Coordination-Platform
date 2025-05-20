import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import render_template
import pdfkit
from weasyprint import HTML


SMTP_SERVER = 'localhost'
SMTP_PORT = 1025
SENDER_EMAIL = 'no-reply@CreativeMerge.com'
SENDER_PASSWORD = ''

def send_email(to, subject, content):

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'html'))

    with smtplib.SMTP(host=SMTP_SERVER,port=SMTP_PORT) as client:
        client.send_message(msg)
        client.quit()


#send_email('Hello@example','Test Email', '<h1>Hello</h1>')

from models import User, Campaign, Ad, Transactions

def get_sponsor_data(): 
    sponsors = User.query.all() 
    sponsor_data = [] 
    for sponsor in sponsors: 
        if sponsor.roles[0].name == 'Sponsor': 
            campaigns = [] 
            ads = [] 
            trans = [] 
            campaignss = Campaign.query.filter_by(sponsor_id=sponsor.id).all() 
            for campaign in campaignss: 
                campaigns.append(campaign.formatter()) 
                adss = Ad.query.filter_by(campaign_id=campaign.id).all() 
                for ad in adss: 
                    ads.append(ad.formatter()) 
            transactions = Transactions.query.filter_by(user_id=sponsor.id).all() 
            for transaction in transactions: 
                trans.append(transaction.formatter()) 
            sponsor_data.append({ 'sponsorname': sponsor.name, 'campaigns': campaigns, 'ads': ads, 'transactions': trans, 'email': sponsor.email, 'subject': f'{sponsor.name}\'s Monthly Report' }) 
    return sponsor_data



def email_report_helper():
    sponsor_data = get_sponsor_data()
    for sponsor in sponsor_data:
        send_emailreport(sponsor['email'], sponsor['subject'], sponsor['sponsorname'], sponsor['campaigns'], sponsor['ads'], sponsor['transactions'])


def send_emailreport(to, subject, sponsorname, campaigns, ads, transactions):
    rendered = render_template('template.html',sponsorname=sponsorname, campaigns=campaigns, ads=ads, transactions=transactions)
    HTML(string=rendered).write_pdf('output.pdf')
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(rendered, 'html'))

    with smtplib.SMTP(host=SMTP_SERVER,port=SMTP_PORT) as client:
        client.send_message(msg)
        client.quit()