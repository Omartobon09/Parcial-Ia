const { DataTypes } = require("sequelize");
const { sequelize } = require("../config/database");

const Diagnostico = sequelize.define(
  "Diagnostico",
  {
    descripcion: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    recomendacion: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
  },
  { timestamps: false }
); 
