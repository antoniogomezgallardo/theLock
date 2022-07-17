from cryptography.fernet import Fernet
import os



class PasswordManager(object):

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

	def delete_key(self, path):
		if os.path.exists(path):
		  os.remove(path)
		else:
		  print(f"The file {path} does not exist") 

	def create_password_file(self, path, initial_values=None):
		self.password_file = path

		if initial_values is not None:
			for key, value in initial_values.items():
				self.add_password(key, value)

	def load_password_file(self, path):
		self.password_file = path

		with open(path, 'r') as f:
			for line in f:
				site, encrypted = line.split(":")
				self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

	def add_password(self, site, password):
		self.password_dict[site] = password

		if self.password_file is not None:
			with open(self.password_file, 'a+') as f:
				encrypted = Fernet(self.key).encrypt(password.encode())
				f.write(site + ":" + encrypted.decode() + "\n")

	def get_password(self, site):
		return self.password_dict[site]

	def print_password_file(self, path):
		for site, key in self.password_dict.items():
			print(site + " : " + key)

	def show_menu(self):
		print(""" 



			 __                   _          _______ _            _                _    
 \ \        / / | |                          | |        |__   __| |          | |              | |   
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___      | |  | |__   ___  | |     ___   ___| | __
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \     | |  | '_ \ / _ \ | |    / _ \ / __| |/ /
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |    | |  | | | |  __/ | |___| (_) | (__|   < 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/     |_|  |_| |_|\___| |______\___/ \___|_|\_\
                                                                                                    
                                                                                                    




			What do you want to do?:

			(1): Create a new Key
			(2): Get an existing Key
			(3): Delete an existing key
			(4): Create new Password File
			(5): Load exisiting Password File
			(6): Add a new Password
			(7): Get an existing Password from loaded file
			(8): Print all existing Passwords in loaded file
			(m): Show Menu
			(q): Quit

			""")



def main():
	sample_passwords = {
			"email":"email_password",
			"youtube":"youtube_password",
			"some_site":"some_site_password"
	}

	pm = PasswordManager()
	pm.show_menu()

	done = False


	while not done:

		choice = input("Enter your choice: ")
		if choice == "1":
			path = input("Enter Path: ")
			pm.create_key(path)
		elif choice == "2":
			path = input("Enter Path: ")
			pm.load_key(path)
		elif choice == "3":
			path = input("Enter Path: ")
			pm.delete_key(path)
		elif choice == "4":
			path = input("Enter Path: ")
			pm.create_password_file(path, sample_passwords)
		elif choice == "5":
			path = input("Enter Path: ")
			pm.load_password_file(path)
		elif choice == "6":
			path = input("Enter Path: ")
			site = input("Enter the site: ")
			password = input("Enter the Password: ")
			pm.add_password(site, password)
		elif choice == "7":
			site = input("Enter the site: ")
			print(f"Password for {site} is {pm.get_password(site)}")
		elif choice == "8":
			path = input("Enter Path: ")
			pm.print_password_file(path)
		elif choice == "m":
			pm.show_menu()
		elif choice == "q":
			done = True
			print("bye!")
		else:
			print("Invalid choice!")



if __name__ == "__main__":
	main()