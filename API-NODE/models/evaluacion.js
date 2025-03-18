const { DataTypes, Sequelize } = require('sequelize');
const { sequelize } = require('../config/database');

const Evaluacion = sequelize.define('Evaluacion', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  usuario_id: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  fecha: {
    type: DataTypes.DATE,
    defaultValue: Sequelize.literal('CURRENT_TIMESTAMP')
  }
}, {
  tableName: 'evaluaciones',
  timestamps: false
});

module.exports = Evaluacion;
