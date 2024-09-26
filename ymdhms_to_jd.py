# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Ajay Seethana
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2
# parse script arguments
if len(sys.argv)==7:
  year = int(sys.argv[1])
  month = int(sys.argv[2])
  day = int(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
  ...
else:
  print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()

# write script below this line

JD1 = day - 32075
JD2 = 1461 * (year + 4800 + ((month - 14)//12 + 1))//4
JD3 = 367 * int(month - 2 - ((month-14)//12 + 1) * 12)//12
JD4 = -3 * ((year + 4900 + ((month - 14)//12 + 1))//100)//4

JD = JD1 + JD2 + JD3 + JD4
JD_mid = JD - 0.5
D_frac = (second + 60 * (minute + 60 * hour))/86400

jd_frac = JD_mid + D_frac

print(jd_frac)
