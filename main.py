import requests
from Search_links import platform_search_links

def search_profile(platform, username):
    if platform in platform_search_links:
        search_url = platform_search_links[platform] + username
        try:
            response = requests.get(search_url)
            if response.status_code == 200:
                return search_url
            else:
                print(f"Failed to retrieve data from {platform.capitalize()} for username: {username}")
                return None
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error occurred while trying to access {platform.capitalize()}: {e}")
            return None
    else:
        print(f"Platform '{platform}' not supported.")
        return None

def get_username():
    while True:
        username = input("Please enter the username to search for: ")
        if username.strip():
            return username.strip()
        else:
            print("Username cannot be empty. Please try again.")

def check_username(username):
    found = False
    for platform in platform_search_links.keys():
        profile_link = search_profile(platform, username)
        if profile_link:
            print(f"Username: {username} found on {platform.capitalize()} 👉 {profile_link}")
            found = True
    if not found:
        print(f"No results found for username: {username}")

def main():
    username = get_username()
    check_username(username)

if __name__ == "__main__":
    main()
