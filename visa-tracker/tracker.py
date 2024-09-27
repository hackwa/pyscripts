# User Steps:
# 1. pip install telethon
# 2. Ubuntu : sudo apt install ffplay
#    Windows : install vlc media player
# 3. Create a telegram account and get API_ID, API_HASH at:
# https://core.telegram.org/api/obtaining_API_ID
import asyncio
import os
import time
from PIL import Image
from telethon import TelegramClient

# Update these
API_ID = 123456
API_HASH = 'a9kjkshfdks83'
# File to play when message arrives
MP3_PATH = "piano.mp3"


# Code State
client = TelegramClient('session_name', API_ID, API_HASH)
PLAYING_MUSIC = False


def should_notify(txt, photo):
  pat_bad = [
    "na", "not available",
    "?", "any", "anyone", "facing",
    "issue", "problem", "please", "provide"
  ]
  pat_good = ["available"]
  # Check 1: Bad pattern
  if any(pattern in txt for pattern in pat_bad):
    return False
  # Check 2: No Bad pattern and has media
  if photo is not None:
    return True
  # Check 3: No bad patterns or media but has good patterns
  if any(pattern in txt for pattern in pat_good):
    return True
  return False


async def play_music():
  global PLAYING_MUSIC
  if PLAYING_MUSIC:
    print("Music already active")
    return
  PLAYING_MUSIC = True
  for _ in range(1):
    if os.name == "nt":
      # Start Windows Media Player:
      #  ["powershell", "-c", "start", MP3_PATH]
      # Start VLC Media Player with custom settings -
      #  100 percent default volume and set windows to be minimized
      p = await asyncio.create_subprocess_exec(
        "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
        "--play-and-exit", MP3_PATH
      )
    else:
      p = await asyncio.create_subprocess_exec(
        "ffplay", "-v", "0", "-nodisp", MP3_PATH
      )
    await p.wait()
  PLAYING_MUSIC = False


async def main():
  admin_name = "blackwidowtheavenger"
  g = await client.get_entity("H1B_H4_Visa_Dropbox_slots")
  latest_id = 0
  tasks = set()
  while True:
    async for msg in client.iter_messages(g, limit=1):
      if latest_id == msg.id or not msg.text:
        break
      txt = msg.text.lower()
      notify = should_notify(txt, msg.photo)
      if admin_name not in txt:
        print(notify, time.strftime('%I:%M'), txt)
      if notify:
        if msg.photo:
          photo_path = await msg.download_media(file="photo.jpg")
          Image.open(photo_path).show()
        await client.send_message('me', 'Ping!')
        t = asyncio.create_task(play_music())
        tasks.add(t)
        t.add_done_callback(tasks.discard)
      latest_id = msg.id
    await asyncio.sleep(4)


if __name__ == "__main__":
  with client:
    client.loop.run_until_complete(main())
