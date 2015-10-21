# Iarnród

This script is a very crude JSON retrieval/parse system which utilises the 
Transport For London (TFL) Application Interface (API) to retrieve the current 
service status of a given TFL rail line. 

The script does not carry out any validation on the data recieved from TFL and
 there is very little sanitisation of the data fed via the command line.

The name iarnród comes from the Irish (Gaeilge) word for railway, directly 
translated to English as iron road. 

## TFL Data

Before you modify and use this code, you should read the TFL API rules on the
[TFL data website](https://tfl.gov.uk/info-for/open-data-users/)

# Usage Instructions

## General usage

**This script requires python3** 

This script is quite simple and only requires the name of the line whose status
you are querying as an input e.g. 
 
```bash
   ./iarnrod --line=hammersmith-city 
```

You can specify any of the lines listed below as the line name

 * District
 * Circle
 * Victora
 * Central
 * Northern
 * Piccadilly
 * Bakerloo
 * hammersmith-city
 * waterloo-city
 * DLR
 * Metropolitan
 * Jubilee

## i3status integration

This script works with i3status, though probably not as it should :[

In order to make this work with the i3status, you should modify your 
.i3status.conf and ensure it contains the following line

```bash
   output_format = "i3bar"
```

In the general section of your configuration you should have somthing similar  
to the following

```bash
   status_command i3customstatus
```

As per the i3status documentation, you should add a wrapper accessible on your
 path which executes drawing in the i3status details alongside your script. 
A sample wrapper file can be found in the man page for i3status. 

You can also find a sample script in this repository. 

# License

Copyright Conor O'Callaghan 2015

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
