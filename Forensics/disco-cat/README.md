# Disco Cat

Category: forens

Creator: hana.1217

Flag: `sctf{d1d_y0u_l1k3_th3_c0l0ur5}`

## Description:
Check out this gif I made! 

## Solution:

Looking at the gif closely, it seems there are a few frames that look different from the others. Hence, you can use Ezgif (or other software) to break down the GIF into its frames. Of the frames there are 2 halves of a QR Code.
![](<../../../../../Desktop/CyberSec/SCTF/SCTF Challs/Forensics/Disco Cat/src/gif/gif.011.jpeg>)
![](<../../../../../Desktop/CyberSec/SCTF/SCTF Challs/Forensics/Disco Cat/src/gif/gif.019.jpeg>)

After that, just join the 2 halves together to create the entire QR Code. However, as the QR Code has many designs over it, you can start cleaning the QR Code (The QR code can be cleaned in multiple ways, since it is translucent you can colour over the QR code to restore it)

The final QR Code looks like this:
![](<../../../../../Desktop/CyberSec/SCTF/SCTF Challs/Forensics/Disco Cat/src/frame.png>)

Scanning the QR Code brings you to a Google Slides. 
https://docs.google.com/presentation/d/1EuXUaL8LaWWpcofyBq1ItknjUhSO1Boc8hLzXNB1hbU/edit?usp=sharing

Looking through the seemingly empty slides, there is white text on 4 of 5 slides and the 4th slide has the flag.
