const jwt = require("jsonwebtoken");
const Usuario = require("../models/usuario");

const validateAuth = async (req, res, next) => {
  const token = req.header("Authorization").replace("Bearer ", "");

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    const usuario = await Usuario.findByPk(decoded.id);

    if (!usuario) {
      throw new Error();
    }

    req.user = usuario;
    next();
  } catch (error) {
    res.status(401).json({
      success: false,
      message: "Autenticación fallida",
    });
  }
};

module.exports = { validateAuth };