import socket
import logging
import atom.service
import gdata.service
import gdata.spreadsheet
import gdata.spreadsheet.service
import gdata.spreadsheet.text_db
                                                       
class SampleFetcher():
    def run(self, from_date=None, to_date=None):
        self.getGoogleEntries(from_date, to_date)

    def getGoogleEntries(self, from_date=None, to_date=None):                
        """
	    Sample code to fetch data from a Google Spreadsheet using a query and a sort, followed
	    by example of how to get the data out by column name.
	
	    This code assumes you have a spreadsheet that looks something like this:
	
	    Timestamp  		|	First Name	|	Last Name
	    8/16/2010 12:15:00  |	Michael		|	Woof
	    8/17/2010 14:25:35	|	John		|	Doe          
	
	    Google Spreadsheets normalizes the column names for the purposes of the API by stripping all non-alphanumerics and lower-casing,
	    hence the column names used in the code as "timestamp", "firstname", and "lastname".
	    """
        gd_client = gdata.spreadsheet.service.SpreadsheetsService()
        gd_client.email = 'rpi.fongming@gmail.com'
        gd_client.password = 'Fongshek702'
        gd_client.source = 'python rpi'

        try:                    
	    # log in
            gd_client.ProgrammaticLogin()
        except socket.sslerror, e:
            logging.error('Spreadsheet socket.sslerror: ' + str(e))
            return False
	    
	key = 'YOUR_SPREADSHEET_KEY'
	wksht_id = 'rpi-config'
        
        q = gdata.spreadsheet.service.ListQuery()
        q.orderby = 'column:firstname'
        q.reverse = 'true'

        # Here's the actual query
        if from_date and to_date:
            q.sq = 'timestamp >= %s and timestamp <= %s' % (from_date, to_date)
        elif from_date:
            q.sq = 'timestamp >= %s' % from_date
        elif to_date:
            q.sq = 'timestamp <= %s' % to_date

        try:
	    # fetch the spreadsheet data
            feed = gd_client.GetListFeed(key, wksht_id, query=q)
        except gdata.service.RequestError, e:
            logging.error('Spreadsheet gdata.service.RequestError: ' + str(e))
            return False
        except socket.sslerror, e:
            logging.error('Spreadsheet socket.sslerror: ' + str(e))
            return False
        
        # Iterate over the rows
        for row_entry in feed.entry:
	    # to get the column data out, you use the text_db.Record class, then use the dict record.content
            record = gdata.spreadsheet.text_db.Record(row_entry=row_entry)
            print "%s,%s,%s" % (record.content['timestamp'], record.content['firstname'], record.content['lastname'])

if __name__ == "__main__":
    SampleFetcher().run()

