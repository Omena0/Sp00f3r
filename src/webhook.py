import discord_webhook as wh
embed = wh.DiscordEmbed(f'File Opened','Your file has been opened')
webhook = wh.DiscordWebhook('https://discord.com/api/webhooks/1188101684258418778/Qtm9-un68Eh_XUQzWFTI47AMlqjlS2pS82C0ll4HWfm1T2fTgt0cNPwiZoP_s9Yi_Lr_')
webhook.add_embed(embed)
webhook.execute()