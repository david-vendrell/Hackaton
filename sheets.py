import json
import logging
import pytz
import google.auth
from googleapiclient import discovery
from google.oauth2 import service_account

from user import UserManager

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
credentials, project = google.auth.default()

class SheetManager:
    
    def get_infections(self):
            service = discovery.build("sheets", "v4", credentials=credentials)
            spreadsheet_id = "11nWBri7VYjXRB-I8vIPuYmnSJDrwH3m_lfY2oPbIWDM"
            sheet="Full 1"
            request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=sheet + "!A:Z")
            print(request.execute())


SheetManager().get_infections()