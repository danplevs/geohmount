from geohmount.config import Config
import chart_studio

def set_chart_studio():
    config = Config.read_config()
    chart_studio.tools.set_credentials_file(username=config.chart_studio_username, api_key=config.chart_studio_api_key)
    print("Credentials OK!")
