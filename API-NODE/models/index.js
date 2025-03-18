const { sequelize } = require("../config/database");
const Rol = require("./rol");
const Usuario = require("./usuario");
const Diagnostico = require("./diagnostico");
const Pregunta = require("./pregunta");
const Evaluacion = require("./evaluacion");
const Respuesta = require("./respuesta");
const Resultado = require("./resultado");
const Historial = require("./historial");

// Establecer relaciones entre las tablas

// Relación entre Rol y Usuario (uno a muchos)
Rol.hasMany(Usuario, { foreignKey: "rol_id", onDelete: "CASCADE" });
Usuario.belongsTo(Rol, { foreignKey: "rol_id" });

// Relación entre Usuario y Evaluacion (uno a muchos)
Usuario.hasMany(Evaluacion, { foreignKey: "usuario_id", onDelete: "CASCADE" });
Evaluacion.belongsTo(Usuario, { foreignKey: "usuario_id" });

// Relación entre Usuario e Historial (uno a muchos)
Usuario.hasMany(Historial, { foreignKey: "usuario_id", onDelete: "CASCADE" });
Historial.belongsTo(Usuario, { foreignKey: "usuario_id" });

// Relación entre Evaluacion y Respuesta (uno a muchos)
Evaluacion.hasMany(Respuesta, {
  foreignKey: "evaluacion_id",
  onDelete: "CASCADE",
});
Respuesta.belongsTo(Evaluacion, { foreignKey: "evaluacion_id" });

// Relación entre Pregunta y Respuesta (uno a muchos)
Pregunta.hasMany(Respuesta, { foreignKey: "pregunta_id", onDelete: "CASCADE" });
Respuesta.belongsTo(Pregunta, { foreignKey: "pregunta_id" });

// Relación entre Evaluacion y Resultado (uno a muchos)
Evaluacion.hasMany(Resultado, {
  foreignKey: "evaluacion_id",
  onDelete: "CASCADE",
});
Resultado.belongsTo(Evaluacion, { foreignKey: "evaluacion_id" });

// Relación entre Diagnostico y Resultado (uno a muchos)
Diagnostico.hasMany(Resultado, {
  foreignKey: "diagnostico_id",
  onDelete: "CASCADE",
});
Resultado.belongsTo(Diagnostico, { foreignKey: "diagnostico_id" });

// Sincronización de modelos
const sincronizarModelos = async () => {
  try {
    await sequelize.sync({ alter: false });
    console.log("✅ Modelos sincronizados correctamente.");
  } catch (error) {
    console.error("❌ Error al sincronizar modelos:", error);
  }
};

module.exports = {
  sequelize,
  Rol,
  Usuario,
  Diagnostico,
  Pregunta,
  Evaluacion,
  Respuesta,
  Resultado,
  Historial,
  sincronizarModelos,
};
