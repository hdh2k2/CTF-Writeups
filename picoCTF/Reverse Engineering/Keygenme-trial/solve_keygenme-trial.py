#============================================================================#
#============================ARCANE CALCULATOR===============================#
#============================================================================#

import hashlib #hashtable
#from cryptography.fernet import Fernet
import base64

username_trial = "FREEMAN"
## 45362718
flag = "picoCTF{1n_7h3_|<3y_of_"
#decode
flag += hashlib.sha256(username_trial.encode()).hexdigest()[4]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[5]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[3]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[6]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[2]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[7]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[1]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[8]
flag +='}'
print(flag)

