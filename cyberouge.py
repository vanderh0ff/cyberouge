import requests
import lxml.html as html

def main():
    print("welcome to cyberouge")

def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        html.fromstring(response.text)
    else:
        break


if __name__ == "__main__":
    main()
