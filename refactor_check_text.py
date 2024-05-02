numbers = {"count": 0, "items": []}
strings = {"count": 0, "items": []}
symbols = {"count": 0, "items": []}
spaces = {"count": 0, "indexes": []}

def add_spaces(index):
    spaces.update({ "count": spaces["count"] + 1 })
    spaces["indexes"].append(index)

def add_string(item):
    strings.update({ "count": strings["count"] + 1 })
    strings["items"].append(item)

def add_number(item):
    numbers.update({ "count": numbers["count"] + 1 })
    numbers["items"].append(item)

def add_symbol(item):
    symbols.update({ "count": symbols["count"] + 1 })
    symbols["items"].append(item)

def check_text(text):
	for item in text:
		if item.isnumeric():
			add_number(item)
		elif item.isalpha():
			add_string(item)
		elif item.isspace():
			add_spaces(text.index(item))
		else:
			add_symbol(item)

def print_result():
	print (f"length of text : {len(text)} \nCount of number : {numbers['count']} ,numbers : {numbers['items']} ,\n Count of alphabet : {strings['count']} , strings : {strings['items'] }\n Count of symbols :{symbols['count']} , symbols : {symbols['items']} \n Count of spaces: {spaces['count']}, indexes: {spaces['indexes']} ")


text=input("Enter your text")
check_text(text)
print_result()
