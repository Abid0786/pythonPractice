#two.py

import one

print('Top level in two.py')

one.func()

if __name__=='__main__':
	print('two.py is bein run directly')
else:
	print('two.py is being imported ')