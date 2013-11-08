EmailScheduler
==============

Python script to automatically send emails at designated intervals.


Install
=============
Install python-crontab:
```
sudo easy__install python-crontab
```
or
```
sudo pip python__crontab
```

Copy or rename CONFIG.public to CONFIG.private. Modify the fields for your own email account:\
from_email: the email address that sends all of the emails
username: the username for whatever email server you're using (if you are using a Gmail account, this is the same as from_email)
password: the password for the email server
mail_server: the smtp address. If you're using Gmail, you don't have to change this.
send_times: the times (in hours, military time) that you want emails to be sent. The sample config sends emails at 8:00AM and 8:00PM
email_schedule: the name of the text file containing your schedule. Unless you want to rename schedule.txt, you don't have to change this.
receiver_domain_name: if schedule.txt does not include full email addresses, this will be appended to every receiver in the schedule.
msg_text: the text of the message to be sent
msg_subject: subject line for the message

Modify schedule.txt. It expects information in the same format: "mm/dd	email"

Once you have updated CONFIG.private and schedule.txt, run install.py. Everything has been copied to /usr/local/bin/send__email. To update the schedule in the future, you should modify /usr/local/bin/send__email/schedule.txt