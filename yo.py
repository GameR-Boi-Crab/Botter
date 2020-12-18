import discord
from discord.ext import commands


class MyClient(discord.Client):


    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        word_list = ['FUCK', 'fuck', 'Fuck', 'Sex', 'SEX', 'sex', 'noob', 'Noob']

        # don't respond to ourselves
        if message.author == self.user:
            return

        messageContent = message.content
        if len(messageContent) > 0:
            for word in word_list:
                if word in messageContent:
                    await message.delete()
                    await message.channel.send(f'Do not say that!')

        messageattachments = message.attachments
        if len(messageattachments) > 0:
            for attachment in messageattachments:
                if attachment.filename.endswith(".dll"):
                    await message.delete()
                    await message.channel.send("No DLL's allowed!")
                elif attachment.filename.endswith('.exe'):
                    await message.delete()
                    await message.channel.send("No EXE's allowed!")
                else:
                    break


client = MyClient()
client.run('NzY4NjkzODkwNTQ2Nzk0NTQ2.X5EL-Q.ceUatLY399HmEXYRcE9j_ryt8hk')