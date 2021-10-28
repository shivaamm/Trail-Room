var mongoose = require("mongoose");
var passportLocalMongoose = require("passport-local-mongoose");
var bycrypt = require('bcryptjs');
var jwt = require('jsonwebtoken');

const UserSchema = new mongoose.Schema({
    username: {type: String, unique: true,require:true},
    password: {type: String, require: true},
    email: {type: String, require:true},
    tokens: [{
        token :{
            type: String,
            require: true
        }
    }]
});

// //Generating token
UserSchema.methods.generateauthtoken = async function() {
    const user = this
    const token = jwt.sign( {_id: user._id.toString() }, 'thisisthesecret')

    user.tokens = user.tokens.concat({ token })

    await user.save();

    return token;
}



// verifying our user
UserSchema.statics.findbycredentials = async (username, password) => {
    const user = await User.findOne({username})
    if(!user){
        throw new Error("unable to login");

    }

    const ismatch = await bycrypt.compare(password, user.password)

    if(!ismatch){
        throw new Error("unable to login");
    }

    return user;
}


//Haash the password
UserSchema.pre('save', async function(next){
    const user = this

    if (user.isModified("password")){
    
    user.password = await bycrypt.hash(user.password, 8);

    }

    next()
})

const User = mongoose.model("User", UserSchema);

module.exports = User;