const { DataTypes } = require('sequelize');
const { sequelize } = require('../config/database');

const Respuesta = sequelize.define('Respuesta', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  evaluacion_id: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  pregunta_id: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  respuesta: {
    type: DataTypes.BOOLEAN,
    allowNull: false
  }
}, {
  tableName: 'respuestas',
  timestamps: false
});

module.exports = Respuesta;
