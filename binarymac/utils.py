def menulist(active):

    menu = [
        {
            'name': "Home",
            'url': '/',
            'active': False,
            'nested': None,
        },
        {
            'name': "Creative Method",
            'url': '/creative_method',
            'active': False,
            'nested': None,
        },
        {
            'name': "Ideas & Creations",
            'url': '/creations',
            'active': False,
            'nested': None,
        },
    ]

    for item in menu:
        if active[0] == item['url']:
            item['active'] = True
    return menu
