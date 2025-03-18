const Usuario = require('../models/usuario.js');

const login = async (req, res) => {
  try {
    console.log('Datos recibidos:', req.body);
    const { usuario, contrasena } = req.body;
    
    // Verificar que se proporcionen las credenciales
    if (!usuario || !contrasena) {
      return res.status(400).json({
        success: false,
        message: 'Usuario y contraseña son requeridos'
      });
    }
    
    // Buscar usuario por el campo "usuario"
    const usuarioEncontrado = await Usuario.findOne({ where: { usuario } });
    
    // Si no existe el usuario
    if (!usuarioEncontrado) {
      return res.status(404).json({
        success: false,
        message: 'Usuario no encontrado'
      });
    }
    
    // Comparación directa para contraseñas en texto plano
    const isPasswordValid = contrasena === usuarioEncontrado.contrasena;
    
    if (!isPasswordValid) {
      return res.status(401).json({
        success: false,
        message: 'Contraseña incorrecta'
      });
    }
    
    // Si todo es correcto, devolver éxito y datos básicos del usuario
    const userData = {
      id: usuarioEncontrado.id,
      nombre: usuarioEncontrado.nombre,
      apellido: usuarioEncontrado.apellido,
      usuario: usuarioEncontrado.usuario,
      rol_id: usuarioEncontrado.rol_id
    };
    
    return res.status(200).json({
      success: true,
      message: 'Login exitoso',
      user: userData
    });
    
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: 'Error en el proceso de login',
      error: error.message
    });
  }
};

module.exports = { login };