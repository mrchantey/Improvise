import requests


if __name__ == "__main__":
    try:
        response = requests.get("http://127.0.0.1:5000")
        print response.body
    except:
        print 'no response'
