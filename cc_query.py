from datetime import date
from datetime import timedelta
from itertools import cycle 

date_elements = []
while len(date_elements)<3:
	user_data = input("Enter a date (mm/dd/yyyy): ")
	date_elements = user_data.split('/')
if date_elements[0][0]=='0':
	date_elements[0]=date_elements[0][1]
if date_elements[1][0]=='0':
	date_elements[1][0]==date_elements[1][1]

lookup_date = date(int(date_elements[2]),int(date_elements[0]),int(date_elements[1]))

# List of interns
interns = ['Isabel','Kai','Lynette','Gladys','Shanique','Tadelin']
intern_cycle = cycle(interns)

# List of Thursdays we don't meet in our groups
no_session = { 
	date(2019,11,5), date(2019,11,7), date(2019,11,28), date(2019,12,26),
	date(2020,1,2), date(2020,1,9), date(2020,1,30), date(2020,2,27),
	date(2020,2,20), date(2020,4,2), date(2020,4,9), date(2020,4,16),
	date(2020,6,4)
	}

# Start date
start_date = date(2019,10,24)

# End date
end_date = date(2020,6,7)

sessions=[]
date = start_date
date_dict = dict()

while date < end_date:
	if date not in no_session:
		date_dict[date]=next(intern_cycle)
		#print(date, next(intern_cycle))
	date += timedelta(days=7)

if lookup_date in date_dict:
	print("Cheers and challenge by %s" % date_dict[lookup_date])
else:
	print("No cheers and challenge this date!")

	







