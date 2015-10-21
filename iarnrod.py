#!/usr/bin/python3

#
# Copyright:   Conor O'Callghan 2015
# Version:     v1.1.0
# 
# Please feel free to fork this project, modify the code and improve 
# it on the github repo https://github.com/brioscaibriste/iarnrod 
 
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

import coire

# Iarnrod Tuning options
Throttling = "True"
PollInterval = 5 # This is the status polling interval in minutes  
StatusOutput = "small" # You can set this to small or large and it will change the output format
TFileName = '/tmp/iarn-i3-temp' # Where to store the timestamp file for poll throttling
SFileName = '/tmp/iarn-i3-stat' # Where to store the cache of the line status

# Parse the command line arguments
Line = coire.ParseArgs()

# Throttling
Run = coire.Throttle(PollInterval,Throttling,TFileName)

# Gather the line status data
LineStatusData = coire.RetrieveTFLData(Line,Run,SFileName)

# Generate the status output and print
if (StatusOutput == "small") and (LineStatusData == "Good Service"):
    print ("TFL " + Line[0] + Line[1] + Line[2] + " OK")
elif StatusOutput == "small":
    print ("TFL " + Line[0] + Line[1] + Line[2] + " " + LineStatusData)
else:
    print ("TFL " + Line + " line has " + LineStatusData)
