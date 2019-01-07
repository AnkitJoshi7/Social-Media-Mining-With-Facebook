import os
import json
import facebook
import my_api_token
if __name__ == '__main__':
    token = my_api_token.tkn
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me', fields='name,location')
    print(json.dumps(profile, indent=4))
    
