# IPDS
IMAGE-BASED PHENOTYPE DETECTION SYSTEM IN SUSPENSION CELL CULTURES

This project includes a box design and source code for phenotype diagnosis and status assessment using images of suspension cultures. Quality controls (contamination, amount and speed of recombinant protein production, production efficiency, other abnormal behaviors, etc.) of suspension cultures, which are frequently used in commercial and R&D areas, can be detected only with images after model training without requiring analysis. In this way, diagnosis can be performed quickly and safely without external intervention in the culture environment, by eliminating contamination risks and stress factors.

Working Principle:

Mapping is performed in the RGB color space by detecting particle count and color changes over time in suspension cultures (Mie and Rayleigh scattering changes). The recorded maps are used for inference.

Representation of Mie and Rayleigh Scattering:

<img width="1152" height="295" alt="Ekran Görüntüsü - 2025-08-18 00-06-46" src="https://github.com/user-attachments/assets/71aa18e8-f9b8-4d06-b801-7007b5201c10" />

Suspension Culture Container Selection:

The shape of the container in which the culture will be grown depends on the user's wishes, but the vessel should be transparent and the type of container used in the training data and inference data should be the same. Otherwise, incorrect estimation results will occur because the path (depth) traveled by the light will increase.

Creating the Recording Environment for Capturing Images:

A closed box setup was designed to capture images and block general light from the outside environment. In addition to blocking external light, fixed recording parameters were used during the recording process. The white balance was set to 5200, the ISO to 50, the aperture to 1.75, the lens focal length to 5.96, and the shutter speed to 1/80, and all images were fixed at these settings to be recorded with the same recording device. A household LED bulb with a power output of 6500K, 8400lm, a power output of 9W, a size of 60 × 108mm, and a beam angle of 220° was used as the light source. The dark area was created by lining the inside of a square magenta box-sized cardboard box with black fabric. An opening was created by cutting out an area the size of the area to be scanned to align with the suspension culture. The detailed design of the recording environment is shown in the image below.

<img width="680" height="599" alt="Ekran Görüntüsü - 2025-08-18 00-29-48" src="https://github.com/user-attachments/assets/4fae2bbc-338c-440c-a585-fcd2a2951ae3" />

Creating Image and Measurement Dataset Structures:

The resulting images are collected in a separate folder for each magenta. The collected images are numbered and sorted. An Excel file named "data.xlsx" is created in the same location as the collected images within the folder. The resulting measurement data is processed into the Excel file. When entering data into the Excel file, row 1 is used for the label name, and the column containing the label name is used for entering the measurement data. Each image is sorted by its sequence number, corresponding to the value (row number + 1) in the Excel file, and the resulting sequence is used as a timeline. If there is no measurement data for the image, the corresponding row is left blank. Each column represents a separate measurement dataset and is entered independently. This prevents the columns from interfering with each other during training.

<img width="633" height="466" alt="Ekran Görüntüsü - 2025-08-17 23-06-57" src="https://github.com/user-attachments/assets/fc8b352b-d78a-4a4f-bf5a-05fb3c46e3b6" />


Creating the Training Algorithm:

Images are used as control points. The average RGB color of each image is calculated, and the coordinates along this path are calculated by calculating the shortest distance between two images. After this calculation, the coordinates are written to a separate Excel file along a timeline.

Calculating Intermediate Values of Measurement Data and Adding them to the Model Excel File:

After writing the intermediate RGB coordinates to the model Excel file and determining the total model size, the measurement data is added to the same row as the images. Following this addition, four different calculation methods are used to calculate the intermediate values. For the values of the intermediate estimates, linear increase and decrease calculations, exponential increase and decrease calculations, a combination of linear and exponential increase and decrease calculations, and data expansion methods are used. Each image and measurement data used as a control point are mapped to the next control point, and intermediary value estimates are performed between the two control points.


Combining Trained Models and Recalculating Intermediate Values:

Combining Trained Models with Time-Coherence in Mind:

To combine trained models in time-coherence, the trained models must contain an equal number of images, and the starting point of the suspension cultures must be under the same conditions. Regardless of the similarity of the control points between the combined models, the arithmetic average is calculated based solely on the Z-score of the timeline and the control points. After the control points are combined, the intermediate values are recalculated.

<img width="544" height="357" alt="modelbirlestir" src="https://github.com/user-attachments/assets/8268c36f-e7fe-4d4f-ab6f-6263708244d7" />


Merging Trained Models Without Considering Time Consistency:

A separate algorithm was designed to merge trained models without considering time concurrency. This algorithm aims to merge models that lack the same control points. The control points that show the most similarity between the main model and the secondary models are merged, regardless of the timeline. The data flow is designed to be unidirectional, from the secondary models to the main model. The closest coordinates and measurement data are merged by taking their arithmetic averages. Updated control points and measurement data are written to a separate model, and the calculation of intermediate values is repeated. A distance threshold option was added before model merging. This threshold prevents the merging of dissimilar values, even if the closest control point is found on the model, and thus creating an incorrect model.

<img width="459" height="427" alt="modelbirlestir2" src="https://github.com/user-attachments/assets/9755ee86-9cf2-4666-95a9-34dee7aaa341" />

Inference Algorithms Used:

Minimum Distance and Weighted Scoring-Based Inference Algorithm:

This inference algorithm was designed to use the Excel file used for the trained model. The average RGB value of the inference image is taken and mapped to the nearest coordinate on the trained model. After finding the nearest coordinate, a weighted score (cosine similarity x vector length) is used for numerical data to calculate the percentage similarity value. The percentage similarity between the inference image and the similar coordinate is calculated using a set of values and is defined as the inference set. For textual data, a weighted score is used to calculate the percentage similarity value.

Random Forest Regression Model:

A random forest regression model was created with 10 decision trees for inference of numerical measurement data. The minimum sample size was set at 2 and the maximum branching depth was set at 5. The data source for training the random forest regression model is the numerical sample data within the model's Excel file, and inference is performed using the average RGB value of the inference image.

Artificial Neural Networks:

The input layer size was set to 3 and the hidden layer size to 5 neurons. The output layer was set to a variable number equal to the number of measurement data labels. The epoch number was set to 1000, and the learning rate was set to 0.01 to prevent overfitting. ReLU was selected as the activation function for the hidden layers, and Softmax was selected as the activation function for the output layer to classify the textual measurement data.

3D Mapping for Model Comparisons:

Similarities and differences between the behaviors of the models and the measurement data contained within them are visualized using a 3D mapping method for holistic comparison. The 3D map is designed to be interactive, and the measurement data is plotted on coordinates. Each model is labeled with a random color, providing visual differentiation between the models.

<img width="526" height="459" alt="Ekran Görüntüsü - 2025-08-18 00-30-05" src="https://github.com/user-attachments/assets/b743ea0f-0119-4ccf-a07f-519f14a6577b" />

Inference Results:

The average total accuracy of inferences performed with the Minimum Distance and Weighted Scoring-Based Inference Algorithm was 97.24%, the average total accuracy of inferences performed with Random Forest Regression was 94.22%, and the average percentage accuracy of inferences performed with Artificial Neural Networks was 47.06%.

Inference and Training:

For inference and training, simply run the interface.py file. Documentation is also included within the interface, and you can follow the steps provided. The interface is optimized for Windows operating systems. Currently, problems may occur on Linux and macOS operating systems.

Sample Datasets:

Alfalfa, Agrobacterium tumefaciens, and Escherichia coli suspension cultures, as well as Alfalfa contamination datasets, will be released soon.


