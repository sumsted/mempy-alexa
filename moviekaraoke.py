from __future__ import print_function


def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "startPointBreakIntent":
        return start_point_break(intent, session)
    elif intent_name == "pointBreakOneIntent":
        return point_break_1(intent, session)
    elif intent_name == "pointBreakTwoIntent":
        return point_break_2(intent, session)
    elif intent_name == "pointBreakThreeIntent":
        return point_break_3(intent, session)
    elif intent_name == "startHolyGrailIntent":
        return start_holy_grail(intent, session)
    elif intent_name == "holyGrailOneIntent":
        return holy_grail_1(intent, session)
    elif intent_name == "holyGrailTwoIntent":
        return holy_grail_2(intent, session)
    elif intent_name == "holyGrailThreeIntent":
        return holy_grail_3(intent, session)
    elif intent_name == "holyGrailFourIntent":
        return holy_grail_4(intent, session)
    elif intent_name == "imFinishedIntent":
        return i_am_finished(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def get_access_token(session):
    try:
        return session['user']['accessToken']
    except:
        return ''


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome To Movie Karaoke"
    speech_output = "Welcome to Movie Karaoke. " \
                    "Ask Movie Karaoke, start scene. Try to continue the dialogue through the scene."

    reprompt_text = "Ask Movie Karaoke to start a scene."

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Good bye and thanks for all the fish!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def start_point_break(intent, session):
    title = "Point Break"
    should_end_session = False
    session_attributes = {}
    reprompt_text = None

    speech_output = "Special Agent Utah."

    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def point_break_1(intent, session):
    title = "Point Breack"
    should_end_session = False
    session_attributes = {}
    reprompt_text = None

    speech_output = "Just waiting for my set."

    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def point_break_2(intent, session):
    title = "Point Break"
    should_end_session = False
    session_attributes = {}
    reprompt_text = None

    speech_output = "Yeah, it went bad, went real bad. Life sure has a sick sense of humour, doesn't it? Still surfing?"

    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def point_break_3(intent, session):
    title = "Point Break"
    should_end_session = False
    session_attributes = {}
    reprompt_text = None

    speech_output = "You know the rest."

    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def start_holy_grail(intent, session):
    title = "Holy Grail"
    should_end_session = False
    session_attributes = {}
    reprompt_text = None

    speech_output = "Consult the book of Armaments!"

    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def holy_grail_1(intent, session):
    title = "Holy Grail"
    should_end_session = False
    session_attributes = {}
    reprompt_text = None

    speech_output = """
    And Saint Atila raised the hand grenade up on high, saying,
    'Oh, Lord, bless this thy hand grenade that with it thou mayest blow
    thy enemies to tiny bits, in thy mercy.'  And the Lord did grin, and
    people did feast upon the lambs, and sloths, and carp, and anchovies,
    and orangutans, and breakfast cereals, and fruit bats, and large --
    """

    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def holy_grail_2(intent, session):
    title = "Holy Grail"
    should_end_session = False
    session_attributes = {}
    reprompt_text = None

    speech_output = """
    And the Lord spake, saying, First shalt thou take out the
    Holy Pin.  Then, shalt thou count to three, no more, no less.  Three
    shalt be the number thou shalt count, and the number of the counting
    shalt be three.  Four shalt thou not count, nor either count thou two,
    excepting that thou then proceed to three.  Five is right out.  Once
    the number three, being the third number, be reached, then lobbest thou
    thy Holy Hand Grenade of Antioch towards thou foe, who being naughty
    in my sight, shall snuff it.
    """

    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def holy_grail_3(intent, session):
    title = "Holy Grail"
    should_end_session = False
    session_attributes = {}
    reprompt_text = None

    speech_output = "Amen."

    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def holy_grail_4(intent, session):
    title = "Holy Grail"
    should_end_session = False
    session_attributes = {}
    reprompt_text = None

    if get_slot(intent, 'nextNumber', '3') == '3':
        speech_output = "Yes, Three! Boom!"
    else:
        speech_output = "Three, sir!"

    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def i_am_finished(intent, session):
    title = "Holy Grail"
    should_end_session = True
    session_attributes = {}
    reprompt_text = None

    speech_output = "That was fun. See you later."

    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def get_slot(intent, key, default=None):
    try:
        return intent['slots'][key]['value']
    except:
        return default


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
