import gtts
text = input()
voice = gtts.gTTS(text, lang="en", slow=False)
voice.save("python\TESTS.py\Voice.mp3")