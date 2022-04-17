import discord
#color=0x00BFFF
features={
  'description':'Description',
  'temp':'Temperature(*C)',
  'feels_like':'Feels Like(*C)',
  'temp_min':'Minimum Temperature(*C)',
  'temp_max':'Maximum Temperature(*C)',
  'humidity':'Humidity',
  'pressure':'Pressure(Pascal)' 
}

def weather_data(data):
  #data=data['main'].update(data['weather'][0])
  del data['icon']
  del data['id']
  del data['main']
  return data

def w_msg(data,location):
  location=location.title()
  message=discord.Embed(title=f'{location} Weather',color=0x00BFFF)
  for key in data:
    message.add_field(name=features[key],value=str(data[key]),inline=False)
  return message
def error_msg(location):
  location=location.title()
  return discord.Embed(title='Error',description=f'Invalid Location',color=0xEE2C2C)