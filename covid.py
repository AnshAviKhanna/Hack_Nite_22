import discord
import matplotlib.pyplot as plt
import numpy as np
def situation(data):
    deaths=data['deaths']
    confirmed=data['confirmed']
    recovered=data['recovered']
    active=confirmed-recovered
    population=data['population']
    healthy=population-active-deaths
    
    if deaths!=0:
        y = np.array([healthy,active,deaths])
        mylabels = ['Healthy','Active','Deaths']
        myexplode = [0,0.2,0.1]
    else:
        y = np.array([healthy,active])
        mylabels = ['Healthy','Active']
        myexplode = [0,0.2]
    plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
    plt.savefig("pie.png")
    img=discord.File("pie.png")
    plt.close()
    return img

    #message=discord.Embed(title='Covid Statistics')