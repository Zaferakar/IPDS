# IPDS
Working Principle:

Mapping is performed in the RGB color space by detecting particle count and color changes over time in suspension cultures (Mie and Rayleigh scattering changes). The recorded maps are used for inference.

Creating the Recording Environment for Capturing Images:

A closed box setup was designed to capture images and block general light from the outside environment. In addition to blocking external light, fixed recording parameters were used during the recording process. The white balance was set to 5200, the ISO to 50, the aperture to 1.75, the lens focal length to 5.96, and the shutter speed to 1/80, and all images were fixed at these settings to be recorded with the same recording device. A household LED bulb with a power output of 6500K, 8400lm, a power output of 9W, a size of 60 × 108mm, and a beam angle of 220° was used as the light source. The dark area was created by lining the inside of a square magenta box-sized cardboard box with black fabric. An opening was created by cutting out an area the size of the area to be scanned to align with the suspension culture. The detailed design of the recording environment is shown in the image below.

Creating Image and Measurement Dataset Structures:

The resulting images are collected in a separate folder for each magenta. The collected images are numbered and sorted. An Excel file named "data.xlsx" is created in the same location as the collected images within the folder. The resulting measurement data is processed into the Excel file. When entering data into the Excel file, row 1 is used for the label name, and the column containing the label name is used for entering the measurement data. Each image is sorted by its sequence number, corresponding to the value (row number + 1) in the Excel file, and the resulting sequence is used as a timeline. If there is no measurement data for the image, the corresponding row is left blank. Each column represents a separate measurement dataset and is entered independently. This prevents the columns from interfering with each other during training.

<img width="1262" height="932" alt="Ekran Görüntüsü - 2025-08-17 23-06-57" src="https://github.com/user-attachments/assets/fc8b352b-d78a-4a4f-bf5a-05fb3c46e3b6" />


Creating the Training Algorithm:

Images are used as control points. The average RGB color of each image is calculated, and the coordinates along this path are calculated by calculating the shortest distance between two images. After this calculation, the coordinates are written to a separate Excel file along a timeline.

Calculating Intermediate Values of Measurement Data and Adding them to the Model Excel File:

After writing the intermediate RGB coordinates to the model Excel file and determining the total model size, the measurement data is added to the same row as the images. Following this addition, four different calculation methods are used to calculate the intermediate values. For the values of the intermediate estimates, linear increase and decrease calculations, exponential increase and decrease calculations, a combination of linear and exponential increase and decrease calculations, and data expansion methods are used. Each image and measurement data used as a control point are mapped to the next control point, and intermediary value estimates are performed between the two control points.


Combining Trained Models and Recalculating Intermediate Values:

Combining Trained Models with Time-Coherence in Mind:

To combine trained models in time-coherence, the trained models must contain an equal number of images, and the starting point of the suspension cultures must be under the same conditions. Regardless of the similarity of the control points between the combined models, the arithmetic average is calculated based solely on the Z-score of the timeline and the control points. After the control points are combined, the intermediate values are recalculated.

<img width="1021" height="669" alt="modelbirlestir" src="https://github.com/user-attachments/assets/8268c36f-e7fe-4d4f-ab6f-6263708244d7" />





