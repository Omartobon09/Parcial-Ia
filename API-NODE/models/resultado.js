
const { DataTypes } = require('sequelize');
const { sequelize } = require('../config/database');

const Resultado = sequelize.define('Resultado', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  evaluacion_id: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  diagnostico_id: {
    type: DataTypes.INTEGER,
    allowNull: false
  }
}, {
  tableName: 'resultados',
  timestamps: false
});

module.exports = Resultado;