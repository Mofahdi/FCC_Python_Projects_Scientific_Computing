def add_time(start, duration, start_day=None):
	start = start.split()
	start_am_pm = start[1]
	start_hour = start[0].split(':')[0]
	start_min = int(start[0].split(':')[1])

	start_hour = int(start_hour) + 12 if start_am_pm == 'PM' else int(start_hour)

	added_hr, added_min = int(duration.split(':')[0]), int(duration.split(':')[1])

	min_plus_duration = start_min + added_min
	if min_plus_duration > 60:
		added_hours=min_plus_duration//60
		min_plus_duration = min_plus_duration % 60
		hr_plus_duration = added_hours + added_hr + start_hour
	else:
		min_plus_duration = min_plus_duration
		hr_plus_duration = added_hr + start_hour
  
	if hr_plus_duration >= 24:
		days = hr_plus_duration // 24
		hrs_new_time = hr_plus_duration - days * 24
	else:
		days = 0
		hrs_new_time = hr_plus_duration
  
	if hrs_new_time > 11:
		hrs_new_time_am_pm = hrs_new_time - 12
		new_time_am_pm = 'PM'
		if hrs_new_time_am_pm==0:
			hrs_new_time_am_pm+=12
	else:
		if hrs_new_time==0:
			new_time_am_pm = 'AM'
			hrs_new_time_am_pm=hrs_new_time+12
		else:
			hrs_new_time_am_pm = hrs_new_time
			new_time_am_pm = 'AM'
	time_format = str(hrs_new_time_am_pm)
	time_format += ':'
	time_format += str(min_plus_duration).rjust(2, '0') if len(str(min_plus_duration)) == 1 else str(min_plus_duration)
	time_format+=new_time_am_pm.rjust(3)

	if start_day!=None:
		days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
		for i, day in enumerate(days_list):
			if start_day.lower() == day.lower():
				start_day_index = i
        
		new_day = start_day_index + days
		if new_day>=7:
			new_day=new_day%7
		time_format+=', '+days_list[new_day]

	if days==1:
		time_format+=' (next day)'
	elif days>1:
		time_format+=' ('+str(days)+' days later)'

	return time_format
	return time_format