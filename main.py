# Lakeland Mullins
# 4-30-23
# CIS245-309H
# Project Draft
import json, requests

#Main involves putting the URL together and getting the json response for the weather readout.
def main():
  base_url = 'https://api.openweathermap.org/data/2.5/weather'
  appid = 'ee29457eff5ed51786ba2895e731c60b'
  #Use getCity method to get the zip or city from user.
  city = getCity()

  #Puts URL together based on appid and city input.
  url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
  print(url)
  print()

  #Try block here for if the request fails to connect.
  try:
    response = requests.get(url)
  except:
    print("Was not able to connect.")
  unformated_data = response.json()

  #Try block here mainly for dealing with city entries that are not cities.
  try:
    temp = unformated_data["main"]["temp"]
    print(f"The current temp is: {temp}")

    temp_max = unformated_data["main"]["temp_max"]
    print(f"The max temp is: {temp_max}")
  except:
    print("An error occured. Try entering another city.")

# Method to get user input for the city and determines if it is a zip or city entry before returning.
def getCity():

  check = 'f'
  
  while(check == 'f'):
    temp_city = input("Please enter a zip (##### format) or the city's name.")
    #Checks to see if input is just numbers and only 5 of them.
    if temp_city.isnumeric() and len(temp_city) == 5:
      print("You've entered a zip code.")
      check = 't'
    #Checks to see if input is just letters.
    elif(temp_city.isalpha()):
      print("You've given a city name.")
      check = 't'
    else:
      print("Not a valid city try again")
  return temp_city
      
# Method that checks to see if the user wants to check another city.
def another():
  again = ""
  while(again != 'y' or 'n'):
    again = input("Would you like to try another city? y/n")
    if(again == 'y'):
      main()
    elif(again == 'n'):
      break
    else:
      print("Need to answer 'y' or 'n'")


main()
another()
  