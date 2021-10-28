var User = require("../schema/user");

module.exports = async(req, res) => {
    const user = new User(req.body)
    try{
      await user.save()
      const token = await user.generateauthtoken()
      res.status(201).json({user, token})
    } 
    catch(e){
        //res.json(e);
      res.status(400).send("Username already exists");
    }
}