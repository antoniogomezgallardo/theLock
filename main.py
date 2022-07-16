from cryptography.fernet import Fernet

class PasswordManager(object):

	"""docstring for PasswordManager"""
	def __init__(self):
		self.key = None
		self.password_file = None
		self.password_dict = {}


	def create_key(self, path):
		self.key = Fernet.generate_key()
		with open(path, 'wb') as f:
			f.write(self.key)

	
	def load_key(self, path):
		with open(path, 'rb') as f:
			self.key = f.read()


	def create_password_file(self, path, initial_values=None)
		self.password_file = path

		if initial_values is not None:
			pass # TODO: add password function


	def load_password_file(self, path):
		self.password_file = path

		with open(path, 'rb') as f:
			for line in f:
				site, encrypted = line.split(":")
				self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()




pm = PasswordManager()
pm.create_key("mykey.key")



