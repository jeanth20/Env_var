# import os module
import os

# access the environment variable named 'app_password'
# The value returned when environment variable is not present in the stystem is given as the second input
val = os.getenv('app_password', 'default_value')

print('The value of app_password is {0}'.format(val))
# this should print
# The value of app_password is mysupersecret
