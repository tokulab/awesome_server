import time
import sys

ERROR_OCCURRED_TEMPLATE = '''
------------------------------
An unexpected error has occurred.
Please try this following.

{err}
------------------------------
'''

def force_abort(limit=3):
    print('Automatically abort after {} seconds.'.format(str(limit)))
    for cnt in range(limit):
        sys.stdout.write('#')
        sys.stdout.flush()
        time.sleep(1)
    sys.exit('\nAbort.')
