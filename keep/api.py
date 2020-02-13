"""
https://gkeepapi.readthedocs.io/en/latest/

"""

import gkeepapi

keep = gkeepapi.Keep()
success = keep.login(get_user.user_name, get_user.token)

"""
Search function will be default search by string across all options
otherwise specify a type
arg query_string: Thing to search
arg type: search by a type of label/value in google keep api
"""


def search(query_string, type):

    if type == "title":
        # Find by filter function
        gnotes = keep.find(func=lambda x: x.deleted and x.title == query_string)
    elif type == "label":
        # Find by labels
        gnotes = keep.find(labels=[keep.findLabel('todo')])
    elif type == "color":
        # Find by colors
        gnotes = keep.find(colors=[gkeepapi.node.ColorValue.White])
    elif type == "state":
        # Find by pinned/archived/trashed state
        gnotes = keep.find(pinned=True, archived=False, trashed=False)
    else:
        # Find by string
        gnotes = keep.find(query=query_string)

    return gnotes
