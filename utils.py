import os
import yaml
import inspect
# REPLACE THIS WITH YOUR CODE

def get_apikey():
    """
    Reads API key from a configuration file.

    This function opens a configuration file named "apikeys.yml", reads the API key for OpenAI

    Returns:
    api_key (str): The OpenAI API key.
    """
    
    # Construct the full path to the configuration file
    script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    file_path = os.path.join(script_dir, "apikeys.yml")

    with open(file_path, 'r') as yamlfile:
        d = yaml.load(yamlfile, Loader=yaml.SafeLoader)
        API_KEY = d['openai']['api_key']
        
    return API_KEY

if __name__ == "__main__":
    print("API_KEY", get_apikey())