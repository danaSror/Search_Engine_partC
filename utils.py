import pickle
import requests
import zipfile
import re



def save_obj(obj, name):
    """
    This function save an object as a pickle.
    :param obj: object to save
    :param name: name of the pickle file.
    :return: -
    """
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    """
    This function will load a pickle file
    :param name: name of the pickle file
    :return: loaded pickle file
    """
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


__fid_ptrn = re.compile("(?<=/folders/)([\w-]+)|(?<=%2Ffolders%2F)([\w-]+)|(?<=/file/d/)([\w-]+)|(?<=%2Ffile%2Fd%2F)([\w-]+)|(?<=id=)([\w-]+)|(?<=id%3D)([\w-]+)")
__gdrive_url = "https://docs.google.com/uc?export=download"
def download_file_from_google_drive(url, destination):
    m = __fid_ptrn.search(url)
    if m is None:
        raise ValueError(f'Could not identify google drive file id in {url}.')
    file_id = m.group()
    session = requests.Session()

    response = session.get(__gdrive_url, params = { 'id' : file_id }, stream = True)
    token = _get_confirm_token(response)

    if token:
        params = { 'id' : file_id, 'confirm' : token }
        response = session.get(__gdrive_url, params = params, stream = True)

    _save_response_content(response, destination)    

def _get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def _save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
        
def unzip_file(file_path, target_dir):
    with zipfile.ZipFile(file_path, 'r') as z:
        z.extractall(target_dir)
