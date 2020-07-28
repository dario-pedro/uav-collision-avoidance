# UAV Collision Avoidance

This project contain 5 sub projects:

 - [colanet-web](colanet-web) : Expose the collision videos dataset ColANet and scripts to handle the dataset. Running example at [https://colanet.qa.pdmfc.com/](https://colanet.qa.pdmfc.com/)
 - [generate-dataset](generate-dataset) : Folder to handle images from collision videos of ColANet. The jupyter notebook image_to_panda.ipynb simplify the dataframe creation as it was explained in the paper [ColANet: A UAV Collision Avoidance Dataset](https://link.springer.com/chapter/10.1007/978-3-030-45124-0_5)
 - [train-models](train-models) : Different models study used to detect and generate escape vectors for collisions
 - [experiments](experiments): Latest notebooks to study computer vision algorithm on drones
 - [collision_generate_dataset](collision_generate_dataset): Folder to handle images from collision videos of ColANet. As above, but for regression
