"""
Name : download_saved_models.py
Author : Sebastian Orbell
Contact : sebastian.o@btinternet.com
Time    : 14/07/2021 11:33
Desc:
"""
import os
import zipfile

python neural_style/neural_style.py eval --content-image /images/content-images/amber --model /saved_models/candy.pth --output-image /images/output-images --cuda 0


# PyTorch 1.1 moves _download_url_to_file
#   from torch.utils.model_zoo to torch.hub
# PyTorch 1.0 exists another _download_url_to_file
#   2 argument
# TODO: If you remove support PyTorch 1.0 or older,
#       You should remove torch.utils.model_zoo
#       Ref. PyTorch #18758
#         https://github.com/pytorch/pytorch/pull/18758/commits
try:
    from torch.utils.model_zoo import _download_url_to_file
except ImportError:
    try:
        from torch.hub import download_url_to_file as _download_url_to_file
    except ImportError:
        from torch.hub import _download_url_to_file


def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(path=dest_dir)


if __name__ == '__main__':
    _download_url_to_file('https://www.dropbox.com/s/lrvwfehqdcxoza8/saved_models.zip?dl=1', 'saved_models.zip', None, True)
    unzip('saved_models.zip', '')