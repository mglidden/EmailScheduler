#/usr/bin/python

from crontab import CronTab
import json
import os
from shutil import copyfile

install_dir = '/usr/local/bin/send_email'
config = json.loads(open('CONFIG.private').read())

# Installing the script to /usr/local/bin/send_email
if os.path.exists(install_dir):
  print 'Install directory already existed.'
else:
  os.makedirs(install_dir)

files_to_install = ['send_email.py', 'crontab.py', 'CONFIG.private']
for filename in files_to_install:
  copyfile(filename, '%s/%s' % (install_dir, filename))

cron = CronTab()

cmd = 'python %s/send_email' % (install_dir)
for old_job in cron.find_command(cmd):
  cron.remove(old_job)

job = cron.new(command='python %s/send_email.py' % (install_dir))
job.enable()
#job.minute.on(0)
#for hour in config['send_times']:
#  job.hour.also.on(hour)

cron.write()
