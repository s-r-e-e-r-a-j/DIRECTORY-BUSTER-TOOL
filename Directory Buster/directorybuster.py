import requests
import argparse

print("""

###############sreeraj###########################################################################################################sreeraj#########################################################
###############################sreeraj########################################################sreeraj################################################sreeraj#####################################
##############sreeraj##############################sreeraj###################################################sreeraj#############################################################################

  _____    _                        _                              ____                  _                     _______                   _ 
 |  __ \  (_)                      | |                            |  _ \                | |                   |__   __|                 | |
 | |  | |  _   _ __    ___    ___  | |_    ___    _ __   _   _    | |_) |  _   _   ___  | |_    ___   _ __       | |      ___     ___   | |
 | |  | | | | | '__|  / _ \  / __| | __|  / _ \  | '__| | | | |   |  _ <  | | | | / __| | __|  / _ \ | '__|      | |     / _ \   / _ \  | |
 | |__| | | | | |    |  __/ | (__  | |_  | (_) | | |    | |_| |   | |_) | | |_| | \__ \ | |_  |  __/ | |         | |    | (_) | | (_) | | |
 |_____/  |_| |_|     \___|  \___|  \__|  \___/  |_|     \__, |   |____/   \__,_| |___/  \__|  \___| |_|         |_|     \___/   \___/  |_|
                                                          __/ |                                                                            
                                                         |___/                                                                             
                                                                                                                                                                                                                                       
################sreeraj################################################################################################################################sreeraj#################################### 
#######################################sreeraj#########################################################sreeraj###########################################################sreeraj##################
#####################################################sreeraj#########################################################sreeraj######################################################################


\n
******************************************************
\n
* Copyright of Sreeraj,2024                      *\n
\n
* www.youtube.com/@debugspecter                  *\n
\n
*  https://github.com/s-r-e-e-r-a-j              *\n
*****************************************************
\n
             """)
print("\n")
print("Searching for hidden paths")
print("\n")
# Function to check each URL path, print status, and write only found paths to the file
def check_path(url, output_file):
    try:
        response = requests.get(url, timeout=3)
        status_code = response.status_code
        
        # Print the status of each URL check to the console
        print(f"[{status_code}] Checking: {url}")

        # Store only relevant results (200 or 403) in the output file
        if status_code == 200 or status_code == 403:
            result = f"[{status_code}] {url}"
            with open(output_file, "a") as f:
                f.write(result + "\n")  # Write to file if found
    except requests.RequestException:
        # Print error on screen for debugging, skip writing to file
        print(f"[ERROR] Failed to reach: {url}")

# Main function to handle arguments and run the brute-force
def main():
    parser = argparse.ArgumentParser(description=" Directory Buster Tool")
    parser.add_argument("url", help="Target URL (e.g., http://example.com)")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    parser.add_argument("-o", "--output", default="found_results.txt", help="Output file to save found paths (default: found_results.txt)")

    args = parser.parse_args()
    target_url = args.url.rstrip("/")
    output_file = args.output

    # Clear the output file before starting
    with open(output_file, "w") as f:
        f.write("This Tool Founded  Results. Check This Urls In  WebBrowser. There Is A Chance In Hidden Directories,Hidded Webpages,Hidden Files Exist In This URLS:\n")

    # Read wordlist and check each path
    with open(args.wordlist, "r") as file:
        for line in file:
            path = line.strip()
            full_url = f"{target_url}/{path}"
            check_path(full_url, output_file)

if __name__ == "__main__":
    main()