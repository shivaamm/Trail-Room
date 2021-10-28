var User = require("../schema/user");

module.exports = async function (req,res){
    try{
        const user = await User.findbycredentials(req.body.username, req.body.password);
        const token = await user.generateauthtoken()
        res.status(200).send({user, token}); 
    
      } catch(e){
        res.status(400).send("Wrong Credentials");
    }
}