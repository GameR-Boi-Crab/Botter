import discord
from discord.ext import commands
import random
from discord.ext.commands import cog


bot = commands.Bot(command_prefix='bo!')
bot.remove_command("help")




@bot.event
async def on_ready():
    activity = discord.Game(name="bo!help")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('Bot is ready')


@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.command(aliases=['8ball', 'test', '8b'])
async def _8ball(ctx, *, question):
    responces = ['As I see it,who knows',
                 'idk',
                 'yes',
                 'no',
                 'not gonna tell you now'
                 ' im not sure but ur def stupid',
                 'No, you dingleberry']
    await ctx.send(f'Questions: {question}\nAnswer: {random.choice(responces)}')


@bot.command()
async def clear(ctx, amount=200):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def cry(ctx, member : discord.Member):
    await ctx.send(f";-; *Some Crying Noises* **{member.display_name}**")


@bot.command()
async def channel(ctx):
    e = discord.Embed(title="The Channel Of My Creator",
                      url="https://www.youtube.com/channel/UCzcTmr3mc-a3QDmGqE1JH7g",
                      description="GameR, One of the Youtuber, Make Sure to Subscribe and press the bell Icon for more Thank You")
    e.set_thumbnail(
        url="https://images-ext-2.discordapp.net/external/hCkkimvAzRW1pO6mydDvsxx-ba31tZBbgNpr9VRopP4/https/yt3.ggpht.com/ytc/AAUvwnj1Ep2zoHqPoIvZSMzXKGseWhnY_nhvboUVadmQbQ%3Ds900-c-k-c0x00ffffff-no-rj?width=473&height=473")
    await ctx.send(embed=e)


@bot.command()
async def invite(ctx):
        e = discord.Embed(title="Botter Invite Link",
                          url="https://discord.com/api/oauth2/authorize?client_id=768693890546794546&permissions=8&scope=bot",
                          description="Botter, One of the Best Bot in all the Discord")
        e.set_thumbnail(url="https://play-lh.googleusercontent.com/ZoDYlydaoXDuPMj17uC_WCozWZKyPOQemOfCHP9t8db3zbBMB4vN0O8-_AzBMKwkPKaI=s180")
        await ctx.send(embed=e)

@bot.command(aliases=['Support', 'SUPPORT'])
async def support(ctx):
    e = discord.Embed(title="Botter's Server of Support",
                          url="https://discord.gg/93STFF8hcx",
                          description="This place is for support of the Bot, If any bug or problem u can join and ask for support")
    e.set_thumbnail(url="https://play-lh.googleusercontent.com/ZoDYlydaoXDuPMj17uC_WCozWZKyPOQemOfCHP9t8db3zbBMB4vN0O8-_AzBMKwkPKaI=s180")
    await ctx.send(embed=e)

Joke = [
    'https://images-ext-1.discordapp.net/external/FX4sdp4OSZegOZB4fV4w7v-wMa4ZjTYZHHuN5XllFYs/https/i.redd.it/veo1ot9l79461.gif?width=591&height=473',
    'https://images-ext-1.discordapp.net/external/PjWoUzvwVk1hrvKzQeW4q5knW1GDWXDa6Y8agzJM1Qw/https/i.redd.it/0ngvkzwvha461.jpg?width=362&height=473',
    'https://images-ext-1.discordapp.net/external/YImauIqpQtAtuKBu1SLSYhG2bi1JPq4UNIrPFISnimk/https/i.redd.it/8hd5dx4w6c461.jpg?width=473&height=473',
    'https://images-ext-2.discordapp.net/external/kCBrjtJf8iN-Ys9uACxkVaMGcU5YAlfWhg_qVjlxaGU/https/i.redd.it/l09tmxnrf8461.png?width=568&height=473',
    'https://images-ext-2.discordapp.net/external/vZDXvhuwd7S0VN_65esN9CNFcS5Zpp6Vj6z114fdQyM/https/i.imgur.com/XASla9Q.gif?width=515&height=473',
    'https://images-ext-2.discordapp.net/external/eVysQHynbc6E8fdOnzzdHQgrUC_47fcC9D1LOqQgwTE/https/i.redd.it/ksl5tptdj9461.gif?width=473&height=473',
    'https://images-ext-2.discordapp.net/external/UDzyoJD0QqByt38NURoKy-DKY4-WV0fF12IFta1Utmg/https/i.redd.it/7o5wc862cc461.jpg?width=655&height=473',
    'https://images-ext-2.discordapp.net/external/5TsLawWeXoa7zdXarlAA2XF_KuffXOiBiwdYQ98_ezg/https/i.redd.it/re4wok7vo9461.jpg?width=383&height=473',
    'https://images-ext-1.discordapp.net/external/JIG6CYuyzYEbPaSanbOuChz1joUQmM7Zc3NQshhjnlY/https/i.imgur.com/q6Uiom3.jpg?width=366&height=473',
    'https://cdn.discordapp.com/attachments/758675079634223114/772332090477510686/Screenshot_20201031-150950.png',
    'https://media.discordapp.net/attachments/758675079634223114/772332090175127572/Screenshot_20201031-151120.png?width=945&height=473']


