# This is an example of python lambda function sorting list of dictionaries by a specific key and it's subsequent value

deps = [
	{
		'funding': 10000,
		'department': 'Statistics',
		'department_head': 'kevin berlington'
	},
    {
    	'funding': 15000,
		'department': 'Physics',
		'department_head': 'Sean Baskin'
    },
    {
        'funding': 8000,
		'department': 'Art',
		'department_head': 'Kelly Crumlin'
    }
]

#Simply printing the result of lambda function being passed to sorted function. 
print(sorted(deps, key=lambda x:x['department'], reverse=False))

#We can store the lambda function in a variable so we can pass any list of dict
sort_dict = lambda list_of_dicts:sorted(list_of_dicts, key=lambda x:x['department'], reverse=False)
