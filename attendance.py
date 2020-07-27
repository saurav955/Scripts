import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/saurav/attendance/firstproject-dfdfdf904a87.json', scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/sdfsdfwerqwerqwerffasdssdfdfdfdfdfdfdfdfdfdf/edit#gid=1123412341234') #url of the google sheet.
worksheet = sheet.worksheet("Saurav Sharma")  #'Saurav Sharma' is the name of the sub-sheet.
next_row_count = next_available_row(worksheet)
today = date.today()
d = today.strftime("%b-%d-%Y")
cell = worksheet.findall(d)

if cell:
 print("Today's entry already exists")
else:
 previous_row_count = int(next_row_count)-1
 val1 = worksheet.cell(previous_row_count, 5).value   #5 is the column number.
 val2 = worksheet.cell(previous_row_count, 6).value
 val3 = worksheet.cell(previous_row_count, 9).value
 worksheet.update_cell(next_row_count, 1, next_row_count)
 worksheet.update_cell(next_row_count, 2, d)
 worksheet.update_cell(next_row_count, 5, val1)
 worksheet.update_cell(next_row_count, 6, val2)
 worksheet.update_cell(next_row_count, 9, val3)

