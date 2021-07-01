'''Python Chatbot template created for CS Club @ IU '''
import TutorData
import TutorData.emailCheck as ec

'''Template Contributors - Wade Fletcher and Brady Anderson '''
'''Tutor session scheduler Chatbot created for Luddy Tutors'''
'''Tutor Scheduler Contributors - Brady Anderson '''

'''
Essential
    -complete!
Non-Essential
    1.Send calendar invite to tutor and student
'''

# global configs
USER_TEMPLATE = "[USER]: "  # prefix for user input messages
BOT_TEMPLATE = "[Steve]: "  # prefix for bot output messages
STARTUP_MESSAGE = """       
+================================+
  Tutor Scheduler  
  Copyright CS Club @IU 
+================================+
What class do you want to be tutored in?
"""  # message to be printed at the begining of script execution

# student preference object here
STUDENT_PREFERENCE = {'Time':None, 'Day': None, 'Tutor': None, 'Class':None, 'Email':None}
PUNCTUATION = "!#$%&'()*+, -/:;<=>?[\]^_`{|}~"

def respond(message):
    """Given a user's input message, take relevant data and prompt for more"""
    # remove capitalization from input
    message = message.lower()
    # remove all punctuation from input
    message = "".join([m for m in message if m not in PUNCTUATION])
    # change all spaces to single spaces
    message = " ".join(message.split())

    # this is the bag-of-words we discussed earlier
    student_response = message.split()

    # extract what data we can from our bag of words
    # gather student details - time, class, preffered tutor
    for word in student_response:
        print(word)
        try:
            # the time can be assumed here since 130 will always be 1:30
            # covert to proper format to be handled
            minutes = int(word[1:])/60
            time = int(word[0]) +  minutes
            print(time)
            STUDENT_PREFERENCE["Time"] = time
        except ValueError:
            pass

        # cleaning data input for analysis
        word = word[0].upper() + word[1:]
        if word in TutorData.DAYS:
            STUDENT_PREFERENCE["Day"] = word

        if word in TutorData.COURSES:
            STUDENT_PREFERENCE["Class"] = word

        if word in TutorData.NAMES:
            STUDENT_PREFERENCE["Tutor"] = word
        if ec.check(word):
            STUDENT_PREFERENCE["Email"] = word

    # if we're missing essential data, let's ask the user for it
    if STUDENT_PREFERENCE["Day"] is None:
        return "What Day of the week works best for you?"
    if STUDENT_PREFERENCE["Time"] is None:
        return "What time works best for you on the day you provided?"
    if STUDENT_PREFERENCE["Class"] is None:
        return "What class do you want tutoring for?"
    if STUDENT_PREFERENCE["Email"] is None:
        return "What is your IU email address?"   
    # match best options
    tutor_match = TutorData.findTutors(time = STUDENT_PREFERENCE['Time'], day = STUDENT_PREFERENCE['Day'],tutor = STUDENT_PREFERENCE['Tutor'], courses = STUDENT_PREFERENCE['Class'])
    bot_response = "I found {} tutors".format(str(len(tutor_match.axes[0])))
    if len(tutor_match) > 1:
        bot_response += " I'd recommend {tutor1} or {tutor2} for {day} at {time}, for {cls}. Only one more thing needed, could you tell me your email?".format(
            time=STUDENT_PREFERENCE["Time"], day=STUDENT_PREFERENCE["Day"], tutor1=tutor_match.iloc[:1]["First"].item(), tutor2=tutor_match.iloc[1:2]['First'].item, cls=STUDENT_PREFERENCE["Class"]
        ) 
    elif len(tutor_match) == 1:
        bot_response += " Setting up meeting with {tutorName}! You should recieve an email soon confirming your appointment with more information. If not please email brjoande@iu.edu".format(
            tutorName=tutor_match.iloc[:1]["First"].item()
        )
        # send calendar invite here

    return bot_response


def main():
    """Main request-response loop"""

    # show the startup message
    print(STARTUP_MESSAGE)

    # start a (kinda) infinite loop, so we can carry on a conversation
    while True:
        # ask the user for input, using the prompt defined in USER_TEMPLATE
        message = input(USER_TEMPLATE)

        # exit the loop (and therefore the program) when the message 'quit' is sent
        # (this is why our loop is only (kinda) infinite)
        if message == "quit" or (STUDENT_PREFERENCE["Time"] != None and STUDENT_PREFERENCE["Day"] != None and STUDENT_PREFERENCE["Email"] != None and STUDENT_PREFERENCE["Class"] != None):
            print("Exiting, bye!")
            break

        # given a user's input message, pass it to the bot response() function and save the result
        response = respond(message)

        # output the bot's response, prefixed by BOT_TEMPLATE and followed by a new line (\n)
        print(BOT_TEMPLATE + response + "\n")


# code in this conditional will run if and only if the script is being run directly
# it won't run if we import our file as a module
if __name__ in "__main__":
    # start the main loop
    main()