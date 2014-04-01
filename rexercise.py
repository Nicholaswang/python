#rex
import os,re,datetime
filename = 'output_1989.11.21.txt'
get_time = re.search("(?P<year>\d{4})\.(?P<month>\d{2})\.(?P<day>\d{2})",filename)
year = get_time.group('year')
month = get_time.group('month')
day = get_time.group('day')
date = datetime.date(int(year),int(month),int(day))
wd = date.weekday()+1
os.rename(filename,'output_'+year+'-'+month+'-'+day+'-'+str(wd)+'.txt')

