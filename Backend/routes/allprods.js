const Product = require('../schema/product');
module.exports = (req,res)=>{
    Product.find({},(err,result)=>{
        if(err){
            res.json(err);
        }
        else{
            res.json(result);
        }
    })
} 
