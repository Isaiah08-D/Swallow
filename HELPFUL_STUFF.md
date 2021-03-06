# get the user's end url (route)
```py
from flask import request
print(request.path)
# possible results:
# / (for the homepage)
# /login (for the login page)
# ...
```

# get one of the user's cookies (data is saved to the site, such as if he is currently logged in.)
```py
from flask import session
print(session.get('login'))
# Possible results:
# False or None (if the user is not logged in)
# [True, 'isaiah08'] (if the user is logged in and his username is isaiah08.)

# Note that i have made a function for this purpose:
from python.user import login_check
print(login_check)
# either returns False OR [True, '<username>']
```

# import a python file form a folder
```py
# gets the function called function1 from folder/file.py
from folder.file import function1
# BEWARE! This can also import the function called function1 in the class file in folder.py
```