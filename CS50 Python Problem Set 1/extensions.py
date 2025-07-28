# dictionary of file extension / media type pairs
web_exts = {
  "gif": "image/gif",
  "jpg": "image/jpeg",
  "png": "image/png",
  "peg": "image/jpeg",
  "pdf": "application/pdf",
  "txt": "text/plain",
  "zip": "application/zip",
  "css": "text/css",
  "pub": "application/epub+zip"
  }

# Ask user for file name
file_name = input("What is the name of your file? ").lower().strip()

# get file extension
file_ext = file_name[-3:]

# if the file extension is not in the dictionary returns default media type
# otherwise print the media type
print(web_exts.get(file_ext, "application/octet-stream"))
