import requests
import re

class AssistNinja():
	"""Connects to assist.org, retrieves reports 
	   and parses them out for you"""
	
	base_url = 'http://web1.assist.org/cgi-bin/REPORT_2/Rep2.pl'
	extra_params = '&dir=1&&sidebar=false&rinst=left&mver=2&kind=5&dt=2'

	# major = 'EECS'
	# year = '12-13'
	# t_to = 'UCB'
	# t_from = 'BERKELEY'
	
	def __init__(self):
		self.reports = []
		self.t_from = ''
		self.t_to = ''
		self.major = ''
		self.year = ''
	
	def set_mission_info(self, transfer_from, transfer_to, major, year):
		self.t_from = transfer_from
		self.t_to = transfer_to
		self.major = major
		self.year = year
	
	def fetch_report(self):
		if (self.t_from):
			major_params = '?aay=' + self.year + '&dora=' + self.major
			transfer_from_params = '&agreement=aa&sia=' + self.t_from + '&ia=' + self.t_from
			transter_to_params = '&oia=' + self.t_to + '&ay=' + self.year + '&event=19&ria=' + self.t_to
			request = requests.get(base_url + major_params + transfer_to_params + transfer_from_params + extra_params)
			self.reports.append(request.text)
		else:
			print('You need to give your ninja information about the report you want.')
			print('Use #set_mission_info(transfer_from, transfer_to, major, year)\n')

def extract_group(html_response, groups = []):
	response = str(html_response)
	group = re.findall(r'([\s]?[-]+[\s]*<[Bb]\s?>[\s\S]*?)[\s]+[-]+[\s]+<[Bb]\s?>', response)
	if (len(group) > 0):
		groups.append(group[0])
		response = response.replace(str(group[0]), '')
		extract_group(response, groups)
	return(groups)

def extract_courses(group, courses = []):
	courses = re.findall(r'\|([A-Z]+\s\d+[A-Z]?)', str(group))
	return(courses)
	
def extract_title(group):
	title = re.findall(r'[\s]?[-]+[\s]+<[Bb]\s?>([\s\S]*?)</[Bb]\s?>', group)
	return(title[0].rstrip().lstrip())
	
# major = 'EECS'
# year = '12-13'
# t_to = 'UCB'
# t_from = 'BERKELEY'
# base_url = 'http://web1.assist.org/cgi-bin/REPORT_2/Rep2.pl'
# extra_params = '&dir=1&&sidebar=false&rinst=left&mver=2&kind=5&dt=2'
# 
# 
# url = base_url + '?aay=' + year + '&dora=' + major + '&oia=' + t_to + '&ay=' + year + '&event=19&ria=' + t_to + '&agreement=aa&sia=' + t_from + '&ia=' + t_from + extra_params
# request = requests.get(url)

# groups = extract_group(request.text)
# 
# for group in groups:
# 	print extract_title(group)
# 	for course in extract_courses(group):
# 		print course

ninja = AssistNinja()
ninja.set_mission_info('BERKELEY', 'UCB', 'EECS', '12-13')
ninja.fetch_report()