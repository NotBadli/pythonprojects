import time, zipfile

ZIP_DIRECTORY = "C:/Users/illia/Downloads/Options/optionsLC 1.17.1"
ZIP_DESTINATION = "C:/Users/illia/AppData/Roaming/.minecraft"

with zipfile.ZipFile(ZIP_DIRECTORY, 'r') as zip_ref:
    zip_ref.extractall(ZIP_DESTINATION)
