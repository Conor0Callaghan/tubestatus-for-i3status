#!/usr/bin/python3

#
# Copyright:   Conor O'Callghan 2015
# Version:     v1.1.0a
# 
# Please feel free to fork this project, modify the code and improve 
# it on the github repo https://github.com/brioscaibriste/iarnrod 
#
 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import json
import sys
import tempfile
from datetime import datetime
from urllib.request import urlopen

'''

ParseArgs

A simple function to parse the command line arguments passed to the function. 
The function does very little sanitisation on the input variables. The 
argument passed is then returned from the function.  

'''

def ParseArgs():

    # Parse our command line argument for the line name
    parser = argparse.ArgumentParser()
    parser.add_argument('--line',dest='LineName',help='Specify the London line you want to report on')
    args = parser.parse_args()

    # Convert the line name to lower case for easy comparison
    Line = (args.LineName)
    Line = Line.lower()

    # If the line isn't in the line list, fail badly
    if Line not in ('district','circle','victoria','central','northern',
         'bakerloo','hammersmith-city','jubilee','metropolitan', 
         'piccadilly','waterloo-city','dlr',):
         print ("\nError, you have specified " + Line + " as your line. You must specify one of the following: "
                "\n\tDistrict"
                "\n\tCircle"
                "\n\tVictora"
                "\n\tCentral"
                "\n\tNorthern"
                "\n\tPiccadilly"
                "\n\tBakerloo"
                "\n\thammersmith-city"
                "\n\twaterloo-city"
                "\n\tDLR"
                "\n\tMetropolitan"
                "\n\tJubilee\n")
         sys.exit(1)
     
    return Line    

'''

RetrieveTFLData

This function takes the Line variable (a name of a Transport For London line 
name) and polls the TFL API. The function then returns the current line
status for the specified line. 

'''

def RetrieveTFLData(Line):

    # TFL Unified API URL
    TFLDataURL = "https://api.tfl.gov.uk/Line/" + Line + ("/Status?detail=False"
    "&app_id=&app_key=")

    # Read all the information from JSON at the specified URL
    #RawData = urlopen(TFLDataURL).readall().decode('utf8') or die("Error, failed to "
    #        "retrieve the data from the TFL website")
    #TFLData = json.loads(RawData)

    # Sanitize the data to get the line status
    #Scratch = (TFLData[0]['lineStatuses'])
    #LineStatusData = (Scratch[0]['statusSeverityDescription'])

    LineStatusData = "Good Service"
    return LineStatusData

'''

 check if temp file exists, if not, write it with time stamp in it, else pull time stamp
 check time stamp vs. poll interval, if it's less than time + interval, skip it, else run and write the temp file again
 two functions at least, one for time, one for polling, returning status value
'''

def Throttle(PollInterval,Throttle):

    if ( Throttle == "True" ):
        print ("Throttling in progress")

    TFile = tempfile.NamedTemporaryFile(suffix='dat', prefix='iarn-throttle', delete=False)

    try:
        #CurrentMinute = 26
        CurrentMinute = datetime.now().minute

    finally:
        CurrentMinute = datetime.now().minute

        # Get the current time stamp and write it to the temp file, but only if it doesn't exist
        #TFile.write(CurrentMinute)

    TimeFile = 18
    Remainder = CurrentMinute - TimeFile

    if ( Remainder < PollInterval ):
        print ("Not time to poll yet")
        Run = 0
    else:
        print ("Poll that shit and rewrite the file") 
        Run = 1

    TFile.close()

    return Run
