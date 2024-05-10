
# Transport 101

Category: misc

Creator: hana.1217

Flag: `sctf{20.2}`

## Description
Oh no, I'm lost! Here's a picture of where I am and my destination. How far away am I by driving? Oh, the password? It's the date that my parents registered their car! The format is [month][year] (e.g. January2025)

Give your answer to nearest 1 decimal place in km. Wrap it in sctf{}

## Solution:

Password: November2012

1. Using a website from LTA, a car starting with SKJ is registered in November 2012
2. Using that password, unlock the zip file
3. From start.jpg , you can see it is in a tunnel with 2 arrows pointing away and with closer observation and some quality enhancer software, it says KPE and MCE
4. Some Google searching will tell you KPE and MCE are 2 connected expressways in Singapore
5. At the connection point, there is this sign (Google Street View)
6. At end.jpg , it shows AYE on the sign which is another expressway
7. There is also Singapore Mint in the background so you can locate where that picture was taken
8. Using the coordinates from both locations, put into Google Maps and change the settings to driving to find the shortest distance between them.
