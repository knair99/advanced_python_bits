import threading 


def audio(audio_event, video_event, lock, name):

	audio_event.set()
	video_event.wait()
	print "Video ready. Audio can start\n"

	for i in range(0,100):
		lock.acquire()
		print ("%s Audio clip, %d \n") % (name, i)
		#print ("%s AAAAAAAAAAAAAAAA %d \n") % (name, i)
		lock.release()

		
		


def video(audio_event, video_event, lock, name):
	audio_event.wait()
	video_event.set()

	print "Audio ready. Video can start\n"

	for i in range(0, 100):
		lock.acquire()
		print ("%s Video clip, %d \n") % (name, i)
		#print ("%s VVVVVVVVVVVVVVV %d \n") % (name, i)
		lock.release()



#define an event for both threads
audio_event = threading.Event()
video_event = threading.Event()

lock = threading.Lock()

#first start both threads
audio_thread = threading.Thread(target=audio, args=(audio_event, video_event, lock, "audiothread >>"))
video_thread = threading.Thread(target=video, args=(audio_event, video_event, lock, "videothread >>"))
audio_thread.start()
video_thread.start()

