var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var cors = require('cors');

const app = express();
app.use(bodyParser.json());
app.use(cors());
mongoose.connect("mongodb+srv://admindb:admindatabase@cluster0-vlwic.mongodb.net/myntra",{ useNewUrlParser: true, useUnifiedTopology: true});

app.get('/',(req,res)=>{
    res.send("Working");
});

//routes

//signup route
var signupUser = require("./routes/signup");
app.post("/user/signup",cors(), signupUser);

//login route
var loginUser = require("./routes/login.js");
app.post("/user/login",cors(),loginUser);

var allProducts = require('./routes/allprods');
app.use('/allproducts',allProducts);

const port = process.env.PORT || 3000;
app.listen(port,()=>{console.log(`Running at port ${port}!`)});