#Bot discord pour récupérer des infos sur un compte tiktok
#
#replace token at line 43
#
#Créé par @edeme_ sur Tiktok

#impots diverses
import discord
from discord.ext import commands
from TikTokApi import TikTokApi
import nest_asyncio

#REMPLACEZ LA VALEUR PAR VOTRE TOKEN D'API
your_token = ""

#initialisation de l'asynchrone
nest_asyncio.apply()

#template du message de réponse
txtTemplate = "Information about {0}'s account :\n \
                Followers : {1}\n \
                Video count : {2}\n \
                Heart count : {3}\n"

#initialisation des varaibles
bot = commands.Bot(command_prefix= "!", description = "Bot de edeme_")
api = TikTokApi()
# username = 'edeme_'

#fonction de renvoi des inforamtions d'un utilisateur
async def parse_User(userToFind):
    user = api.get_instance().get_user(username = userToFind).get('userInfo').get('stats')
    return txtTemplate.format(userToFind, user.get('followerCount'), user.get('videoCount'), user.get('heartCount'))

#evénement d
@bot.event
async def on_ready():
    print("Ready !")

#événement de retour
@bot.command()
async def getUser(ctx, user):
    user = await parse_User(user)
    await ctx.send(user)

#lancement du bot
bot.run(your_token)





