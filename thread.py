import threading 


def audio():

	for i in range(0,10):
		print ("Audio clip, %d \n") % i


def video():

	for i in range(0,10):
		print ("Video clip, %d \n") % i




audio_thread = threading.Thread(target=audio)
video_thread = threading.Thread(target=video)
audio_thread.start()
video_thread.start()