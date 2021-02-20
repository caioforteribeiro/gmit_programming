#Program that stores all calendar months in a tuple
#Prints out only the summer months, one at a time
#Author: Caio Forte Ribeiro

#Defines tuple with all months
months = ("January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December")

#Slices May, June and July and stores in summer
summer = months[4:7]

for month in summer:
    print(month)