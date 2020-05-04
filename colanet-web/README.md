# COLANET
### DATASET FOR DRONES COLLISIONS

ColANet, a dataset of collisions that aims to provide a base for training new Machine Learning algorithms that handle the problem of collisions with high efficiency and robustness. We show that  using this dataset is easy to construct new neural network models and test them.

## Getting Started

#### Requirements

[Download the colanet dataset ](https://colanet.qa.pdmfc.com/download_dataset) and place it under colanet-web/public/download/colanet.zip

node version == v12.16.2+
npm version == 6.14.4+

or

Docker version == 19.03.5+

#### Execute

Using docker `docker-compose build && docker-compose up`

or

Using node `npm i && node index.js`

#### Further files on the public folder can be fetched by FILENAME using: 

http://localhost:8000/public/download?download="FILENAME"

example :  [http://localhost:8000/public/download?download="image_to_panda.ipynb"](http://localhost:8000/public/download?download="image_to_panda.ipynb")


#### If you use this dataset or scripts to handle your video dataset, please cite:

@InProceedings{colanet2020,author="Dário Pedro, Andrá Mora, João Carvalho, Fábio Azevedo and José Fonseca",
title="ColANet: A UAV Collision Avoidance Dataset", year="2020",
publisher="Springer International Publishing", pages="53--62",
isbn="978-3-030-45124-0}
