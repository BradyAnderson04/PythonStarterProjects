from groupy.client import Client
from secret import bot_token, group_name

client = Client.from_token(bot_token)
group = [group for group in client.groups.list_all() if group.name == group_name][0]