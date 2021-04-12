Artifically Intelligent (Software) "Robot" for Childhood Autism - ARICA
This program was developed for the purpose of a term project for the KSU COMP730-A FALL2020 course as well as a potential independant study topic for Grant Loewer.

##System Requirements##
SUGGESTED
	Raspberry Pi with Raspbian & USB connected Microphone
OR
	Any machine that can run Python3 and can install additional python libraries
		- with either a built in microphone or connected microphone.

##Installation##
EITHER
	Run the setup.sh file with the 'bash setup.sh' command on UNIX systems. (Within the correct directory)
OR
	Use the package manager [pip](https://pip.pypa.io/en/stable/) and apt-get to install the following pacakges

	'''bash
	pip3 install SpeechRecognition
	pip3 install pyaudio
	sudo apt-get install flac
	sudo apt-get install python3-numpy python3-scipy libzmq-dev liblapack-dev libatlas-dev gfortran
	pip3 install nltk
	pip3 install numpy
	sudo apt-get install libatlas-base-dev
	pip3 install scipy
	pip3 install scikit-learn
	'''
	
##Running it##
EITHER
	Run the ARICA.py file with the 'python3 ARICA.py' command on UNIX systems. (Within the correct directory)
OR
	Run the ARICA.py file by double clicking it.
	
##Usage##
1.) ARICA will greet you with "Hello my name is ARICA!" and "My face is materializing, please wait!"
2.) Once her face shows up, begin talking to ARICA, her face will display the predicted emotion of the statement you said to her.
	- a statement is only reacted to by ARICA when you stop talking for a second, as she must hear a pause before reacting.
3.) Talk to her as long as you would like.
4.) To exit, select the X button at the top of the terminal as you would do on any other application.

##Thanks##
Thank you for talking to ARICA, she really appreciates it.