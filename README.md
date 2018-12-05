# swissadvisor - taxonomies

## Installation

```bash
# create a new virtualenv
virtualenv pyenv
source pyenv/bin/activate

# install dependencies
pip install -r requirements.txt

# if you want to export the graphs as image, you need graphviz
sudo apt-get install graphviz
```


## Usage


```bash
source pyenv/bin/activate
python iptc.py
python user_needs.py
```

The library used can generate `.dot` files based on a tree, i.e. we can visualize the tree using `graphviz`
