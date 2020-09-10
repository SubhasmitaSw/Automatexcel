import pyttsx3

converter = pyttsx3.init() 
  

voices = converter.getProperty('voices') 

for voice in voices: 
	# to get the info. about various voices in our PC 
	print("Voice:") 
	print("ID: %s" %voice.id) 
	print("Name: %s" %voice.name) 
	print("Age: %s" %voice.age) 
	print("Gender: %s" %voice.gender) 
	print("Languages Known: %s" %voice.languages) 


voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# Use female voice 
converter.setProperty('voice', voice_id) 

converter.runAndWait() 

