import pandas as pd
from geopy import distance
import numpy as np
import matplotlib.pyplot as plt

##MANUAL INPUTS
#office coordinates 
austin_coords = (30.481609, -97.776680)
glendale_coords = (34.146500, -118.255520)
playavista_coords = (33.973358, -118.430191)
mountainview_coords = (37.394770, -122.080580)
coords_list = [austin_coords, glendale_coords, playavista_coords, mountainview_coords]

#divisions and office location names
depts = [
    "Marketing",
    "Finance",
    "Product",
    "Care",
    "Tax",
    "People & Places",
    "Fulfillment",
    "Technology",
    "Legal",
    "Partnerships",
    "Executive",
    "Sales",
    "Strategy & Ops",
    "Central Operations",
    "Design"]
locs = [
    "Austin",
    "Glendale",
    "Playa Vista",
    "Mountain View",
    "none"]
loc_coords = {
    locs[0]: coords_list[0],
    locs[1]: coords_list[1],
    locs[2]: coords_list[2],
    locs[3]: coords_list[3],
    locs[4]: (0,0)
}

#roster CSV, last updated Feb 17
data = pd.read_csv("roster.csv")
data["Location"] = ""
aapi = pd.read_csv("aapi-roster.csv")

cutoff_date = 44835.00 #10/1/22
max_dist = 50 #miles
count = 0
person_count = 0
# Person Number,	Name, Work Email,	Job Name, Department Name, Level 01 Organization Name,	Management Level,	Employee Enterprise Hire Date,	Address Line 1,	Address Line 2,	City,	Region 2,	Postal Code,	Location Name,	Geocoded latitude,	Geocoded longitude,	Geocoded address

##NEW HIRES OFFICE PROXIMITY
#create depts x locs empty DataFrame 
cols = {}
for loc in locs:
    cols[loc] = [0]*len(depts)
output = pd.DataFrame(data = cols, index=depts)

#iterate through roster
for index, row in data.iterrows():
    #skip erroneous coordinates
   if row["Geocoded latitude"] > 0 and row["Geocoded longitude"] < 0:
       person_count += 1
       #extract person's coordinates, hire date, department, amass all new hires
       person_coords = (row["Geocoded latitude"], row["Geocoded longitude"])
       hire_date = row["Employee Enterprise Hire Date"]
       person_dept = row["Level 01 Organization Name"]
        
        #loop through locations to check for proximity and add to output
       assigned = 0
       for key in loc_coords:
           if distance.distance(person_coords, loc_coords[key]).miles < max_dist:
               output[key][person_dept] += 1
               count +=1
               assigned = 1

       if assigned == 0:
               output["none"][person_dept] += 1
               count +=1
               assigned = 1

output.index.name = "Function"

output.to_csv("all_staff_output.csv")
           
##visualize it
# output.plot.bar(stacked = True, title = "Function by Location, new hires")
# 
#print(person_count)
#print(count)

#output_t = output.T
#output_t.plot.bar(stacked = True, title = "Location by Function")
#plt.show()

#initialize list for people in area

austin_peeps = []
glendale_peeps = []
playavista_peeps = []
mountainview_peeps = []

austin = 0
la = 0
mv = 0
remote = 0


#populate the above peeps lists
for index, row in data.iterrows():
    if row["Geocoded latitude"] > 0 and row["Geocoded longitude"] < 0 and row["Work Email"] in aapi['EMAIL'].values:
        person_coords = (row["Geocoded latitude"], row["Geocoded longitude"])
        if distance.distance(person_coords, austin_coords).miles < max_dist:
            data.loc[index,"Location"] = "Austin"
            austin += 1
        elif distance.distance(person_coords, glendale_coords).miles < max_dist:
            data.loc[index,"Location"] = "LA"
            la += 1
        elif distance.distance(person_coords, playavista_coords).miles < max_dist:
            data.loc[index,"Location"] = "LA"
            la += 1
        elif distance.distance(person_coords, mountainview_coords).miles < max_dist:
            data.loc[index, "Location"] = "Mountain View"
            mv += 1
        else:
            data.loc[index,"Location"] = "Remote"
            remote += 1

print(aapi)
print("Austin:")
print(austin)
print("LA:")
print(la)
print("Mountain View:")
print(mv)
print("Remote:")
print(remote)













    

    

    


    




