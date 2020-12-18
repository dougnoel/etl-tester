import zipfile

zipfilePath = "zipfile.zip"
tempDir = "temp"

with zipfile.ZipFile(zipfilePath, 'r') as zip_ref:
    zip_ref.extractall(tempDir)
    
print(zipfilePath + " Extracted")