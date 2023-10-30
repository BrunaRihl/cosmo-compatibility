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
WORKSHEET = SHEET.worksheet('sumary')

def update_worksheet(sign, hits):
    cell = WORKSHEET.find(sign)

    # update cell player
    number_of_people = cell.col + 1
    old_player_value = WORKSHEET.cell(cell.row, number_of_people).value
    new_player_value = int(old_player_value) + 1
    WORKSHEET.update_cell(cell.row, number_of_people, str(new_player_value))

    # update cell hits column
    hits_col = cell.col + 2
    old_hit_value = WORKSHEET.cell(cell.row, hits_col).value
    new_hit_value = int(old_hit_value) + hits_col
    WORKSHEET.update_cell(cell.row, hits_col, str(new_hit_value))

    # calc compatibility
    compatibility = cell.col + 3
    perc = new_hit_value / (new_player_value * TOTAL_QUESTIONS) * 100
    WORKSHEET.update_cell(cell.row, compatibility, int(perc))

    # return all values
    return WORKSHEET.get_all_values()


