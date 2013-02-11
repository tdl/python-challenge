import base64
import wave
import winsound

f = open("l19/base64d.txt")
fo = open("l19/indian.wav", "wb") ## note the wb !!
base64.decode(f,fo)
fo.close()
f.close()

## just listen first
winsound.PlaySound("l19/indian.wav", winsound.SND_FILENAME)

w = wave.open("l19/indian.wav")
bytes = w.readframes(w.getnframes())
## shift by one byte!
bytes = bytes[1:]

wmod = wave.open("l19/indianshift.wav", "wb")
wmod.setparams(w.getparams())
## and write back out
wmod.writeframes(bytes)
wmod.close()
w.close()

## now check this out!
winsound.PlaySound("l19/indianshift.wav", winsound.SND_FILENAME)

