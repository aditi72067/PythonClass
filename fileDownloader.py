import requests

def download_file(url, file_name):

    file_name=f"(file_name).{url.split('.')[-1].lower()}"
    # Send a GET request to the provided url
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        print(f"Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":
    url = 'https://github.com/upessocs/B1B2/blob/main/fileOrganizerGui/Organizer.zip'
    file_name = 'FileName.zip'
    download_file(url, file_name)
