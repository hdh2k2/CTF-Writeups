picoCTF{1n_7h3_|<3y_of_0d208392}

## CODE 


# import hashlib
import hashlib

# username
username_trial = "FREEMAN"

# known flag
flag = "picoCTF{1n_7h3_|<3y_of_"

# decrypt flag
flag += hashlib.sha256(username_trial.encode()).hexdigest()[4]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[5]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[3]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[6]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[2]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[7]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[1]
flag += hashlib.sha256(username_trial.encode()).hexdigest()[8]

flag += '}'

# print flag
print(flag)
