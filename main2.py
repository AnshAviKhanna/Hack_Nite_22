import discord
from discord.ext import commands
import requests
import os
import random
import json
from weather_guide import *
from joke_generator import *
from cities import *
from exchange import *
from covid import *
import emoji
from dotenv import load_dotenv
load_dotenv()

#TOKEN='OTY0NTE5ODM1ODM5MTI3NTcy.Yll1GA.rqd1dQXtVIyD4RWIK4pEtLMdmhA'  #.env
W_API=os.getenv('Weather_API')#0b8edb7dfce298422a325153cd679c73'  #.env
#GMaps_API='AIzaSyAHhX2NMMFC36O0NDSCWMG_aeQPThxulH4'
C_API=os.getenv('Curr_API')#'4adcc23966bfc709b8924593'  #.env
#client=commands.Bot(command_prefix='!')
command_prefix='$'
'''
command_prefix_w='w@'
command_prefix_j='j@'
command_prefix_c='c@'
command_prefix_tt='td@'
command_prefix_doc='doc@'
command_prefix_covid='covid@'
command_prefix_hc='hc@'
'''
client=discord.Client()
help_count=0
@client.event
async def on_ready():
    #global help_count
    print("Ready to go")
    #help_count=0

r=0
r_bot=0
user_out=False
hc_in=False

@client.event
async def on_message(message):
  global r
  global r_bot
  global user_out
  global hc_in
  global help_count
  username=str(message.author).split('#')[0]
  user_message=str(message.content)
  channel=str(message.channel.name)
  #print(f'{username}: {user_message} ({channel})')
  if message.author==client.user:
    return

  if user_message.lower()=='help':
    if help_count==0: 
        channel_w=await message.guild.create_text_channel('weather')
        channel_td=await message.guild.create_text_channel('maps')
        channel_curr=await message.guild.create_text_channel('currency-exchange')
        channel_covid=await message.guild.create_text_channel('covid-statistics')
        channel_hc=await message.guild.create_text_channel('hand cricket')
        channel_j=await message.guild.create_text_channel('jokes')
    help_count=1
###############
  if user_message.startswith(command_prefix) and channel=='hand-cricket' and hc_in==False:
    hc_in=True
    return

  if user_message.lower()=='help':
    await message.channel.send("      Welcome To Travel Bot\n1.Weather : Go to channel 'weather' & type $<city_name>\n2.Maps : Go to channel 'maps' & type $<city_1>-<city_2> to find Distance and Travel Time\n3.Currency Exchange Rates : Go to channel 'currency-exchange' & type $<amount> <currency_1>-<currency_2> to convert the amount from currency_1 to currency_2\n4.Covid Statistics  : Go to channel 'covid-statistics' & type $<country_name>\n5.Feeling bored waiting for your flight? We got you! : Go to channel 'hand-cricket' & type $play\n6.Jokes : Go to channel 'jokes' & type $make me laugh")
###############
  if user_message not in ['1','2','3','4','5','6'] and channel=='hand-cricket' and hc_in==True:
    await message.channel.send("Go Slow Tiger {}".format(emoji.emojize(":grinning_face:")))
    return
  bot_num=random.choice(['1','2','3','4','5','6'])
  if user_out==False and channel=='hand-cricket' and hc_in==True:
    while(user_message!=bot_num):
        await message.channel.send(f"BOT : {bot_num}")
        r+=int(user_message)
        await message.channel.send(f"USER : {r}*")
        bot_num=random.choice(['1','2','3','4','5','6'])
        return
    await message.channel.send(f"BOT : {bot_num}")
    await message.channel.send("USER got OUT")
    user_out=True
    await message.channel.send("BOT's Batting")
    return
  elif hc_in==True and channel=='hand-cricket':
    bot_num1=random.choice(['1','2','3','4','5','6'])
    while(user_message!=bot_num1):
      await message.channel.send(f"BOT : {bot_num1}")
      r_bot+=int(bot_num1)
      await message.channel.send(f"BOT : {r_bot}*")
      if r_bot>r and channel=='hand-cricket':
        await message.channel.send("BOT WON {}".format(emoji.emojize(":middle_finger:")))
        r_bot=0
        r=0
        user_out=False
        hc_in=False
        await message.channel.send("--------------------")
        return
        
      bot_num1=random.choice(['1','2','3','4','5','6'])
      return
    await message.channel.send(f"BOT : {bot_num1}")
    await message.channel.send("BOT got OUT!!!")
  if hc_in==True and r>r_bot and channel=='hand-cricket':
    await message.channel.send("YOU WIN {}".format(emoji.emojize(":partying_face:")))
    r_bot=0
    r=0
    user_out=False
    hc_in=False
    return

  elif hc_in==True and r<=r_bot and channel=='hand-cricket':
    await message.channel.send("BOT WON {}".format(emoji.emojize(":middle_finger:")))
    r_bot=0
    r=0
    user_out=False
    hc_in=False
    return
###############
  elif(user_message.startswith(command_prefix) and channel=='weather'):
    location=user_message.replace(command_prefix,'').lower()
    #location=location.lower()
    if len(location)>=1:
      url=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={W_API}&units=metric"

      try:
        data=json.loads(requests.get(url).content)['weather'][0]
        data.update(json.loads(requests.get(url).content)['main'])
        data=weather_data(data)
        await message.channel.send(embed=w_msg(data,location))
      except KeyError:
        await message.channel.send(embed=error_msg(location))

###############
  elif(user_message.startswith(command_prefix) and channel=='jokes'):
    #joke=generate()
    await message.channel.send(embed=generate())
###############
  elif user_message.startswith(command_prefix) and channel=='currency-exchange':
    ind_sp=user_message.index(' ')
    ind=user_message.index('-')
    val=user_message[1:ind_sp]
    cur_1=user_message[ind_sp+1:ind]
    cur_2=user_message[ind+1:]
    url=f'https://v6.exchangerate-api.com/v6/{C_API}/pair/{cur_1}/{cur_2}'
    try:
      data=json.loads(requests.get(url).content)
      await message.channel.send(embed=ex_curr(data,cur_1,cur_2,val))
    except Exception as e:
      await message.channel.send(e)
###############
  elif user_message.startswith(command_prefix) and channel=='covid-statistics':
    country=user_message[1:]
    url=f'https://covid-api.mmediagroup.fr/v1/cases?country={country}'
    data=json.loads(requests.get(url).content)['All']
    await message.channel.send(file=situation(data))
###############
  elif user_message.startswith(command_prefix) and channel=='maps':
    ind=user_message.index('-')
    city_1=user_message[1:ind]
    city_2=user_message[ind+1:]
    #url='https://nominatim.openstreetmap.org/search?format=json'
    #response_1= requests.get(f"{url}&country={city_1}")
    #data_1= response_1.json()[0]
    #response_2= requests.get(f"{url}&country={city_2}")
    #data_2= response_2.json()[0]
    await message.channel.send(embed=get_data(city_1.lower(),city_2.lower()))


client.run(os.getenv('TOKEN'))