from covid import Covid
from random import choice
import discord
from discord.ext import commands
import random
from googlesearch import search as gs
import typing as t
import aiohttp

bot = commands.Bot(command_prefix='.')
status = ['Warzone on Verdansk', 'with Mia Khalifa', 'with Myself', 'Netflix']


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    channel = bot.get_channel(773657772221792260)
    await channel.send('👋🏼')
    await bot.change_presence(activity=discord.Game(name=choice(status)))


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Howdy {member.name}, welcome the KNG Lounge! Help yourself, dabs on the table!'
    )


@bot.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'**Pong!** Your latency is: {round(bot.latency * 1000)}ms, Sir.')


@bot.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['***grumble*** Yes, Sir?', 'Top of the morning to you Sir!',
                 'Hello Sir, how are you?', 'Bot Butler here sir!', '**Wasssuup!**']
    await ctx.send(choice(responses))


@bot.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more',
                 'i have a family, kill them instead', 'Red suit Yegor... will get you.']
    await ctx.send(choice(responses))


@bot.command(name='drop', help='This command returns a place where we should drop')
async def drop(ctx):
    responses = ['Superstore', 'Promenade', 'Dam', 'Train', 'Stadium', 'Port', 'Prison', 'Farmland', 'Quarry',
                 'Pool', 'Storage Town', 'Airport', 'Park', 'TV Station', 'The Spot Magnum doesn\'t like', 'Military Base']
    await ctx.send(f'May I suggest {choice(responses)}, Sir?')


@bot.command(name='credits', help='This command returns the credits')
async def credits(ctx):
    await ctx.send('Made by `Magnum`')


@bot.command(name='creditz', help='This command returns the TRUE credits')
async def creditz(ctx):
    await ctx.send('**No one but me!**')


@bot.command(name='airplane', help='Responds with a random quote from Airplane! 1')
async def airplane(ctx):
    airplane = ['Joey, have you ever been in a turkish prison?',
                'Looks like the foot is on the other hand now, Mr. Kramer!',
                'There\'s no reason to become alarmed, and we hope you\'ll enjoy the rest of your flight. By the way, is there anyone on board who knows how to fly a plane?'
                ]
    response = random.choice(airplane)
    await ctx.send(response)


@bot.command(name='FMJ', help='Responds with a random quote from Full Metal Jacket!')
async def FMJ(ctx):
    FMJ = ['From now on you will speak only when spoken to, and the first and last words out of your filthy sewers will be \'Sir.\' Do you maggots understand that??',
           'Bullsh-t. It looks to me like the best part of you ran down the crack of your mama\'s ass and ended up as a brown stain on the mattress. I think you\'ve been cheated!',
           'Get the f--k down off of my obstacle! NOW! MOVE IT! Or I\'m going to rip your balls off, so you cannot contaminate the rest of the world! I will motivate you, Pvt. Pyle, EVEN IF IT SHORT-D-CKS EVERY CANNIBAL ON THE CONGO!',
           'How tall are you? I didn\'t know they stacked shit this high.'
           ]
    response = random.choice(FMJ)
    await ctx.send(response)

# more commands to be added
# experimental


