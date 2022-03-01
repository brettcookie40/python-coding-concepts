# This is an example of python lambda function sorting list of dictionaries
# import pprint
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

print(sorted(deps, key=lambda x:x['department'], reverse=False))