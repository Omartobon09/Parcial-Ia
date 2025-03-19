const mysql = require('mysql');


exports.getAllHistoriales = (req, res) => {
  connection.query('SELECT * FROM historial', (error, results) => {
    if (error) {
      return res.status(500).json({
        status: false,
        message: 'Error al obtener historiales',
        error: error
      });
    }
    
    return res.status(200).json({
      status: true,
      message: 'Historiales obtenidos con éxito',
      data: results
    });
  });
};


exports.getHistorialById = (req, res) => {
  const id = req.params.id;
  
  connection.query('SELECT * FROM historial WHERE id = ?', [id], (error, results) => {
    if (error) {
      return res.status(500).json({
        status: false,
        message: 'Error al obtener historial',
        error: error
      });
    }
    
    if (results.length === 0) {
      return res.status(404).json({
        status: false,
        message: 'Historial no encontrado'
      });
    }
    
    return res.status(200).json({
      status: true,
      message: 'Historial obtenido con éxito',
      data: results[0]
    });
  });
};


exports.getHistorialByUsuario = (req, res) => {
  const usuarioId = req.params.usuarioId;
  
  connection.query('SELECT * FROM historial WHERE usuario_id = ? ORDER BY fecha DESC', 
  [usuarioId], (error, results) => {
    if (error) {
      return res.status(500).json({
        status: false,
        message: 'Error al obtener historial del usuario',
        error: error
      });
    }
    
    return res.status(200).json({
      status: true,
      message: 'Historial del usuario obtenido con éxito',
      data: results
    });
  });
};

exports.createHistorial = (req, res) => {
  const { usuario_id, descripcion } = req.body;
  
  // Validate request
  if (!usuario_id || !descripcion) {
    return res.status(400).json({
      status: false,
      message: 'Se requieren todos los campos: usuario_id, descripcion'
    });
  }
  
  // Save historial to database
  const newHistorial = {
    usuario_id,
    descripcion,
    fecha: new Date()
  };
  
  connection.query('INSERT INTO historial SET ?', newHistorial, (error, results) => {
    if (error) {
      return res.status(500).json({
        status: false,
        message: 'Error al crear historial',
        error: error
      });
    }
    
    return res.status(201).json({
      status: true,
      message: 'Historial creado con éxito',
      data: { id: results.insertId, ...newHistorial }
    });
  });
};

// Update historial
exports.updateHistorial = (req, res) => {
  const id = req.params.id;
  const { usuario_id, descripcion, fecha } = req.body;
  
  // Validate historial exists
  connection.query('SELECT * FROM historial WHERE id = ?', [id], (error, results) => {
    if (error) {
      return res.status(500).json({
        status: false,
        message: 'Error al validar historial',
        error: error
      });
    }
    
    if (results.length === 0) {
      return res.status(404).json({
        status: false,
        message: 'Historial no encontrado'
      });
    }
    
    // Update historial
    const updateHistorial = {};
    
    if (usuario_id) updateHistorial.usuario_id = usuario_id;
    if (descripcion) updateHistorial.descripcion = descripcion;
    if (fecha) updateHistorial.fecha = fecha;
    
    connection.query('UPDATE historial SET ? WHERE id = ?', 
    [updateHistorial, id], (error, results) => {
      if (error) {
        return res.status(500).json({
          status: false,
          message: 'Error al actualizar historial',
          error: error
        });
      }
      
      return res.status(200).json({
        status: true,
        message: 'Historial actualizado con éxito',
        data: { id, ...updateHistorial }
      });
    });
  });
};

// Delete historial
exports.deleteHistorial = (req, res) => {
  const id = req.params.id;
  
  connection.query('DELETE FROM historial WHERE id = ?', [id], (error, results) => {
    if (error) {
      return res.status(500).json({
        status: false,
        message: 'Error al eliminar historial',
        error: error
      });
    }
    
    if (results.affectedRows === 0) {
      return res.status(404).json({
        status: false,
        message: 'Historial no encontrado'
      });
    }
    
    return res.status(200).json({
      status: true,
      message: 'Historial eliminado con éxito'
    });
  });
};