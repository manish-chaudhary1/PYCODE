x =  "https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Country_Flags.csv"
import pandas as pd
import os
try:
    import requests_oauthlib
except ImportError:
    print("The 'requests' library is not installed. Please install it using 'pip install requests'.")
    raise
file = pd.read_csv(x)
# Create a folder named 'flags' if it doesn't exist
os.makedirs('flags', exist_ok=True)

# Iterate through the links in the third column and download the images
for idx, url in enumerate(file.iloc[:, 2]):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'flags/flag_{idx + 1}.png', 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download image from {url}")