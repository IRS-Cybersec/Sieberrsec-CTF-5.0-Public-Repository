
# Running Can

Category: forens

Creator: hana.1217

Flag: sctf{d1d_y0u_run_0r_b1nw41k}

## Description:
I love this song! 

You've been runnin' 'round, 
runnin' 'round, 
runnin' 'round 
throwin' that dirt all on my name ~

## Hint

Have you heard of binwalk?

## Solution:

After opening the runninground.mp3 in Hexedit, there is a JFIF string and the file ends with FF D9 which are all signs that there is a jpg file in the .mp3 file
![](../../../../../Desktop/runningHexEdit.png)

Using binwalk to extract the file, there is a .jpg file that you can open and you can find the second part of the flag.

Looking through the HexEdit or using strings, there is the second part of the flag. (If you see the jpg carefully, there is part of the jpg that is grey part of the jpg that suggests that some part of the jpg data is not suppose to be there)

With the 2 parts of the flag, you have found the flag.