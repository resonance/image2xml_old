# image2xml

This is the code being used by the Resonance Engineering team to transform the Vector Pattern files into XML code. 





A few tips:

	1) When running on SageMaker, make sure you go to the "Conda" tab once you are in the notebook directory and make sure to add Keras to the environment you choose to use. What has worked for me is running it using the Conda_Python3 environment which means adding Keras there. The HTML/XML (HTML:XML) folder contains the currently altered code to run the XML and vector images. This is the version which is only the RNN and uses the pretrained imagenet to do feature extraction and the keras preprocessing library to extract the tokens. 

	2) Disconnecting from the internet disconnects the job because the connection to the kernel is lost. This is most likely due to running in jupyter notebooks and the next step would be to deploy the job from the notebook in sagemaker and then monitor remotely removed from the notebook itself. (the notebook would just be the interface to kick off the job, it wouldn't be run through the notebook like we are doing now.

	3) If running on jupyter notebooks keep an eye on the remaining GPU time. The email warnings seem to be on a delay which can cause the GPU to expire and the kernel to disconnect, forcing a re-run of the job entirely (unless you spawn the model from previously saved weights)

	4) To upload multiple files into a jupyter notebook, but them in a folder and then compress into a zip file and upload the zip file. From there, create a new notebook and run the following code: 
				import zipfile as zf
				files = zf.ZipFile("ZippedFolder.zip", 'r')
				files.extractall('directory to extract')
				files.close()


The next step is to alter the code for the bootstrapped version which adds the CNN layer and extracts the features and tokens on demand from the images and the seeding of input tokens. This is where we would probably need our own DSL because these tokens shouldn't all need to be pre-fed. Only a seeding of the tokens. 
