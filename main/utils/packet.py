import json

def unpacking(request):
    """ 
        Convert http request data into json data
    """
    request_body_data = request.body
    request_json_data = json.loads(request_body_data)
    return request_json_data

