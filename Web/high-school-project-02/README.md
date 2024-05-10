# High School Project 02

My teacher told me about the vulnerability present in version 1. Now I have learnt templating and super safe techniques to avoid all this!

## Solution
"+ {location=name} +"
Set name to a JavaScript uri in the content field as the site sets the title content to window.name. Set title to javascript:alert(1). It breaks out of the quotes in one of the javascript functions
And the function treats the {location=name} as a parameter
So it needs to find sflr return value. And to find its return value it needs to evaluate whatever statement is inside. location=name is the same as window.location = window.name. Just as how fetch() is the same as window.fetch().