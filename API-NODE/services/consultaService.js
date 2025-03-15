const { getConnection } = require('../database');

class ConsultaService {
  async crearConsulta(consulta) {
    const connection = await getConnection();
    try {
      await connection.beginTransaction();

      const [consultaResult] = await connection.execute(
        'INSERT INTO consultas (usuario_id, diagnostico) VALUES (?, ?)',
        [consulta.usuario_id, consulta.diagnostico]
      );
      const consultaId = consultaResult.insertId;

      for (const respuesta of consulta.respuestas) {
        await connection.execute(
          'INSERT INTO respuestas (consulta_id, pregunta_id, respuesta) VALUES (?, ?, ?)',
          [consultaId, respuesta.pregunta_id, respuesta.respuesta]
        );
      }

      await connection.commit();
      return consultaId;
    } catch (error) {
      await connection.rollback();
      throw error;
    } finally {
      connection.release();
    }
  }

  async obtenerTodasConsultas() {
    const connection = await getConnection();
    try {
      const [consultas] = await connection.execute(`
        SELECT c.id, c.usuario_id, c.fecha_consulta, c.diagnostico, u.nombre, u.identificacion
        FROM consultas c
        JOIN usuarios u ON c.usuario_id = u.id
        ORDER BY c.fecha_consulta DESC
      `);

      for (const consulta of consultas) {
        const [respuestas] = await connection.execute(`
          SELECT r.pregunta_id, r.respuesta, p.texto_pregunta
          FROM respuestas r
          JOIN preguntas p ON r.pregunta_id = p.id
          WHERE r.consulta_id = ?
        `, [consulta.id]);
        consulta.respuestas = respuestas;
      }
      return consultas;
    } finally {
      connection.release();
    }
  }

  async buscarConsultas(params) {
    const connection = await getConnection();
    try {
      let query = `
        SELECT c.id, c.usuario_id, c.fecha_consulta, c.diagnostico, u.nombre, u.identificacion
        FROM consultas c
        JOIN usuarios u ON c.usuario_id = u.id
        WHERE 1=1
      `;
      const values = [];

      if (params.usuario_id) {
        query += ' AND c.usuario_id = ?';
        values.push(params.usuario_id);
      }
      if (params.identificacion) {
        query += ' AND u.identificacion = ?';
        values.push(params.identificacion);
      }
      if (params.fecha_inicio) {
        query += ' AND c.fecha_consulta >= ?';
        values.push(params.fecha_inicio);
      }
      if (params.fecha_fin) {
        query += ' AND c.fecha_consulta <= ?';
        values.push(params.fecha_fin);
      }
      query += ' ORDER BY c.fecha_consulta DESC';

      const [consultas] = await connection.execute(query, values);

      for (const consulta of consultas) {
        const [respuestas] = await connection.execute(`
          SELECT r.pregunta_id, r.respuesta, p.texto_pregunta
          FROM respuestas r
          JOIN preguntas p ON r.pregunta_id = p.id
          WHERE r.consulta_id = ?
        `, [consulta.id]);
        consulta.respuestas = respuestas;
      }
      return consultas;
    } finally {
      connection.release();
    }
  }
}

module.exports = ConsultaService;