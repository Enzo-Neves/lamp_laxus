import json

# Opening JSON file...
f = open('dataset1.json')

# creates a dictionary with all the data
data = json.load(f)

# get the list of the dictionary
base_stations = data['base_stations']
edge_servers = data['edge_servers']
users = data['users']
applications = data['applications']
services = data['services']
networks = data['network']
links = networks['links']

for i in base_stations:
    base_stations[i]

# dat = [data['base_stations'], data['edge_servers'], data['users'],data['applications'], data['services'], data['network']]
# print
# print('Base Stations: ', base_stations)
# print('Edge Servers: ', edge_servers)
# print('Users: ', users)
# print('Applications: ', applications)
# print('Services: ', services)
# print('Networks: ', networks)
# print('Links (from networks): ', links)
print(dat)
