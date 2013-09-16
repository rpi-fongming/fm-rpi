#!/usr/bin/python
#
# Copyright (C) 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__author__ = 'api.rboyd@gmail.com (Ryan Boyd)'

import datetime

try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom
import getopt
import sys
import string
import time

def _FormatDatetime(tDatetime):
#    print (tDatetime)
#    result = tDatetime.replace(".000+","T")
    result = tDatetime[0:10] + " " + tDatetime[11:19] 
    return (result)


class CalendarExample:

  def __init__(self, email, password):
    """Creates a CalendarService and provides ClientLogin auth details to it.
    The email and password are required arguments for ClientLogin.  The
    CalendarService automatically sets the service to be 'cl', as is
    appropriate for calendar.  The 'source' defined below is an arbitrary
    string, but should be used to reference your name or the name of your
    organization, the app name and version, with '-' between each of the three
    values.  The account_type is specified to authenticate either
    Google Accounts or Google Apps accounts.  See gdata.service or
    http://code.google.com/apis/accounts/AuthForInstalledApps.html for more
    info on ClientLogin.  NOTE: ClientLogin should only be used for installed
    applications and not for multi-user web applications."""

    self.cal_client = gdata.calendar.client.CalendarClient(source='Google-Calendar_Python_Sample-1.0')
    self.cal_client.ClientLogin(email, password, self.cal_client.source);

  def RunTest(self, delete='false'):
    print ("Running test")
    self._DateRangeQueryEx('2013-09-16','2013-09-20')
    
  def _DateRangeQueryEx(self, start_date='2013-09-01', end_date='2013-09-10'):
    """Retrieves events from the server which occur during the specified date
    range.  This uses the CalendarEventQuery class to generate the URL which is
    used to retrieve the feed.  For more information on valid query parameters,
    see: http://code.google.com/apis/calendar/reference.html#Parameters"""

    print 'Date range queryEx for events on Primary Calendar: %s to %s' % (start_date, end_date,)
    text_query = ""
    query = gdata.calendar.client.CalendarEventQuery(text_query=text_query,start_min=start_date, start_max=end_date)
    feed = self.cal_client.GetCalendarEventFeed(q=query)
    for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
      for a_when in an_event.when:
#        print '%s; %s; %s ; %s' % (an_event.title.text,an_event.content.text,_FormatDatetime(a_when.start.strip()),_FormatDatetime(a_when.end.strip()))
        result = '%s; %s; %s ; %s' % (an_event.title.text,an_event.content.text,_FormatDatetime(a_when.start.strip()),_FormatDatetime(a_when.end.strip()))
        print result
        

  def _SaveDateRangeQuery(self, start_date='2013-09-01', end_date='2013-09-10'):
    """Retrieves events from the server which occur during the specified date
    range.  This uses the CalendarEventQuery class to generate the URL which is
    used to retrieve the feed.  For more information on valid query parameters,
    see: http://code.google.com/apis/calendar/reference.html#Parameters"""
    temp_list = []
    print 'Date range queryEx for events on Primary Calendar: %s to %s' % (start_date, end_date,)
    text_query = ""
    query = gdata.calendar.client.CalendarEventQuery(text_query=text_query,start_min=start_date, start_max=end_date)
    feed = self.cal_client.GetCalendarEventFeed(q=query)
    for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
      for a_when in an_event.when:
        result = '%s; %s; %s ; %s' % (an_event.title.text,an_event.content.text,_FormatDatetime(a_when.start.strip()),_FormatDatetime(a_when.end.strip()))
        temp_list.append(result)
#        print result
    return (temp_list)

def main():

  user = 'rpi.fongming@gmail.com'
  pw = 'Fongshek702'
  delete = 'false'

  duration = 20
  StartDate = datetime.date.today().strftime("%Y-%m-%d")
  EndDate = (datetime.date.today()+datetime.timedelta(days=duration)).strftime("%Y-%m-%d")

  print (StartDate,EndDate)
  
  sample = CalendarExample(user, pw)
  result = sample._SaveDateRangeQuery(StartDate,EndDate)
  if (len(result) !=0) :
    print ("Totally  " + str(len(result)) + " events")
    for event in result:
        print event


if __name__ == '__main__':
  main()