# Hack_Nite_22

## HOW TO RUN

Type 'help' to get instructions on how to use the bot.
The first time you type help, 6 channels will be created.
Go to your desired channel for accessing the functions listed below.
The prefix for all commands is '$'(except for 'help')

### channel : weather
Type '$<city_name>' to find out the weather in the specified city.
This will tell you the temperature, feels like, min temperature , max temperature, humidity, pressure and description of weather.

### channel : jokes
Type '$make me laugh' to get a joke.

### channel : currency-exchange
Type '$<quantity_of_money> <currency_1>-<currency_2>' to convert amount from currency_1 to currency_2.
Use currency abbreviation for writing currency...example:INR,

### channel : hand-cricket
Type '$play to start playing hand cricket with the bot. 
You will start batting. Enter a number between 1 and 6 as your runs, and press enter.
Keep doing this till the bot tells you you're out. 
When you get out, the bot will start batting.
Enter a number between 1 to 6, till the bot gets out, or exceeds the runs you made.

### channel : covid-statistics
Type '$<country_name>' to get a pie chart of healthy population,active cases and deaths in that country.
The first letter of the country should be capital.

### channel : maps
Type '$<city_1>-<city_2>' to find the distance and travel time between two cities.

## WHAT THE PROJECT DOES
Our discord bot is a TRAVEL GUIDE.

### Weather
Shows the weather details of any city:
Description
Temperature
Feels Like
Minimum Temperature
Maximum Temperature
Humidity
Pressure

### Maps
Finds the Distance(km) and Travel time(hours) between two cities.

### Currency Exchange Rates
Converts an amount from one currency into another currency.

### Covid Statistics
Displays a pie chart containing Healthy population,Active cases,Deaths data of a country.

### Hand Cricket
The plays hand-cricket with a user wherein user bats first followed by the bot. 
Range of runs to be entered: 1 to 6

### Jokes
Generates a random joke.

## HOW IT WAS BUILT
Coded in python
### Python Libraries Used :
*discord
*requests
*os
*random
*json
*emoji
*dotenv
*numpy
*matplotlib.pyplot

## CHALLENGES FACED
#### *Accessing API keys for free
#### *Limit on the number of url calls

