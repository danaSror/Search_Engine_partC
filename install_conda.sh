conda create -y --name py371 python=3.7.1
conda install -y -q --name py371 --file requirements.txt
conda activate py371
python setup.py
conda deactivate