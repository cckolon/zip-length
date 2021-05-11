import googlemaps # Google maps API package
import csv # For manipulating input and output via CSV files

api_key = 'YOUR_KEY_HERE' # paste your own API key in here

gmaps = googlemaps.Client(key = api_key) # set up the google maps API client

def distance_to_hospital(zip): # a function which tells you the distance from the center of the zip code to each hospital
	routetoSF = gmaps.distance_matrix(zip,'1975 4th St, San Francisco, CA 94158') # distance to SF hospital. SF address is hard-coded
	routetoOakland = gmaps.distance_matrix(zip,'747 52nd St, Oakland, CA 94609') # distance to Oakland hospital. Oakland address is hard-coded
	sfdistance = (routetoSF['rows'][0]['elements'][0]['distance']['value'])/1609.34 # sort through the data structure to determine the distance, in meters, along the route. Divide by 1609.34 to get the distance in miles
	oaklanddistance = (routetoOakland['rows'][0]['elements'][0]['distance']['value'])/1609.34 # same, but for Oakland
	return([sfdistance,oaklanddistance]) # return both distances

with open("distancedata.csv") as fp: # open the list of zip codes in a vertical column from a CSV file
    reader = csv.reader(fp, delimiter=",", quotechar = '"')
    zips = [row for row in reader] # save it as a nested list called zips
	
for place in zips: # for loop to append the SF and Oakland distances to each element in zips
	distances = distance_to_hospital(place[0]) # determine the distances
	place.append(distances[0]) # append the SF distance
	place.append(distances[1]) # append the Oakland distance
	
with open("output.csv","wt",newline='') as fp: # write the new list to a CSV called "output"
    writer = csv.writer(fp, delimiter=",")
    writer.writerows(zips)
    