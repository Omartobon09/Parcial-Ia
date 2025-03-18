const { DataTypes } = require('sequelize');
const { sequelize } = require('../config/database');

const Pregunta = sequelize.define('Pregunta', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  texto: {
    type: DataTypes.STRING(255),
    allowNull: false
  }
}, {
  tableName: 'preguntas',
  timestamps: false
});

module.exports = Pregunta;
