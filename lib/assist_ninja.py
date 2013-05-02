import requests
import re

def extract_groups(html_response, groups = []):
	response = str(html_response)
	group = re.findall(r'([\s]?[-]+[\s]*<[Bb]\s?>[\s\S]*?)[\s]+[-]+[\s]+<[Bb]\s?>', response)
	if (len(group) > 0):		
		groups.append({ 'title' : extract_title(group[0]), 'raw content' : group[0] })
		response = response.replace(str(group[0]), '')
		extract_groups(response, groups)
	return(groups)

def extract_courses(group, courses = []):
	courses = re.findall(r'\|([A-Z]+\s\d+[A-Z]?)', str(group))
	return(courses)

def extract_title(group):
	title = re.findall(r'[\s]?[-]+[\s]+<[Bb]\s?>([\s\S]*?)</[Bb]\s?>', group)
	return(title[0].rstrip().lstrip())


class AssistNinja():
	"""Connects to assist.org, retrieves reports 
	   and parses them out for you"""
	
	base_url = 'http://web1.assist.org/cgi-bin/REPORT_2/Rep2.pl'
	extra_params = '&dir=1&&sidebar=false&rinst=left&mver=2&kind=5&dt=2'
	
	def __init__(self):
		self.reports = {}
		self.missions = []

	# example attributes: 
	# major = 'EECS'
	# year = '12-13'
	# transfer_to = 'UCB'
	# transfer_from = 'BERKELEY'
	
	def fetch_report(self, transfer_from, transfer_to, major, year):
			mission = { 'transfer_from' : transfer_from, 'transfer_to' : transfer_to, 'major' : major, 'year' : year }
			# add logic to prevent duplication of missions that deliver the same report
			self.missions.append(mission)
			request = requests.get(self.build_url(transfer_from, transfer_to, major, year))
			self.reports[major + '-' + transfer_to] = { 'raw request' : request.text }
			report = self.reports[major + '-' + transfer_to]
			self.extract_reports_data()
			return report
	
			
	def build_url(self, transfer_from, transfer_to, major, year):
		major_params = '?aay=' + year + '&dora=' + major
		transfer_from_params = '&agreement=aa&sia=' + transfer_from + '&ia=' + transfer_from
		transfer_to_params = '&oia=' + transfer_to + '&ay=' + year + '&event=19&ria=' + transfer_to
		return self.base_url + major_params + transfer_to_params + transfer_from_params + self.extra_params
	
	
	def extract_reports_groups(self):
		for report in self.reports.keys():
			self.reports[report]['groups'] = extract_groups(self.reports[report]['raw request'])
	
	def extract_reports_courses_and_titles(self):
		for report in self.reports.keys():
			self.reports[report]['all_courses'] = []
			for group in self.reports[report]['groups']:
				courses = extract_courses(group['raw content'])
				group['courses'] = courses
				self.reports[report]['all_courses'] += courses 		
	
	
	def courses_for(self, major, transfer_to):
		return self.reports[major + '-' + transfer_to]['all_courses']
	
	def groups_for(self, major, transfer_to):
		return self.reports[major + '-' + transfer_to]['groups']
	
	def extract_reports_data(self):
		self.extract_reports_groups()
		self.extract_reports_courses_and_titles()

# reports dictionary example:
#	
# reports = { 'EECS-UCB' : { 	'raw request'  : '<html>The request response</html>',
#															 	  'groups'   : [
#																							 	{'title'      : 'Group 1', 
#															 						      'raw content' : '<div>Group 1 ... </div>',
#																						    'courses'     : ['CRS1A']},
#																							 	{'title' 	    : 'Group 2', 
#															 						  	  'raw content' : '<div>Group 2 ... </div>',
#																							  'courses'     : ['CRS1B']}
#																				 		  ]
#															'all_courses' : ['CRS1A', 'CRS1B']
#														} 
#						} 