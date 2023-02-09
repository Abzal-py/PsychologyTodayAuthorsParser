import requests

def get_data(url):
    """
        URL PLEASE
    """
    #Get header
    headers = {
        "accept" : "*/*",
        "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    # Request to page and save
    r = requests.get(url = url, headers = headers).content

    return r