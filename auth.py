import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cosmo_compatibility')
TOTAL_QUESTIONS = 10

def update_worksheet(sign, hits):
    worksheet = SHEET.worksheet('sumary')

    cell = worksheet.find(sign)

    # update cell player
    number_of_people = cell.col + 1
    old_player_value = worksheet.cell(cell.row, number_of_people).value
    new_player_value = int(old_player_value) + 1
    worksheet.update_cell(cell.row, number_of_people, str(new_player_value))

    # update cell hits
    hits = cell.col + 2
    old_hit_value = worksheet.cell(cell.row, hits).value
    new_hit_value = int(old_hit_value) + hits
    worksheet.update_cell(cell.row, hits, str(new_hit_value))

    # calc compatibility
    compatibility = cell.col + 3
    perc = new_hit_value / (new_player_value * TOTAL_QUESTIONS) * 100
    worksheet.update_cell(cell.row, compatibility, round(perc, 2))


# call
update_worksheet("Aries", 7)