import discord
from discord import File
from discord.ext import commands
import pytube
from pytube import YouTube
import os

client = commands.Bot(command_prefix="#")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('ready to convert...'))



@client.command()
async def convert(ctx, *song):


    if ctx.author.voice is None:
        await ctx.send("You aren't in a VC!")
        return
    print(song)

    youtube = pytube.YouTube(str(song).strip("(,)'"))
    video = youtube.streams.filter(only_audio=True).first()
    await ctx.send("downloading...")
    out_file = video.download(output_path="Your Folderlocation")
    await ctx.send("converting...")
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    os.rename(new_file, "Your Folderlocation/music.mp3")
    outputfile = "music.mp3"
    
    text_channel = client.get_channel(780717938322964500)
    await text_channel.send(file=File("Your Folderlocation" +outputfile))
    os.remove("Your Folderlocation/music.mp3")

client.run('Your Token')
