
# Travelling Around the World 2.0

Category: misc

Creator: hana.1217

Flag: `sctf{35.6855328_139.7009257}`

## Description:
My friend is at it again! She doesn't want to tell me where she went! This time, I managed to find out where she posted her holiday pictures at but it seems she found out and deleted the post... Can you find me the coordinates of where she was?

Post Link: https://www.linkedin.com/posts/hana-tan-31741a2b8_is-this-what-you-are-looking-for-link-activity-7169995932862767104-vkGL

Wrap the flag with sctf{latitude_longitude}

## Solution:
1. Go to Wayback Machine and find the web archive of the LinkedIn post page
2. There is an additional post that was not seen originally with a video and a link to the video
3. In the video, there is some Japanese text so the video was taken in Japan
4. In the last few frames, there is some text on a building behind but it is quite blurry
5. Using an image quality enhancer, the words can be made out to be the Katakana words for Hotel Sunroute Plaza
6. Searching Google Maps, there is only 1 branch in Shinjuku
7. Searching around the area of Google Street View, you can find the train and road intersection and you can find the coordinates from Google Street View

