
# beepboop

Category: forens

Creator: hana.1217

Flag: `sctf{f0r3ns1c5_101_0n_4ud10_st3g4n0gr4phy}`

## Description:
Here's a beep boop for you! The password..? rockyou.txt

## Hint:
- Have you heard of LSB?

## Solution:
When you try to extract the zip, you need a password. Also, there is a hint in the challenge description that the password is rockyou.txt. Some Google search will show that rockyou.txt is a password worlist so you download rockyou.txt from the first Google result https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

With some searching from previous writeups online a common tool for password protected zip file challenges during CTFs is fcrackzip (there are many other tools that can be used also)

By running fcrackzip with rockyou.txt
![](../../../../../Desktop/fcrackzip.png)

You can enter the password bestmusic to get beep.wav and boop.wav. 
Since beep.wav is quite short and does not sound like Morse or anything recognisable, you can open it in audio softwares like Audacity or Sonic Visualiser which and see its spectrogram which will give:
![](../../../../../Desktop/spectrogram.png)

Now, this is the first part of the flag and the second part is in boop.wav. When you open boop.wav in HexEdit, there are some strange bytes.
![](../../../../../Desktop/hexedit.png). Hence, it is most likely LSB steganography. After some trial and error with various software with Google there was one of them that gave a printable result (https://sumit-arora.medium.com/audio-steganography-the-art-of-hiding-secrets-within-earshot-part-2-of-2-c76b1be719b3). 

<blockquote>

```lua
# Use wave package (native to Python) for reading the received audio file
import wave
song = wave.open("boop.wav", mode='rb')
# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Extract the LSB of each byte
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
# Convert byte array back to string
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
# Cut off at the filler characters
decoded = string.split("###")[0]

# Print the extracted text
print("Sucessfully decoded: "+decoded)
song.close()
```

</blockquote>

Now, you have both parts of the flag!