
# HackMyPDFs

Category: forens

Creator: hana.1217

Flag: `sctf{h1dden_b3h1nd_4n_1m4g3}`

## Description
Check out my PDF about PDFs!


## Solution
As there is a password for the PDF, you can use tools such as pdfcrack to bruteforce the pdf password with rockyou.txt which gives chocolate. To check if there are any hidden images in the PDF, use pdftohtml tool (or other software there are many) to get all the images in the pdf. One of them is the image of the flag.
