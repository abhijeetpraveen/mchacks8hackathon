from selenium import webdriver
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'memyselfandi7001@gmail.com'
EMAIL_PASSWORD = '*********'

msg = EmailMessage()
msg['Subject'] = '****Important**** Mr. Pennimpede wishes to contact you.'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'abhijeetpraveen@gmail.com'
msg.set_content('''Hello,
                Mr. Pennimpede has asked for you to contact him. Please give him a call as soon as possible.

                Sincerely,
                
                Mr. Thambimuthu''')
                

DRIVER_PATH = '/Users/Abhijeet/Desktop/Liverpool/McHacks/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('file:///Users/Abhijeet/Desktop/Liverpool/McHacks/index.html')

helpstatus = driver.find_element_by_id("needattention")
family_call = driver.find_element_by_id("familycall")

while True:
    try:
        if helpstatus.get_attribute('value') == "1":
            print("THE PATIENT IS IN NEED OF HELP!")
            break
        else:
            print("Patient is fine.")
    except Exception as e:
        pass
    try:
        if family_call.get_attribute('value') == "1":
            print("Patient wants to contact family. Email has been sent to them.")
            print("\n")
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            continue
        else:
            print("Patient does not want to contact family.")
            print("\n")
            continue
    except Exception as e:
        pass
        
        
    i = 0
    while i < 2000000:
        i+=1
    
        
