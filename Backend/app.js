var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

const app = express();
app.use(bodyParser.json());
mongoose.connect("mongodb+srv://admindb:admindatabase@cluster0-vlwic.mongodb.net/myntra",{ useNewUrlParser: true, useUnifiedTopology: true});

app.get('/',(req,res)=>{
    res.send("Working");
});

//routes
var allProducts = require('./routes/allprods');
app.use('/allproducts',allProducts);

const port = process.env.PORT || 3000;
app.listen(port,()=>{console.log(`Running at port ${port}!`)});