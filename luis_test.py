from logging import log
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
from config import TestConfig


CONFIG = TestConfig()






def test_luis_intent():
    """Check LUIS non-regression on *Top intent*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    request ='book a flight from Tunis to Toronto between 22 October 2021 to 5 November 2021, for a budget of $3500'

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)

    check_top_intent = 'BookFlight'
    is_top_intent = response.top_scoring_intent.intent
    assert check_top_intent == is_top_intent




def test_luis_origin():
    """Check LUIS non-regression on *Origin*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    request ='book a flight from Tunis to Toronto between 22 October 2021 to 5 November 2021, for a budget of $3500'

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)
    
    check_origin = 'tunis'
    all_entities = response.entities
    
    for i in range(0, len(all_entities)):
        if all_entities[i].type == 'or_city':
            is_origin = all_entities[i].entity
    
    assert check_origin == is_origin


def test_luis_destination():
    """Check LUIS non-regression on *Destination*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    request ='book a flight from Tunis to Toronto between 22 October 2021 to 5 November 2021, for a budget of $3500'

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)
    
    check_destination = 'toronto'
    all_entities = response.entities
    print('les entités',all_entities)
    for i in range(0, len(all_entities)):
        if all_entities[i].type == 'dst_city':
            is_destination = all_entities[i].entity
    
    assert check_destination == is_destination

def test_luis_date():
    """Check LUIS non-regression on *Date*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    request ='book a flight from Tunis to Toronto between 22 October 2021 to 5 November 2021, for a budget of $3500'

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)
    
    check_date = '22 october 2021'
    all_entities = response.entities
    
    for i in range(0, len(all_entities)):
        if all_entities[i].type == 'str_date':
            is_date = all_entities[i].entity
    
    assert check_date == is_date

def test_luis_budget():
    """Check LUIS non-regression on *Budget*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    request ='book a flight from Tunis to Toronto between 22 October 2021 to 5 November 2021, for a budget of $3500'

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)
    
    check_budget = '$ 3500'
    all_entities = response.entities
    
    for i in range(0, len(all_entities)):
        if all_entities[i].type == 'budget':
            is_budget = all_entities[i].entity
    
    assert check_budget == is_budget


def test_score_intent():
    """Check LUIS non-regression on *Score*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    request ='book a flight from Tunis to Toronto between 22 October 2021 to 5 November 2021, for a budget of $3500'

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)
    
    check_score = 0.90
    is_score = response.top_scoring_intent.score
    
    assert check_score < is_score
