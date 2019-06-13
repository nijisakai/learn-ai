import re
def search(lists,s):
	suggestions = []
        pattern = '.*'.join(s) # Converts 'djm' to 'd.*j.*m'
        regex = re.compile(pattern)     # Compiles a regex.
        for item in lists:
            match = regex.search(item)  # Checks if the current item matches the regex.
            if match:
#                suggestions.append((len(match.group()), match.start(), item))
		suggestions.append(item)
	if suggestions:
		return suggestions
	else :
		return lists
