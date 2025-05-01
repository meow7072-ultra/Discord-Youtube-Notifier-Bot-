# Discord Notifier Bot  

Hi! okey i made this lil tinny bot dor notifier ppl for last vid in yt channel and i luv to make it open sorces cuz why not :3 11!

<p align="center">
  <img alt="gif" src="https://i.pinimg.com/originals/2e/1a/43/2e1a43aa4b2d35c660200ea998643413.gif" width="500px">
</p>

##  What It Does 🌟

- **Auto-Check**: Polls the channel every few minutes (I set the timer very precisely!)  
- **Track Changes**: Stores the last video ID so you only see new uploads—no repeats.  
- **Embed & Ping**: Sends an **@everyone** ping with the link, thumbnail, and a concise description (I trimmed it to 200 characters because long texts can be overwhelming).  
- **Save State**: Persists data in a JSON file. I triple-tested the save/load logic to ensure nothing gets lost.  

<p align="center">
  <img alt="discord_bot.py" src="https://i.pinimg.com/originals/86/a4/b5/86a4b5321cc13077301d80809256870a.gif" width="500px">
</p>

## What You Need ❓

1. **Python 3.8+** 🐍  
2. **Discord Bot Account**  
   - Create one in the [Discord Developer Portal](https://discord.com/developers/applications).  
   - Enable the "Send Messages" and "Embed Links" permissions—these are crucial.  
3. **YouTube Data API Key** 🔑  
   - Get it from the [Google Cloud Console](https://console.cloud.google.com/apis/credentials).  
   - Make sure the **YouTube Data API v3** is enabled.  
4. **Dependencies**  
   ```bash
   pip install discord.py google-api-python-client

<p align="center">
  <img alt="discord_bot.py" src="https://i.pinimg.com/736x/15/69/4b/15694b89f58ba4afbd1c5cc272b72260.jpg" width="500px">
</p>

##  Customization 🎨

- **Embed Appearance**: Tweak embed color, add extra fields like views or publish date in check_for_new_videos().

- **Mentions**: Swap out **@everyone** for a specific role (e.g., @Subscribers) to reduce noise.

- **Interval**: Adjust CHECK_INTERVAL in your .env (1–60 minutes) to control polling frequency.

<p align="center">
  <img alt="discord_bot.py" src="https://i.pinimg.com/originals/5a/76/40/5a7640d54e08ce9db3cff4e7ae427931.gif" width="500px">
</p>

## License 📜
MIT ©**ultimate sigma kitten (it's me :3)**
<p align="center">
  <img alt="discord_bot.py" src="https://i.pinimg.com/736x/d9/37/5c/d9375c35584ecf63a049d9e04da773ff.jpg" width="500px">
</p>
