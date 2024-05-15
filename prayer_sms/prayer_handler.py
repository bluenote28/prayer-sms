from dbhandler import get_random_prayer




def handler(event,context):

    if event['path'] == 'intention':
        return get_random_prayer()





