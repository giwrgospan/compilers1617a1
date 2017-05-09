
import sys
import re
import argparse


parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname,newline='') as ifp:	
	for line in ifp:
	
		
			offset=float(sys.argv[2])
			offset1=int(offset)
			offset2=float(offset-offset1)
			
			h1=float(m.group(1))
			m1=float(m.group(2))
			s1=float(m.group(3))
			s2=float(m.group(4))
			totalsec1=h1*3600+m1*60+s1+s2/1000+offset

			h1o=totalsec1/3600
			m1o=totalsec1/60
			s1o=s1+offset1
			s2o=s2+offset2

			h2=float(m.group(5))
			m2=float(m.group(6))
			s3=float(m.group(7))
			s4=float(m.group(8))
			
			totalsec2=h2*3600+m2*60+s3+s4/1000+offset
			h2o=totalsec2/3600
			m2o=totalsec2/60
			s3o=s3+offset1
			s4o=s4+offset2
			print '%.2f,':',%.2f,':',%.2f,','%.3f,'','-->','',%.2f,':',%.2f,':',%.2f,',',%.3f'%(h2o,m2o,s3o,s4o,h1o,m1o,s1o,s2o,h2o,m2o,s3o,s4o)
		
		line=str(line)
		sys.stdout.write(line)

		
