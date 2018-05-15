import speech_recognition as sr

class SpeechToText:

	def __init__(self):
		self.r = sr.Recognizer()
		self.m = sr.Microphone()
		self.r.pause_threshold = 0.5
		self.r.energy_threshold = 1500
		self.value = None
		self.changed = False

	def listen(self):
		try:
			m = self.m
			r = self.r
			print("A moment of silence, please...")
			#with m as source: r.adjust_for_ambient_noise(source)
			print("Set minimum energy threshold to {}".format(r.energy_threshold))
			print("Say something!")
			with m as source: audio = r.listen(source)

			print("Got it! Now to recognize it...")
			try:
				# recognize speech using Google Speech Recognition
				value = r.recognize_google(audio)
				# we need some special handling here to correctly print unicode characters to standard output
				if str is bytes:  # this version of Python uses bytes for strings (Python 2)
					print(u"You said {}".format(value).encode("utf-8"))
					self.value = format(value)
				else:  # this version of Python uses unicode for strings (Python 3+)
					print("You said {}".format(value))
					self.value = format(value)
			except sr.UnknownValueError:
				print("Oops! Didn't catch that")
				self.value = "Oops! Didn't catch that"
			except sr.RequestError as e:
				print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
				self.value = format(e)
			# return self.value
		except KeyboardInterrupt:
			pass

	def getSentence(self):
		return self.value
