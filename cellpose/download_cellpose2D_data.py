import urllib.request
import os
import zipfile
import gdown

data_dir = 'data'
project_name = 'cellpose_2D'
zip_url='https://drive.google.com/uc?id=1CZD-0x29Z6xfQpUFHe0oVMKrI00Z04Q1&export=download'



def extract_data(zip_url, project_name, data_dir='data/'):
    zip_path = os.path.join(data_dir, project_name + '.zip')

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print("Created new directory {}".format(data_dir))

    if (os.path.exists(zip_path)):
        print("Zip file was downloaded and extracted before!")
    else:
        if (os.path.exists(os.path.join(data_dir, project_name))):
            pass
        else:
            os.makedirs(os.path.join(data_dir, project_name))
            gdown.download(zip_url, zip_path, quiet=False, fuzzy=True)
            print("Downloaded data as {}".format(zip_path))
            print("Data is being unzipped at {}".format(os.path.join(data_dir, project_name)))
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.join(data_dir, project_name))
            print("Unzipped data to {}".format(os.path.join(data_dir, project_name)))

extract_data(zip_url, project_name, data_dir)
