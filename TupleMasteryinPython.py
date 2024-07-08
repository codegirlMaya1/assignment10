

itinerarys=[
        ("Alice", ["Flabc", "New York","London"],["FL123"," London", "Paris"]),
        
]
itinerarys1=[
      ("Bob",("FL456", "Tokyo", "San Francisco"),("Fl789","San Francisco", "New York")),
]

print(" Enter 1: View all itenararies") 
print(" Enter 2: Search by passenger/traveler")
print(" Enter 3: Search by departure city")
print(" Enter 4: Show current itenary")
choice=input("Enter your choice:  ")
pass
def find_travelers_itenarary(itinerarys,traveler):
   for flight in itinerarys[0:]:
            print(f"fligh+t: {flight[0]}, From: {flight[1]}, To: {flight[2]},")
            break
   else:
            print("No itinerary found for this traveler")
def show_city_itinerary(itinerarys,origin):
   print(f"\nItineraries from {origin}")
   for itenary in itinerarys1:
      for flight in itinerarys1[0]:
            print(f"Traveler:{itinerarys1[0]}, Flight: {flight[0]}, To:{flight[2]}")
            pass
def main():
    iteneraries=[
        ("Alice",("Flabc", "New York","London"),("FL123"," London", "Paris")),
        ("Bob",("FL456", "Tokyo", "San Francisco"),("Fl789","San Francisco", "New York")),
]

def show_iteneraries(itinerarys):
   for itenary in itinerarys:
      traveler, flights=itinerarys[0], itinerarys[1]
      print(f"\nTraveler: {traveler}")
      for flight in flights:
         print(f" flight: {flight[0]}, From: {flight[1]}, To: {flight[2]},")
if choice=="1":
          show_iteneraries()
elif choice== "2" :
          traveler=input("Enter traveler's name: ") 
          find_travelers_itenarary(itinerarys, traveler)
          print(traveler, itinerarys[0])
elif choice== "3" :
          origin=input("Enter departure city: ")
          show_city_itinerary(itinerarys1, origin)

       