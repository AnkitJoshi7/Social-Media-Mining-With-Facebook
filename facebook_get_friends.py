import os
import facebook
import json
import my_api_token
if __name__ == '__main__':
    token = my_api_token.tkn
    graph = facebook.GraphAPI(token)
    user = graph.get_object("me")
    friends = graph.get_connections(user["id"], "friends")
    print(json.dumps(friends, indent=4))
