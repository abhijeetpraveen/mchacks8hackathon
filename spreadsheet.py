import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from bs4 import BeautifulSoup

with open('index.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h1')
    level = tags[0].text[1:]
    bed = tags[1].text
        
    
    


pp = pprint.PrettyPrinter()
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('McHacksHackathon.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Patient#123').sheet1
index = 2
while True:
    print(level)
    print(bed)
    print("Hello Nurse, Please enter what you wish to do?")
    print('''Type "Entry" to enter an event for your patient, enter data (fields separated by commas: date,time,event,specifications,status''')
    print('''Type "Incomplete" to take a look at incomplete events''')
    print('''Type "Complete" to take a look at complete events''')
    print('''Type "Change" to change an incomplete event to a complete event''')
    first_input = input("Select your option: ")
    if first_input == "Entry":
        while True:
            second_input = input("Input the data you want to enter or 'done' to finish: ")
            if second_input == 'done':
                break
            else:
                data = second_input.split(",")
                sheet.insert_row(data,index)
                index += 1
    if first_input == "Incomplete":
        incomplete_events = []
        for row in range(2,index):
            if sheet.cell(row,5).value == "Incomplete":
                incomplete_events.append(sheet.row_values(row))
        pp.pprint(incomplete_events)
    if first_input == "Complete":
        complete_events = []
        for row in range(2,index):
            if sheet.cell(row,5).value == "Complete":
                complete_events.append(sheet.row_values(row))
        pp.pprint(complete_events)
    if first_input == "Change":
        event = input("Enter the event you wish to change the status of ")
        for row in range(2,index):
            if sheet.cell(row,3).value == event:
                sheet.update_cell(row,5,"Complete")

        