@bot.command(aliases=['meme', 'MEME'])
async def Meme(ctx):
    await ctx.send(f" {random.choice(Joke)}")


@bot.command()
async def kill(ctx, *,member : discord.Member):
    await ctx.send(f"**{member.display_name}** {random.choice(kill)}")


@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"Unbanned: {user.mention}")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f':lock: Kicked! {member.mention} :lock:')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f':lock: Banned! {member.mention} :lock:')
    


@bot.command(aliases=['avatar'])
async def Avatar(ctx, member: discord.Member):
    await ctx.send(f"||{member.avatar_url}|| *{member.display_name}*")




kill = ['died of COVID-19 RIP', 'sliped and ', 'Again! A drink and drive case!', ' was abducted by aliens',
        'just smelled his socks RIP', ' Died laughing at my memes', 'Just Fell in LAVA *comes out with his skeleton face*', 'tried to get famous on YouTube by live-streaming something dumb. Skydiving while chained to a fridge.', 'creams in terror as they accidentally spawn in the cthulhu while uttering random latin words. Cthulhu grabs AdineVikash by the right leg and takes them to his dimension yelling, "Honey, Dinners ready!"','died from too many sunburns.' ]

kinda_hello= ['yo', 'hoi', 'Nihow!', 'Hola', 'Hi!', 'Hellow!!', 'hElOlOw!']
memes= ['“I went to the doctor the other day and said: “Have you got anything for wind?” So he gave me a kite.”','If you are stuck for cracking a joke then someone might say this! It is an idiom meaning you cannot speak, so the cat is holding your tongue. ', 'To the guy who stole my antidepressants: I hope you’re happy now.' 'Q: What do you get when you combine an insomniac, an agnostic, and a dyslexic? A: Someone who lays awake at night wondering the true meaning of Dog.']


@bot.command(aliases= ['Joke'])
async def joke(ctx):
    await ctx.send(f"{random.choice(memes)}")

@bot.command(aliases= ['warn'])
@commands.has_permissions(ban_members=True)
async def Warn(ctx, user : discord.User, reason=None):
    reason = reason
    await user.send(f":lock:  You! are  Warned for {reason} :lock:")
    await ctx.send(f":lock: {user.mention} has been warned :lock:")




nice_topics= ['“Yesterday is history,tomorrow is a mystery, and today is a gift...thats why they call it present”,― Master Oogway', '“If you only do what you can do, you will never be more than who you are.”―Master Shifu', '"There is no secret ingredient- Ping;Father of po"', '“There are no coincidences in this world.”― Turtle in Kung Fu Panda ', 'Love For All, Hatred For None. – Khalifatul Masih III', ' Change the world by being yourself. – Amy Poehler',
'Every moment is a fresh beginning. – T.S Eliot', 'Never regret anything that made you smile. – Mark Twain'
'Die with memories, not dreams. – Unknown', 'And still, I rise. – Maya Angelou' ]
@bot.command(aliases=['quote'])
async def Quote(ctx):
    await ctx.send(f"{random.choice(nice_topics)}")


@bot.command()
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)

@bot.command(aliases= ['say'])
async def Say(ctx, *, message=None):
     message = message
     await ctx.send(message)

@bot.command(aliases=['Addrole'])
@commands.has_permissions(ban_members=True)
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
 await member.add_roles(role)
 await ctx.send(f":lock: Added **{role}** to **{member.display_name}** :lock:")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = "Verified")
    await member.add_roles(role)

@bot.command(aliases=['hi','yo', 'hoi', 'Nihow!', 'Hola', 'Hellow!!' ])
async def Hi(ctx):
    await ctx.send(f"{random.choice(kinda_hello)}")





class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

@bot.command(aliases=['help'])
async def Help(ctx):
    e = discord.Embed(title="Botter's Help Command, Everything in brief",
                      url="https://newtextdocument.com/64092f5437",
                      description="This is the link for the help of the Botter commands")
    e.set_thumbnail(
        url="https://play-lh.googleusercontent.com/ZoDYlydaoXDuPMj17uC_WCozWZKyPOQemOfCHP9t8db3zbBMB4vN0O8-_AzBMKwkPKaI=s180")
    await ctx.send(embed=e)





bot.run('NzY4NjkzODkwNTQ2Nzk0NTQ2.X5EL-Q.ceUatLY399HmEXYRcE9j_ryt8hk')
