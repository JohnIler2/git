# play a wave sound on a Windows Box
# Python23 tested   vegaseat   2/8/2005
import winsound
import time
# Python also accepts the forward slash

#The variable name will need to be changed for every sound.
def sounds():
    #Input the file path of your .wav file
    soundfile = "C:\Users\..\..\"
    winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)
