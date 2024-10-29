# str => ""
# list => [], list()
#name = "Okurmen"
#name[0] = "A"
#print(name)
cities = ["Bishkek","Astana","osh","Stambul"]
print(cities)
cities[2] = "Talas"
print(cities)
cities[-2] = "Frunze"
print(cities)
print(cities[1:3:2])

#append (element)
cities = ["Bishkek","Astana","osh","Stambul"]
cities.append("Moscow")
cities.append("London")
print(cities)





cities = ["Bishkek","Astana","osh","Stambul"]
cities.append(["Moscow", "London"])
cities.extend(["Madrid", "Paris"])
cities.insert(0, "Naryn")
cities.insert(2, "Berlin")
cities.insert(5, "Rome")
print(cities)


#pop()
cities = ["Bishkek","Astana","osh","Stambul"]
d = cities.pop()
print(d)
d = cities.pop()
print(d)
cities.pop(1)
print(cities)
 



# remove()
cities = ["Bishkek","Astana","osh","Stambul","BIshkek"]
cities.remove("Bishkek")
print(cities)



# reverse()
cities = ["Bishkek","Astana","osh","Stambul","BIshkek"]
cities.reverse()
print(cities)



#clear
cities = ["Bishkek","Astana","osh","Stambul"]
cities.clear()
print(cities)



#sort
numbers = [2, 4, 6, 7, 5, 8, 9, 0, 2, 4, 5, 5, ]
numbers.sort()
print(numbers)
print(type(8/2))