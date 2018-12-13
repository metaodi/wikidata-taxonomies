# swissadvisor - taxonomies

## Installation

```bash
# create a new virtualenv
virtualenv --no-site-packages _notebook
source ./_notebook/bin/activate

# install dependencies
pip install -r requirements.txt

# if you want to export the graphs as image, you need graphviz
sudo apt-get install graphviz
```


## Usage

Run the jupyter notebooks:

```
./_notebook/bin/jupyter notebook
```


IPTC notebook: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/metaodi/wikidata-taxonomies/master?filepath=IPTC%20Taxonomy.ipynb)
User needs notebook: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/metaodi/wikidata-taxonomies/master?filepath=User%20Needs.ipynb)
