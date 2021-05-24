def set_chart_studio():
    import json
    import chart_studio

    with open("/home/daniel/geohmount/code/credentials.json", "r") as credentials_file:
        credentials = json.load(credentials_file)

    cs_credentials = credentials["chart_studio"]
    chart_studio.tools.set_credentials_file(username=cs_credentials["username"], api_key=cs_credentials["api_key"])
