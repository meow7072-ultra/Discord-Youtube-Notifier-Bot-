import os
import discord
import googleapiclient.discovery
import googleapiclient.errors
import datetime
import json

from discord.ext import commands, tasks

DISCORD_TOKEN = "DISCORD BOT TOKEN"
YOUTUBE_API_KEY = "YOUTUBE API KEY"
YOUTUBE_CHANNEL_ID = "YOUTUBE CHANNEL ID"
DISCORD_CHANNEL_ID = 123456 # replace it with the channel id
CHECK_INTERVAL = 10 # this make it check in your youtube channel if u have a new video (by minute)  


meow = commands.Bot(command_prefix = "not-matter", intents = discord.Intents.all())


youtube = googleapiclient.discovery.build(
    "youtube", "v3", developerKey = YOUTUBE_API_KEY
)


LAST_VIDEO_FILE = "last_video.json"

def get_latest_video():
    request = youtube.search().list(
        part = "snippet",
        channelId = YOUTUBE_CHANNEL_ID,
        maxResults = 1,
        order = "date",
        type = "video"
    )
    response = request.execute()
    
    if response['items']:
        video = response['items'][0]
        video_id = video['id']['videoId']
        title = video['snippet']['title']
        description = video['snippet']['description']
        publish_time = video['snippet']['publishTime']
        thumbnail_url = video['snippet']['thumbnails']['high']['url']
        
        return {
            "id": video_id,
            "title": title,
            "description": description,
            "publish_time": publish_time,
            "thumbnail_url": thumbnail_url
        }
    return None

def save_last_video(video_data):
    with open(LAST_VIDEO_FILE, 'w') as f:
        json.dump(video_data, f, indent = 4)

def load_last_video():
    try:
        with open(LAST_VIDEO_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"id": None}

@tasks.loop(minutes = CHECK_INTERVAL)
async def check_for_new_videos():
    print(f"Checking for new videos at {datetime.datetime.now()}")
    
    try:
        latest_video = get_latest_video()
        last_video = load_last_video()
        
        if latest_video and latest_video["id"] != last_video.get("id"):
            channel = meow.get_channel(DISCORD_CHANNEL_ID)
            if channel:
                video_url = f"https://www.youtube.com/watch?v={latest_video['id']}"
                
                embed = discord.Embed(
                    title = latest_video["title"],
                    description = "WATCH IT NOW VIDEO :3",
                    color= 0xff0000,
                    url= video_url
                )
                embed.set_author(name = "New YouTube Video!")
                embed.add_field(
                    name = "description", 
                    value=latest_video["description"][:200] + "..." if len(latest_video["description"]) > 200 else latest_video["description"],
                    inline=False
                    )
                embed.set_image(url = latest_video["thumbnail_url"])
                
                await channel.send("@everyone", embed=embed)
                
                save_last_video(latest_video)
                print(f"New video found and posted: {latest_video['title']}")
            else:
                print(f"Could not find Discord channel with ID {DISCORD_CHANNEL_ID}")

    except Exception as e:
        print(f"Error checking for videos: {e}")

@meow.event
async def on_ready():
    print(f"onilne {round(meow.latency * 1000, 2)}ms")
    
    await check_for_new_videos()

meow.run(DISCORD_TOKEN)