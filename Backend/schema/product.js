var mongoose = require("mongoose");
const ProductSchema = new mongoose.Schema({
    "Label":{type:String},
    "brand":{type:String},
    "name":{type:String},
    "price":{type:Number},
    "rank":{type:Number},
    "ingredients":{type:Number},
    "Combination":{type:Number},
    "Dry":{type:Number},
    "Normal":{type:Number},
    "Oily":{type:Number},
    "Sensitive":{type:Number}
})

const Product = mongoose.model("Product",ProductSchema);
module.exports = Product;
