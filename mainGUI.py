import tkinter as tk
from fileDownloader import download_file

# Initialize the Tkinter window
root = tk.Tk()
root.title("File Downloader")
root.geometry("600x250")

# Create a URL entry widget
URLWidget = tk.Entry(root, width=50)
URLWidget.pack(pady=10)

# Create a file name entry widget
fileNameWidget = tk.Entry(root, width=50)
fileNameWidget.pack(pady=10)

# Function to download the file
def download():
    url = URLWidget.get()
    file_name = fileNameWidget.get()
    download_file(url, file_name)

# Create a download button
downloadButton = tk.Button(root, text="Download", command=download)
downloadButton.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

