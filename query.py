# IMPORTANT NOTE: set the following environment variables:
# PAPERTRAIL_TOKEN, SMTP_HOST, SMTP_USER, SMTP_PASS
# EMAIL_FROM, EMAIL_TO

import httplib, urllib, time, os, json

INTERVAL = 10 * 60


conn = httplib.HTTPSConnection(host = 'papertrailapp.com')
conn.request(
    method = 'GET',
    url = '/api/v1/events/search.json?' + urllib.urlencode({
        'min_time' : str(int(time.time() - INTERVAL))
    }),
    headers = {
        'X-Papertrail-Token' : os.environ['PAPERTRAIL_TOKEN']
    }
)
response = conn.getresponse()

events_no = len(json.loads(response.read())['events'])

if events_no < 1:
    import smtplib
    from email.mime.text import MIMEText

    s = smtplib.SMTP(os.environ['SMTP_HOST'])
    s.login(os.environ['SMTP_USER'], os.environ['SMTP_PASS'])

    msg = MIMEText('Your host stopped calling home!\nTested at: '+time.ctime())
    msg['Subject'] = 'Your host stopped calling home!'
    msg['From'] = os.environ['EMAIL_FROM']
    msg['To'] = os.environ['EMAIL_TO']
    s.sendmail(os.environ['EMAIL_FROM'], [os.environ['EMAIL_TO']], msg.as_string())
    print "message sent"
else:
    print "OK"

