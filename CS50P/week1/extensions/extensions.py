filename = input("File name: ")
filename = filename.strip().lower()

extensions = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

for i in extensions:
    if filename.endswith(i):
        print(extensions[i])
        exit(0)

print("application/octet-stream")
