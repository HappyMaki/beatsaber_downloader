import urllib.request
import os
import zipfile



def read_file(filename):
    urls = []
    f = open(filename)
    urls = "".join(f.readlines()).split("\n")
    f.close()
    del urls[-1]
    return urls

def download_zip(url, file_path="beatmap_temp"):
    filename = url.replace("https://na.cdn.beatsaver.com/", "")
    fullpath = file_path + "/" + filename
    urllib.request.urlretrieve(url, fullpath)
    return filename, fullpath


def unzip(file, full_path, file_path="beatmap_songs"):
    with zipfile.ZipFile(full_path, 'r') as zip_ref:
        zip_ref.extractall(file_path + "/" + file)
    return

def delete_file(filename):
    os.remove(filename)


urls = read_file("beatmap_data/urls.txt")
print(urls)
for url in urls:
    filename, full_path = download_zip(url)
    unzip(filename, full_path)
    delete_file(full_path)



