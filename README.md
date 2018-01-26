# image2xml

This is the code being used by the Resonance Engineering team to transform the Vector Pattern files into XML code. 





A few tips:

	1) When running on SageMaker, make sure you go to the "Conda" tab once you are in the notebook directory and make sure to add Keras to the environment you choose to use. What has worked for me is running it using the Conda_Python3 environment which means adding Keras there. The HTML/XML (HTML:XML) folder contains the currently altered code to run the XML and vector images. This is the version which is only the RNN and uses the pretrained imagenet to do feature extraction and the keras preprocessing library to extract the tokens. 

The next step is to alter the code for the bootstrapped version which adds the CNN layer and extracts the features and tokens on demand from the images and the seeding of input tokens. This is where we would probably need our own DSL because these tokens shouldn't all need to be pre-fed. Only a seeding of the tokens. 
