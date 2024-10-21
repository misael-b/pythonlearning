date = "Monday 2019-03-18"
time = "10:05:34 AM"
astronautCount = input("Enter number of astronauts: ")
astronautStatus = "ready"
averageAstronautMassKg = 80.7
crewMassKg = int(astronautCount) * averageAstronautMassKg
fuelMassKg = 760000
shuttleMassKg = 74842.31
totalMassKg = fuelMassKg + shuttleMassKg + crewMassKg
fuelTempCelsius = -225
fuelLevel = "100%"
weatherStatus = "clear"
def header(text):
  print("-------------------------------------")
  print(text)
  print("-------------------------------------")
header("> LC04 - LAUNCH CHECKLIST")
print("Date: " + date)
print("Time: " + time)
print("")
header("> ASTRONAUT INFO")
print("* count: " + str(astronautCount))
print("* status: " + astronautStatus)
print("")
header("> FUEL DATA")
print("* Fuel temp celsius: " + str(fuelTempCelsius))
print("* Fuel level: " + fuelLevel)
print("")
header("> MASS DATA")
print("* Crew mass: " + str(crewMassKg) + " kg")
print("* Fuel mass: " + str(fuelMassKg) + " kg")
print("* Shuttle mass: " + str(shuttleMassKg) + " kg")
print("* Total mass: " + str(totalMassKg) + " kg")
print("")
header("> FLIGHT PLAN")
print("* weather: " + weatherStatus)
print("")
header("> OVERALL STATUS")
print("* Clear for takeoff: YES")


