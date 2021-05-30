def set_chart_studio():
    import dotenv
    import os
    import chart_studio

    dotenv.load_dotenv(dotenv.find_dotenv())

    cs_username = os.getenv("cs_username")
    cs_api_key = os.getenv("cs_api_key")
    
    chart_studio.tools.set_credentials_file(username=cs_username, api_key=cs_api_key)