@bot.command(pass_context=True, name='covid', help='*Gives you Covid stats, \'.\' required')
async def covid(ctx, *, region="US"):  # Defines func with args
    # Gets covid 19 information by region from 'Covid'
    cases = Covid().get_status_by_country_name(region.lower())
    msrona = discord.Embed()  # Creates initial discord embed
    msrona.title = "Corona virus statistics for {0}".format(
        cases["country"])  # Adds a title to embed
    msrona.add_field(name="Confirmed Cases", value="{0}".format(
        cases["confirmed"]))  # Adds a field to embed
    msrona.add_field(name="Active Cases", value="{0}".format(
        cases["active"]))  # Adds a field to embed
    msrona.add_field(name="Deaths", value="{0}".format(
        cases["deaths"]))  # Adds a field to embedhttps
    msrona.add_field(name="Recovered", value="{0}".format(
        cases["recovered"]))  # Adds a field to embed
    msrona.set_image(
        url='https://keystonehealth.org/wp-content/uploads/2020/03/COVID-19-Update_Twitter.jpg')
    await ctx.send(embed=msrona)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    channel = bot.get_channel(773657772221792260)
    if(message.author.id == bot.user.id):
        return
    if 'hello butler' in message.content.lower():
        await channel.send('Oh I hear you need me? Type in .help to see')
    elif 'thank you butler' in message.content.lower():
        responses = ['Indeed, sir!', 'No problem, sir!', '**sir!**']
        await channel.send(choice(responses))
    elif 'drop' in message.content.lower():
        responses = ['Superstore', 'Promenade', 'Dam', 'Train', 'Stadium', 'Port', 'Prison', 'Farmland', 'Quarry',
                     'Pool', 'Storage Town', 'Airport', 'Park', 'TV Station', 'The Spot Magnum doesn\'t like', 'Military Base']
        await channel.send(f'May I suggest {choice(responses)}, Sir?')
    elif 'thanks butler' in message.content.lower():
        responses = ['I got you, sir!', 'No problem, sir!',
                     'I\'ll be waiting for your next order, sir!']
        await channel.send(choice(responses))
    elif 'thanks' in message.content.lower():
        responses = ['I got you, sir!', 'No problem, sir!',
                     'I\'ll be waiting for your next order, sir!']
        await channel.send(choice(responses))
    elif 'hello' in message.content.lower():
        responses = ['***grumble*** Yes, Sir?', 'Top of the morning to you Sir!',
                     'Hello Sir, how are you?', 'Bot Butler here sir!', '**Wasssuup!**']
        await channel.send(choice(responses))
    elif 'die' in message.content.lower():
        responses = ['why have you brought my short life to an end', 'i could have done so much more',
                     'i have a family, kill them instead', 'Red suit Yegor... will get you.']
        await channel.send(choice(responses))
    elif 'airplane' in message.content.lower():
        responses = ['Joey, have you ever been in a turkish prison?',
                     'Looks like the foot is on the other hand now, Mr. Kramer!',
                     'There\'s no reason to become alarmed, and we hope you\'ll enjoy the rest of your flight. By the way, is there anyone on board who knows how to fly a plane?'
                     ]
        await channel.send(choice(responses))
    elif 'FMJ' in message.content.lower():
        responses = ['From now on you will speak only when spoken to, and the first and last words out of your filthy sewers will be \'Sir.\' Do you maggots understand that??',
                     'Bullsh-t. It looks to me like the best part of you ran down the crack of your mama\'s ass and ended up as a brown stain on the mattress. I think you\'ve been cheated!',
                     'Get the f--k down off of my obstacle! NOW! MOVE IT! Or I\'m going to rip your balls off, so you cannot contaminate the rest of the world! I will motivate you, Pvt. Pyle, EVEN IF IT SHORT-D-CKS EVERY CANNIBAL ON THE CONGO!',
                     'How tall are you? I didn\'t know they stacked shit this high.'
                     ]
        await channel.send(choice(responses))
    elif 'credits' in message.content.lower():
        await channel.send('Made by `Magnum`')
    elif 'loadout' in message.content.lower():
        primary = ['M91', 'Kar98k', 'HDR', 'AX-50', 'Finn LMG', 'Bruen', 'PKM', 'M4A1', 'M4A1 9MM', 'M4A1 Socom .458',
                   'Kilo 141', 'FAL', 'FR 5.56', 'Oden', 'M13', 'M13 Blackout', 'Scar', 'AK 47', 'Ram 7', 'Grau 5.56', 'Amax']
        secondary = ['Origin', 'R9-0 Dragon breath', 'Renetti', 'Kali Sticks', 'JOKR', 'Aug', 'P90',
                     'Bizon', 'Coin Special', 'x16', 'Magnum', 'MP5 45rds', 'Fennec', 'D-Eagle', 'RPG', 'MP7', '']
        perk1 = ['Double Time', 'E.O.D', 'Scavenger',
                 'Cold-Blooded', 'Kill Chain', 'Quick Fix']
        perk3 = ['Tune Up', 'Amped', 'Shrapnel',
                 'Battle Hardened', 'Spotter', 'Tracker']
        perks = [f'{choice(perk1)} and {choice(perk3)}']
        lethals = ['C4', 'Claymore', 'Semtex',
                   'Throwing knife', 'Thermite', 'Frag']
        tactical = ['Flash', 'Smoke', 'Stun', 'Baby monitor', 'Gas', 'Stim']
        embed = discord.Embed(
            title="`Loadout`", description="Fully randomized laodout, fill rest of attachments", color=discord.Color.blurple())
        embed.add_field(name="Primary weapon:",
                        value=choice(primary), inline=False)
        embed.add_field(name="Secondary weapon:",
                        value=choice(secondary), inline=False)
        embed.add_field(name="Perks:", value=choice(perks), inline=False)
        embed.add_field(name="Lethal:", value=choice(lethals))
        embed.add_field(name="Tactical:", value=choice(tactical))
        embed.set_image(
            url='https://www.hitc.com/static/uploads/2020/07/Why-is-there-fireworks-in-the-Warzone-and-Modern-Warfare-menu-1024x566.jpg')
        await channel.send(embed=embed)
    elif 'how are you' in message.content.lower():
        await channel.send('Very well, sir. Type in .help to see all my keywords.')
    elif 'lol' in message.content.lower():
        await channel.send('I know I am funny, sir. Thank you.')
    elif 'not you' in message.content.lower():
        await channel.send('Oh, my bad.')
bot.run('TOKEN')
