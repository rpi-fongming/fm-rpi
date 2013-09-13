import gdata.spreadsheet.service

GoogleUser = "rpi.fongming@gmail.com"
GooglePW = "Fongshek702"
         

def GSheetService(user,pwd):
                gd_client = gdata.spreadsheet.service.SpreadsheetsService()
                gd_client.email = user
                gd_client.password = pwd
                gd_client.source = 'amazonWishListToGSheet.py'
                gd_client.ProgrammaticLogin()
            
                return gd_client

gs = GSheetService(GoogleUser,GooglePW)
sheets = gs.GetSpreadsheetsFeed()

print map(lambda e: e.title.text + " : "  + e.id.text.rsplit('/', 1)[1],sheets.entry)


