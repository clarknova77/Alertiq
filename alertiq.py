#!/usr/bin/python2.6

import urllib2
unass_tickets = 0
triage_tickets = 0 
details_tickets = 0


unassigned = []
triage = []
details = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# RSS feeds for the data
unass_rss = urllib2.urlopen('https://support.<COMPANY.co.uk/staff/feed/fbfefc5a-18bd-fb3c-239d-e64b1ed3c7a0/7.rss')
details_rss = urllib2.urlopen('https://support.<COMPANY>.co.uk/staff/feed/fbfefc5a-18bd-fb3c-239d-e64b1ed3c7a0/137.rss')
triage_rss = urllib2.urlopen('https://support.<COMPANY>.co.uk/staff/feed/fbfefc5a-18bd-fb3c-239d-e64b1ed3c7a0/140.rss')

unass_qry = unass_rss.read()
details_qry = details_rss.read()
triage_qry = triage_rss.read()

# Check for unassigned tickets
for i in unass_qry.split():
	unassigned.append(i)
for i in unassigned:
    if "<title>" in i:
    	unass_tickets += 1  
if unass_tickets == 2:
	print bcolors.FAIL + "There is", unass_tickets -1, "unassigned ticket." + bcolors.ENDC
elif unass_tickets > 0:
    print bcolors.FAIL + "There are", unass_tickets -1, "unassigned tickets." + bcolors.ENDC



# Check for missing details in tickets
for i in details_qry.split():
	details.append(i)
for i in details:
	if "<title>" in i:
		details_tickets += 1
if details_tickets == 2:
	print bcolors.WARNING + "There is", details_tickets -1, "ticket missing details." + bcolors.ENDC
elif details_tickets > 0:
	print bcolors.WARNING + "There are", details_tickets -1, "ticket missing details." + bcolors.ENDC
elif details_tickets == 1:
	print bcolors.OKBLUE + "There are ", details_tickets -1, "tickets missing details." + bcolors.ENDC

 

# Check for missing details
for i in triage_qry.split():
    triage.append(i)
for i in triage:
	if "<title>" in i:
		triage_tickets += 1
if triage_tickets == 2:
	print bcolors.WARNING + "There is", triage_tickets -1, "ticket in triage." + bcolors.ENDC
elif triage_tickets == 1:
	print bcolors.OKBLUE + "There are", triage_tickets -1, "tickets in triage" + bcolors.ENDC








