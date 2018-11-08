schema = open('schema.txt','r')
java = open('SchemaJava.class','w')

## add a product
## to the "on-order" list
# M AddProduct
# F id	int
# F name	char[30]
# F order_code	int
# E


def comment_handler():
	print 'comment fn'

def field_handler():
	print 'field'

def method_handler():
	print 'method'

def end_handler():
	print 'end'

def default_handler():
	print 'default'

switcher = {
	'#': comment_handler,
	'F': field_handler,
	'M': method_handler,
	'E': end_handler
}

for line in schema:
	character = line[:1]
	fn = switcher.get(character, default_handler)
	fn()
