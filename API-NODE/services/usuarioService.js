const { getConnection } = require('../database');

class UsuarioService {
  async crearUsuario(usuario) {
    const connection = await getConnection();
    try {
      const [result] = await connection.execute(
        'INSERT INTO usuarios (nombre, identificacion) VALUES (?, ?)',
        [usuario.nombre, usuario.identificacion]
      );
      return result.insertId;
    } finally {
      connection.release();
    }
  }

  async buscarUsuarioPorIdentificacion(identificacion) {
    const connection = await getConnection();
    try {
      const [rows] = await connection.execute(
        'SELECT * FROM usuarios WHERE identificacion = ?',
        [identificacion]
      );
      return rows[0];
    } finally {
      connection.release();
    }
  }
}

module.exports = UsuarioService;