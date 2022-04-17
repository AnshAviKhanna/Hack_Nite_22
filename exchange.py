import discord
def ex_curr(data,cur_1,cur_2,val):
    conversion_rate=data['conversion_rate']
    message=discord.Embed(title='Currency Exchange Rate',color=0x76EE00)
    message.add_field(name='Conversion :',value=val+' '+cur_1+'='+str(float(val)*conversion_rate)+' '+cur_2,inline=False)
    #message.add_field(name=cur_2,value=' ',inline=False)
    return message
