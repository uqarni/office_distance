import pandas as pd
from geopy import distance

data = pd.read_csv("roster.csv")
# Person Number,	Name, Work Email,	Job Name, Department Name, Level 01 Organization Name,	Management Level,	Employee Enterprise Hire Date,	Address Line 1,	Address Line 2,	City,	Region 2,	Postal Code,	Location Name,	Geocoded latitude,	Geocoded longitude,	Geocoded address

max_distance = 45 #miles

#office coordinates 
austin_coords = (30.481609, -97.776680)
glendale_coords = (34.146500, -118.255520)
playavista_coords = (33.973358, -118.430191)
mountainview_coords = (37.394770, -122.080580)

#initialize list for people in area
max_dist = 45 #miles
austin_peeps = []
glendale_peeps = []
playavista_peeps = []
mountainview_peeps = []

for index, row in data.iterrows():
    if row["Geocoded latitude"] > 0 and row["Geocoded longitude"] < 0:
        person_coords = (row["Geocoded latitude"], row["Geocoded longitude"])
        if distance.distance(person_coords, austin_coords).miles < 45:
            austin_peeps.append(row["Work Email"])
        if distance.distance(person_coords, glendale_coords).miles < 45:
            glendale_peeps.append(row["Work Email"])
        if distance.distance(person_coords, playavista_coords).miles < 45:
            playavista_peeps.append(row["Work Email"])
        if distance.distance(person_coords, mountainview_coords).miles < 45:
            mountainview_peeps.append(row["Work Email"])


print(austin_peeps)
print(len(austin_peeps))
    

    

    


    




