const { DataTypes } = require("sequelize");
const { sequelize } = require("../config/database");

const Diagnostico = sequelize.define("Diagnostico", {
  nombre: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  descripcion: {
    type: DataTypes.TEXT,
    allowNull: false,
  },
  recomendacion: {
    type: DataTypes.TEXT,
    allowNull: false,
  },
  fecha: {
    type: DataTypes.DATE,
    defaultValue: DataTypes.NOW,
  },
});

module.exports = Diagnostico;