import re
import requests

def get_quote():
    url = "https://api.quotable.io/random"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "Stay disciplined."

        data = response.json()

        return data.get("content", "Stay consistent.")

    except requests.exceptions.Timeout:
        return "Time is precious. Stay focused."

    except requests.exceptions.RequestException:
        return "Keep pushing forward."

    except Exception:
        return "Stay strong."

    
def get_time():
    url = "https://aisenseapi.com/services/v1/datetime"

    try: 
        response = requests.get(url, timeout=5)

        if response.status_code !=200:
            return "it worked"
        
        data = response.json()
      
        return data.get("datetime")
    
    except requests.exceptions.Timeout:
        return "xxxx"
    except requests.exceptions.RequestException:
        return "xxxx"

    except Exception:
        return "xxxx"


print(get_time())