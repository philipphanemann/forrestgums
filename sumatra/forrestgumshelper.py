""" these are helper functions to extract information out of the gams 
listing file after a run"""

class ForrestHelper(object):
	def __init__(self, project, record):
		self.project = project
		self.record = record

	def set_gams_version(self):
		version = self._get_gams_version()
		if version:
			self.record.executable.version = version
		#TODO: should be deleted because version should be found
		else:
			self.record.executable.version = 'still unknown'
		self.project.record_store.save(self.project.name, self.record)

	def _get_gams_version(self):
		main = self.project.default_main_file.split('.')[0]
		path = self.project.path
		with open(path + '/' + main + '.lst', 'r') as f:
			for line in f:
				if '\x0cGAMS' in line: #unicode for FFGams
					return line.split(' ')[1]