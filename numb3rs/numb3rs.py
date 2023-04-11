import re

# Main function
def main():
    print(validate(input("IPv4 Address: ")))

# Validate IP
def validate(ip):
    pattern = r"^(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$"
    if re.match(pattern, ip):
        return True
    else:
        return False

# Call main
if __name__ == "__main__":
    main()