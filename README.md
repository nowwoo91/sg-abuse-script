# How To Use

**run script**

python abuselpdb.py -f $csv_filepath
(example) python abuselpdb.py -f report_ip_test.csv

(default csv path) report_ip.csv 

**ABUSED API KEY and Userid**

api_key is embedded in code

user_id is embedded in code (default sg_cert)

**if script can't run**

pip install -r requirements.txt

sudo pip install -r requirements.txt

#### report category table
id | title | description
--- | --- | ---
3 	| Fraud Orders 	|Fraudulent orders.
4 	|DDoS Attack 	|Participating in distributed denial-of-service (usually part of botnet).
9 	|Open Proxy 	|Open proxy, open relay, or Tor exit node.
10 	|Web Spam 	|Comment/forum spam, HTTP referer spam, or other CMS spam.
11 	|Email Spam 	|Spam email content, infected attachments, phishing emails, and spoofed senders (typically via exploited host or SMTP server abuse). Note: Limit comments to only relevent information (instead of log dumps) and be sure to remove PII if you want to remain anonymous.
14 	|Port Scan 	|Scanning for open ports and vulnerable services.
18 	|Brute-Force 	|Credential brute-force attacks on webpage logins and services like SSH, FTP, SIP, SMTP, RDP, etc. This category is seperate from DDoS attacks.
19 	|Bad Web Bot 	|Webpage scraping (for email addresses, content, etc) and crawlers that do not honor robots.txt. Excessive requests and user agent spoofing can also be reported here.
20 	|Exploited Host 	|Host is likely infected with malware and being used for other attacks or to host malicious content. The host owner may not be aware of the compromise. This category is often used in combination with other attack categories.
21 	|Web App Attack 	|Attempts to probe for or exploit installed web applications such as a CMS like WordPress/Drupal, e-commerce solutions, forum software, phpMyAdmin and various other software plugins/solutions.
22 	|SSH 	|Secure Shell (SSH) abuse. Use this category in combination with more specific categories.
23 	|IoT Targeted 	|Abuse was targeted at an "Internet of Things" type device. Include information about what type of device was targeted in the comments. 


## Using CSV 

default(blank) category = all

default(black) comment = sg_cert_report

ip(require) | category(not require) | comment(not require)
--- | --- | ---
1.1.1.1 | 3,5,12 | comment1
2.2.2.2 | DDOS Attack,Email Spam | comment2
3.3.3.3 | |
4.4.4.4 | | comment3
5.5.5.5 | SSH,5 |