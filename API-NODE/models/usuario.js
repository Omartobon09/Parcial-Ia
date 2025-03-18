const { DataTypes, Sequelize } = require('sequelize');
const { sequelize } = require('../config/database');

const Usuario = sequelize.define('Usuario', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  nombre: {
    type: DataTypes.STRING(100),
    allowNull: false
  },
  apellido: {
    type: DataTypes.STRING(100),
    allowNull: false
  },
  usuario: {
    type: DataTypes.STRING(50),
    allowNull: false,
    unique: true
  },
  contrasena: {
    type: DataTypes.STRING(255),
    allowNull: false
  },
  rol_id: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  fecha_registro: {
    type: DataTypes.DATE,
    defaultValue: Sequelize.literal('CURRENT_TIMESTAMP')
  }
}, {
  tableName: 'usuarios',
  timestamps: false
});

module.exports = Usuario;