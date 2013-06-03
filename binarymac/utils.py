def menulist(active):

    nested = [
        {
            'name': "Incubation",
            'url': '/creations/incubation',
            'active': False,
        },
        {
            'name': "Analyzation",
            'url': '/creations/analyzation',
            'active': False,
        },
        {
            'name': "Experimentation",
            'url': '/creations/experimentation',
            'active': False,
        },
        {
            'name': "Implementation",
            'url': '/creations/implementation',
            'active': False,
        },
        {
            'name': "Documentation",
            'url': '/creations/documentation',
            'active': False,
        },
    ]

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
            'nested': nested,
        },
        {
            'name': "Contact",
            'url': '/contact',
            'active': False,
            'nested': None,
        },
    ]

    for item in menu:
        if active[0] == item['url']:
            item['active'] = True
        if item['nested']:
            for nested in item['nested']:
                if active[1] == nested['url']:
                    nested['active'] = True
    return menu
