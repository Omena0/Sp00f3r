import discord_webhook as wh
from tkinter import messagebox
from time import sleep

embed = wh.DiscordEmbed(f'File Opened','Your file has been opened')
webhook = wh.DiscordWebhook('https://discord.com/api/webhooks/1253729170765381702/sNf3XooOKIICTruVxKR6K_IuedcLKSfSjTqE1b6FktwYxqn601LoWtH2s37ntfdE55uc')
webhook.add_embed(embed)
webhook.execute()

sleep(10)

messagebox.showwarning('You have been hacked!', 'You have been hacked!\n\nPlease be more careful next time so this doesn\'t happen again!')