
const express = require('express'); 
const path = require('path');
const app = express(); 
const port = 2001;

app.set("view engine", "ejs")
var order=0//please do not attempt to go to output first :)
app.use(express.static(path.join(__dirname, 'public')));

app.get("/", (req,res)=>{
    res.render("index.ejs")
})
app.get("/filename", (req, res) => {
    console.log(req.query)
    console.log(req.query.path)
    order=1
    var banned="../"
    if (req.query.path.includes(banned) || req.query.path.includes("flag.txt")){
        res.send("404, you might have tripped a banned character!")
        console.log("banned")
        return
    }
    if (req.query.path.length>21){
        res.send("Please check the file's spelling!")
        return
    }
    console.log(req.query.path)
    res.redirect('/output?location='+req.query.path)    
});



app.get("/output",(req,res)=>{
    console.log(req.query)
    console.log(req.query.location)

    //no way anyone has possibly gotten past the previous filter right?
    //anyways here's another one for security purposes
    var input=req.query.location
    var banned="../"
    var banned2="fla"
    var output=""
    var permitted="/pics/user/"

    if (order==0){
        res.redirect("/")
    }
    order=0
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
    res.sendFile(path.resolve('./' + output));
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})



