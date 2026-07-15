from bs4 import BeautifulSoup
import re

html = '''
<html>
<body>
    <p>Contact admin@securesite.com for help</p>
    <p>User: john_doe logged in from 192.168.1.1</p>
    <p>User: jane_smith logged in from 10.0.0.5</p>
    <p>Alert: admin@securesite.com flagged 192.168.1.2</p>
    <p>User: h4cker_99 logged in from 172.16.0.1</p>
    <p>Contact support@securesite.com for issues</p>
</body>
</html>
'''

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()

emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)
users = re.findall(r'User:\s*(\w+)', text)
ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)

print("📧 Emails found:")
for email in set(emails):
    print(f"  → {email}")

print("\n👤 Usernames found:")
for user in users:
    print(f"  → {user}")

print("\n🌐 IPs found:")
for ip in ips:
    print(f"  → {ip}")