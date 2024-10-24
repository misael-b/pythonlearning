engine_indicator_light = "red blinking"
space_suits_on = True
shuttle_cabin_ready = True
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 200
shuttle_speed = 15000

if engine_indicator_light == "green":
   print("engines have started")
elif engine_indicator_light == "green blinking":
   print("engines are preparing to start")
else:
   print("engines are off")
  
if crew_status:
  print("Crew Ready")
else:
  print("Crew Not Ready")

if computer_status_code == 200:
  print("Please stand by. Computer is rebooting.")
elif computer_status_code == 400:
  print("Success! Computer online.")
else:
  print("ALERT: Computer offline!")

if shuttle_speed > 17500:
  print("ALERT: Escape velocity reached!")
elif shuttle_speed < 8000:
  print("ALERT: Cannot maintain orbit!")
else:
  print("Stable speed")
fuel_level = 18000
engine_temperature = 2500
engine_indicator_light = "Not red blinking"


if fuel_level < 1000 or engine_temperature > 3500 or \
engine_indicator_light == "red blinking":
  print("ENGINE FAILURE IMMINENT")
elif fuel_level <= 5000 or engine_temperature > 2500:
  print("Check fuel level. Engines running hot.")
elif fuel_level >20000:
  print("Full tank. Engines good.")
elif fuel_level>10000:
  print("Fuel level above 50%. Engines good.")
elif fuel_level >5000:
  print("Fuel level above 25%. Engines good.")
else:
  print("Fuel and engine status pending...")

command_override = False
fuel_level = 21000
engine_indicator_light = "Not red blinking"
if command_override:
  print("Cleared to launch!")
else:
  if fuel_level >20000 and engine_indicator_light != "red blinking":
    print("Cleared to launch!")
  else:
    print("Launch scrubbed!")