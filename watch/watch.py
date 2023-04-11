import re

# Main funtion
def main():
    print(parse(input("HTML: ")))

# Parse Function
def parse(s):
    pattern = r'https?:\/\/(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]+)(?=\")'
    match = re.search(pattern, s)
    if match:
        video_id = match.group(1)
        short_url = f'https://youtu.be/{video_id}'
        return short_url
    else:
        return None

# Call main
if __name__ == "__main__":
    main()
