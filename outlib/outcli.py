import sys
from outlib.models import r_outliers

def main():

	sysarglist = sys.argv
	sysarglist.pop(0)
	assert len(sysarglist) == 2, "Insufficient number of arguments provided"

	filename_in = sysarglist[0]
	filename_out = sysarglist[1]
	assert filename_in, "Input CSV filename must be provided"
	assert filename_out, "Output CSV filename must be provided"
	r_outliers(filename_in, filename_out)
