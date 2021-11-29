import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender_email = input("What is your email?\n")
password = input("Type your password and press enter: \n")

subject = "Internship Opportunity Search"

f = open("template.txt", "rt")
draft_body = f.read()


company_list = open("companies_list.txt")

companies = []
emails = []


for line in company_list:
    company_information = line.strip().split()
    companies.append(company_information[0])
    emails.append(company_information[1])

print(companies)
print(emails)

resume_name = "resume.pdf"
project_name = "project.pdf"

with open(resume_name, "rb") as attachment:
    resume = MIMEBase("application", "octet-stream")
    resume.set_payload(attachment.read())

with open(project_name, "rb") as attachment:
    project = MIMEBase("application", "octet-stream")
    project.set_payload(attachment.read())

# Encode files in ASCII characters to send by email
encoders.encode_base64(resume)
encoders.encode_base64(project)

# Add header as key/value pair to attachment part
resume.add_header(
    "Content-Disposition",
    f"attachment; filename= {resume_name}",
)

project.add_header(
    "Content-Disposition",
    f"attachment; filename= {project_name}",
)

# Create a multipart message and set headers
def send_the_email(name_of_company, receiver_email, resume_part, project_part , draft_body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    body = draft_body.replace( "CompanyName" , name_of_company)
    message.attach(MIMEText(body, "markdown"))

    # Add attachment to message and convert message to string
    message.attach(resume_part)
    message.attach(project_part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

for index in range(len(companies)):
    send_the_email(companies[index], emails[index], resume, project, draft_body)
