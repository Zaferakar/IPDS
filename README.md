# PCSCC
PHENOTYPIC CHARACTERIZATION IN SUSPENSION CELL CULTURES USING IMAGE-BASED SYSTEMS

This project includes a box design and source code for phenotype diagnosis and status assessment using images of suspension cultures.
Quality controls (contamination, amount and speed of recombinant protein production, production efficiency, other abnormal behaviors, etc.) of suspension cultures, which are frequently used in commercial and R&D areas, can be detected only with images after model training without requiring analysis. In this way, diagnosis can be performed quickly and safely without external intervention in the culture environment, by eliminating contamination risks and stress factors.

Image Recording Box Design:

Image Recorder:

Any mobile phone or professional camera can be used. The same photographing parameters should be used for each image during image recording.

Light Source Selection:

The light source should be white. The remaining values ​​can be determined by the user. The same light source should be used for each image. (In cases where Mie and Rayleigh scattering are high, it is recommended to reduce the light intensity to prevent color distortion)

Suspension Culture Container Selection:

The shape of the container in which the culture will be grown depends on the user's wishes, but the vessel should be transparent and the type of container used in the training data and inference data should be the same. Otherwise, incorrect estimation results will occur because the path (depth) traveled by the light will increase.

![Recorder](https://github.com/user-attachments/assets/d21e8cbc-b9f2-456f-912f-a2eaed9bd30f)

Training and Inference Algorithms:

In the Excel file, time-dependent RGB mapping is performed. The created map is used as the trained model. With RGB mapping, the AKAR algorithm, Random Forest Regression Model and Artificial Neural Networks are fed with the same model and the trainings are repeated. After the trainings are repeated, the prediction phase is performed directly. Only the RGB map is kept locally, the models obtained with repeated trainings before inference are not recorded. The models are trained again for each prediction.
The AKAR algorithm detects the closest image on the trained model for phenotype detection and scores it with weighted scoring by performing similarity detection between the two images.
In addition, maps can be compared for a holistic examination of different behaviors of different organisms.
The AKAR algorithm can be trained with both numerical and verbal data sets. While the Random Forest Regression Model is trained only with numerical data, Artificial Neural Networks are trained only with verbal data. Random Forest Regression model and Artificial Neural Networks are integrated into the system to obtain supportive prediction results.

The obtained inference results are presented to the user on the graphic and numerical data interface.
A detailed user guide for training and inferences has been added to the interface.

In addition, the project will be detailed in the future (after the official publication) and the results will be published with sample data sets.
