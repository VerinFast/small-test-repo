# hello_world/main.py
import requests


def test_requests():
    response = requests.get("https://api.github.com")
    print(f"Status Code: {response.status_code}")


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
    test_requests()
