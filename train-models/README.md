# COLANET Training Models


[collision_avoidance_VGG.ipynb](collision_avoidance_VGG.ipynb) - Jupyter notebook to Train VGG Feature Extrator

[FileCopy.ipynb](FileCopy.ipynb) - Jupyter notebook to simplify preparing the datasets for Feature Extractors. 
The Feature Extractors require files in directories on directories:
  - ./data/images/train/collision 
  - ./data/images/train/no_collision 
  - ./data/images/test/collision 
  - ./data/images/test/no_collision
  
[FullModel.ipynb](FullModel.ipynb) - Uses the Features previously processed to train the FE+RNN+FNN model

