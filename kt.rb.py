import requests
import time

def remove_bg(image_path):
    api_key = "masukkan API key di sini"
    url = "https://api.remove.bg/v1.0/removebg"
    image_file = open(image_path, "rb")
    
    headers = {
        "X-API-Key": api_key
    }

    data = {
        "image_file": ("image_file.jpg", image_file, "image/jpeg")
    }

    response = requests.post(url, headers=headers, data=data, files=data) 
    image_file.close()

    if response.status_code != requests.codes.ok:
        raise Exception("API error: " + response.text)
    
    output_filename = "output/kt.rb_" + str(int(time.time())) + ".png"
    
    with open(output_filename, "wb") as out:
        out.write(response.content)

    return output_filename

image_path = input("Masukkan path gambar: ")
output_path = remove_bg(image_path)
print("Gambar yang telah dihapus latar belakangnya tersimpan di", output_path)
