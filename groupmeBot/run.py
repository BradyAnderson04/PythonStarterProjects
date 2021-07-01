''' a function that interfaces w/ groupme api '''
import time
from groupy.api.messages import Messages
from groupy.api.attachments import Mentions
from clientSetup import client, group
from app import respond

print('Bot online --------\n')

# keep track of the last message seen in the group
last_seen = group.messages.list()[0].id
# student preferences
TIME = ""
CLASS = ""
TUTOR_PREFERENCE = ""

while True:

    # get messages posted after the last seen message
    new_messages = group.messages.list_after(last_seen)

    if len(new_messages.items) > 0:

        last_seen = new_messages[0].id

        # process all new messages
        for message in new_messages:
            print(message)

            # only respond if the bot was mentioned
            if len(message.attachments) > 0:
                for attachment in message.attachments:
                    if isinstance(attachment, Mentions):
                        for i, _id in enumerate(attachment.user_ids):
                            if _id == client.user.get_me()['id']:

                                # remove the mention from the message
                                loci = attachment.loci[i]
                                content = message.text[:loci[0]] + message.text[loci[1]+loci[0]+1:]

                                # generate response
                                group.post(respond(content))
                                            
        time.sleep(1)
