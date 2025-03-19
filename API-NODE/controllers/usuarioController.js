const mysql = require('mysql');
const bcrypt = require('bcrypt');


exports.getAllUsuarios = (req, res) => {
  connection.query('SELECT id, nombre, apellido, usuario, rol_id, fecha_registro FROM usuarios', (error, results) => {
    if (error) {
      return res.status(500).json({
        status: false,
        message: 'Error al obtener usuarios',
        error: error
      });
    }
    
    return res.status(200).json({
      status: true,
      message: 'Usuarios obtenidos con éxito',
      data: results
    });
  });
};

// Get user by ID
exports.getUsuarioById = (req, res) => {
  const id = req.params.id;
  
  connection.query('SELECT id, nombre, apellido, usuario, rol_id, fecha_registro FROM usuarios WHERE id = ?', 
  [id], (error, results) => {
    if (error) {
      return res.status(500).json({
        status: false,
        message: 'Error al obtener usuario',
        error: error
      });
    }
    
    if (results.length === 0) {
      return res.status(404).json({
        status: false,
        message: 'Usuario no encontrado'
      });
    }
    
    return res.status(200).json({
      status: true,
      message: 'Usuario obtenido con éxito',
      data: results[0]
    });
  });
};

exports.createUsuario = (req, res) => {
  const { nombre, apellido, usuario, contrasena, rol_id } = req.body;
  
  // Validate request
  if (!nombre || !apellido || !usuario || !contrasena || !rol_id) {
    return res.status(400).json({
      status: false,
      message: 'Contenido incompleto. Se requieren todos los campos.'
    });
  }
  
  
  bcrypt.hash(contrasena, 10, (err, hash) => {
    if (err) {
      return res.status(500).json({
        status: false,
        message: 'Error al encriptar contraseña',
        error: err
      });
    }
    
  
    const newUser = {
      nombre,
      apellido,
      usuario,
      contrasena: hash,
      rol_id,
      fecha_registro: new Date()
    };
    
    connection.query('INSERT INTO usuarios SET ?', newUser, (error, results) => {
      if (error) {
        return res.status(500).json({
          status: false,
          message: 'Error al crear usuario',
          error: error
        });
      }
      
      return res.status(201).json({
        status: true,
        message: 'Usuario creado con éxito',
        data: { id: results.insertId, ...newUser, contrasena: undefined }
      });
    });
  });
};


exports.updateUsuario = (req, res) => {
  const id = req.params.id;
  const { nombre, apellido, usuario, contrasena, rol_id } = req.body;
  
  // Validate user exists
  connection.query('SELECT * FROM usuarios WHERE id = ?', [id], (error, results) => {
    if (error) {
      return res.status(500).json({
        status: false,
        message: 'Error al validar usuario',
        error: error
      });
    }
    
    if (results.length === 0) {
      return res.status(404).json({
        status: false,
        message: 'Usuario no encontrado'
      });
    }
    
  
    const updateUser = {};
    
    if (nombre) updateUser.nombre = nombre;
    if (apellido) updateUser.apellido = apellido;
    if (usuario) updateUser.usuario = usuario;
    if (rol_id) updateUser.rol_id = rol_id;
    
    // If password is being updated, hash it
    if (contrasena) {
      bcrypt.hash(contrasena, 10, (err, hash) => {
        if (err) {
          return res.status(500).json({
            status: false,
            message: 'Error al encriptar contraseña',
            error: err
          });
        }
        
        updateUser.contrasena = hash;
        
        connection.query('UPDATE usuarios SET ? WHERE id = ?', [updateUser, id], (error, results) => {
          if (error) {
            return res.status(500).json({
              status: false,
              message: 'Error al actualizar usuario',
              error: error
            });
          }
          
          return res.status(200).json({
            status: true,
            message: 'Usuario actualizado con éxito',
            data: { id, ...updateUser, contrasena: undefined }
          });
        });
      });
    } else {
      // Update without changing password
      connection.query('UPDATE usuarios SET ? WHERE id = ?', [updateUser, id], (error, results) => {
        if (error) {
          return res.status(500).json({
            status: false,
            message: 'Error al actualizar usuario',
            error: error
          });
        }
        
        return res.status(200).json({
          status: true,
          message: 'Usuario actualizado con éxito',
          data: { id, ...updateUser }
        });
      });
    }
  });
};

// Delete user
exports.deleteUsuario = (req, res) => {
  const id = req.params.id;
  
  connection.query('DELETE FROM usuarios WHERE id = ?', [id], (error, results) => {
    if (error) {
      return res.status(500).json({
        status: false,
        message: 'Error al eliminar usuario',
        error: error
      });
    }
    
    if (results.affectedRows === 0) {
      return res.status(404).json({
        status: false,
        message: 'Usuario no encontrado'
      });
    }
    
    return res.status(200).json({
      status: true,
      message: 'Usuario eliminado con éxito'
    });
  });
};