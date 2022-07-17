# The Lock

The Lock is a simple cli-application that allows you to manage your passwords. All passwords are safely encrypted in a file and decrypted when the user whants to retrieve one of them.

## Libraries

The lock uses [Fernet](https://cryptography.io/en/latest/fernet/) to encrypt/decrypt data.

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

token = f.encrypt(b"my deep dark secret")

token
b'...'

f.decrypt(token)
b'my deep dark secret'
```

## Usage

run from the root directory:
```
python main.py 
```

```bash
                         __                   _          _______ _            _                _    
 \ \        / / | |                          | |        |__   __| |          | |              | |   
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___      | |  | |__   ___  | |     ___   ___| | __
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \     | |  | '_ \ / _ \ | |    / _ \ / __| |/ /
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |    | |  | | | |  __/ | |___| (_) | (__|   < 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/     |_|  |_| |_|\___| |______\___/ \___|_|\_                                                                                                    
                                                                                                    




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


Enter your choice: 

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)