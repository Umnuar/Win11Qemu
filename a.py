import gdown

# ID của file trên Google Drive
file_id = "1GTgc6v8EwKYFQRjAy8FXghXYPKBDZWGJ"
# URL tải file
url = f"https://drive.google.com/uc?id={file_id}"
# Tên file khi tải về
output = "/mnt/win11.zip"

# Tải file
gdown.download(url, output, quiet=False)
print(f"File đã được tải về: {output}")
