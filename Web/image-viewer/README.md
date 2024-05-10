# Image viewer

## Description

Hi! I have just made an image hosting site that allows me to share some of my favourite pictures with everyone! However, I have heard that some nasty people have been able to abuse this system to get files they should not access! A few filters should keep them away...right?


## Hints

Hint1:
What are some dangers of grabbing files right out of your directory?

Hint2:
1. If you pass in an element as a string, it is going to be really long, maybe consider another data type?
2. Hint! I am passing the input through 2 sites!
3. What are some dangers of a filter system that only loops once without recursion?


## Solution

Hi, this is my first ctf challenge created. The following will be the intended solution to the challenge with the alternative solutions written behind. Hope it was decently challenging and fun for everyone :).

Solution:

From the code we can see the following:

```
res.sendFile(path.resolve('./codeNstuff/' + output));
```

This is a severe vulnerability in the code. Websites should never use the path system or any other input system that can be modified by the front-end user to return files. Doing so makes the website vulnerable to directory traversal attacks, where users can abuse inputs such as "../" (which allows users to escape the folder) to attain files they should not have access to. This is made worse by the fact that the website lacks a security system that will send users to a 403 forbidden page if they are trying to access a file they should not. As such, we are able to edit the "output" to extract files we want.

Looking at the ways the files are arranged, you will realise that the location of frontend.js is in two codeNstuff folders while the flag is held in a flag container. The picture of the cat that the code grabs is stored in "/pics/user". As such, a directory traversal attack to redirect the res.sendFile() into the flagcontainer folder would allow for the file to be extracted.

However, as the challenge description states, there are 3 basic filters to prevent directory traversal from being implemented directly.

*1.*
```
if (req.query.path.includes(banned) || req.query.path.includes("flag.txt")){
        res.send("404, you might have tripped a banned character!")
        console.log("banned")
        return
}
```

This filter mandates that the input must not contain any character"../" or "flag.txt". As a result, the input must do so in a way that circumvents this. You may realise that characters such as "." remains detected even after converting to %2E as the website would convert it back automatically and flag the input. However, if you read a bit more of the code, you will find out that the input actually passes through 2 websites. As such, a double url-encryption can be used for the challenge. Part 3 will explain more on how to bypass flag.txt. 

*2.*
```
if (req.query.path.length>21){
        res.send("Please check the file's spelling!")
        return
    }
```

This function limits the length of the input to an unreasonably small number. The total number of characters is in fact even less than 21 since in a later portion, the following code makes it compulsory for "/pics/user" to be added

```
var permitted="/pics/user"
```

and 

```
if (req.query.location.includes(permitted)){
```

However, this can be bypassed through converting your input into a value within a list. When you change the data type of the path to path[], it automatically converts every data input behind it into a single index within a list, reducing characters to 1 and allowing you to do much longer directory traversals.

After this, the input data would be transferred to another site where another round of input inspection would take place. To prevent u

*3.*
```
if (req.query.location.includes(permitted)){
    for(let i=0;i<(input.length-2);i++){
        var temp=""
        temp+=input[i]
        temp+=input[i+1]
        temp+=input[i+2]
        //what, do you not like the way this is coded? Cope :D
        if (temp == banned || temp == banned2){
            i+=2
        }
        else{
            output+=input[i]
        }
    }
    console.log(output)
}
else{
    res.send("please don't try to hack me :<")
}
```

(The coding was definitely sub-optimal here)
The variables for this includes:

```
var input=req.query.location
var banned="../"
var banned2="fla"
var output=""
var permitted="/pics/user"
```

This code does the following:

1. Ensure that "/pics/user" is within the input

2. Has a sliding window system that ensures "fla" and "../" in their exact terms are not within the input

The sliding window does not outright reject the input, but rather modifies it by excluding the characters to prevent an attack. As such, more characters can be added before and after the actual input to throw the sliding window detection system off. For example, instead of just "../", you can instead type "....//". This would result in the sliding window removing the "../" in the centre, leaving another "../" behind while only reading the end portion of the "../" since the sliding window does not traverse backwards. The same thing goes for flag.txt. Typing "ffflalag" instead bypasses both filter 1 and 3. An unintended consequence of the code is that it will not read the final few characters. As such, you need to have 2 additional letters at the back.

To prevent users from directly traversing to the second webpage and bypassing the first round of filters, a system was implemented where a variable "order" essentially acts as a boolean that will send users back to the starting site if they attempt to skip the first site that uses filename?path . Please do note that for this challenge, you are genuinely not supposed to bypass the filter as that was not my intention (I only implemented it this way because I was running out of time and Nodejs Post and res.redirect() wasn't redirecting). However, if you wish to bypass this system as one group did, you can use curl in linux to visit "/filename?path" and trick the system into thinking you have visited it before visiting "/output?location" directly. Once again, this is not the intended solution and is a major oversight on my part.

As such, the intended solution is:

```
filename?path[]=/pics/user/%252E%252E%252E%252E%252f%252f%252E%252E%252E%252E%252f%252f%252E%252E%252E%252E%252f%252ffflalag container%252ffflalag%252Etxtxt
```

Hope this writeup was helpful. See y'all next time!

## Flag

sctf{D0n't_l3t_tH3m_1nPUT}





