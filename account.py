import webbrowser
from prettytable import PrettyTable
from Login_links import platform_registration_links

def display_platforms():
    print("Social Media Platforms:")
    table = PrettyTable(['#', 'Platform', 'Registration URL'])
    for idx, (platform, registration_url) in enumerate(platform_registration_links.items(), start=1):
        table.add_row([idx, platform, registration_url])
    print(table)

def get_platform_choice():
    while True:
        choice = input("Enter the number of the platform you want to create an account for (or 'exit' to quit): ").strip()
        if choice.lower() == 'exit':
            return None
        elif choice.isdigit():
            index = int(choice)
            if 1 <= index <= len(platform_registration_links):
                platform = list(platform_registration_links.keys())[index - 1]
                return platform
            else:
                print("Invalid choice. Please enter a number within the range.")
        else:
            print("Invalid input. Please enter a number.")

def open_registration_page(platform):
    registration_link = platform_registration_links[platform]
    print(f"Opening registration page for {platform}...")
    webbrowser.open(registration_link)

def close_tool():
    print("Closing the Social Media Account Creation Tool...")

def main():
    print("Welcome to the Social Media Account Creation Tool!")
    while True:
        display_platforms()
        platform_choice = get_platform_choice()
        if platform_choice:
            open_registration_page(platform_choice)
            input("Press Enter after completing the registration...")
        else:
            close_tool()
            break

if __name__ == "__main__":
    main()
