SENDMAIL = "/usr/sbin/sendmail" # sendmail location
FROM = "jpl_team@sdfds.com"
TO = ["maziyar_b4@yahoo.com"] # must be a list

SUBJECT = "finally!3"

TEXT ="Sinceresdfsdfly, JPL Team."

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

import os

p = os.popen("%s -t -i" % SENDMAIL, "w")
p.write(message)
status = p.close()
if status:
    print "Sendmail exit status", status  