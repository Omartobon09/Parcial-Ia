const { sequelize } = require("../config/database");
const Rol = require("./rol");
const Usuario = require("./usuario");
const Diagnostico = require("./diagnostico");
const Pregunta = require("./pregunta");
const Evaluacion = require("./evaluacion");
const Respuesta = require("./respuesta");
const Resultado = require("./resultado");
const Historial = require("./historial");




Rol.hasMany(Usuario, { foreignKey: "rol_id", onDelete: "CASCADE" });
Usuario.belongsTo(Rol, { foreignKey: "rol_id" });

Usuario.hasMany(Evaluacion, { foreignKey: "usuario_id", onDelete: "CASCADE" });
Evaluacion.belongsTo(Usuario, { foreignKey: "usuario_id" });


Usuario.hasMany(Historial, { foreignKey: "usuario_id", onDelete: "CASCADE" });
Historial.belongsTo(Usuario, { foreignKey: "usuario_id" });


Evaluacion.hasMany(Respuesta, {
  foreignKey: "evaluacion_id",
  onDelete: "CASCADE",
});
Respuesta.belongsTo(Evaluacion, { foreignKey: "evaluacion_id" });


Pregunta.hasMany(Respuesta, { foreignKey: "pregunta_id", onDelete: "CASCADE" });
Respuesta.belongsTo(Pregunta, { foreignKey: "pregunta_id" });


Evaluacion.hasMany(Resultado, {
  foreignKey: "evaluacion_id",
  onDelete: "CASCADE",
});
Resultado.belongsTo(Evaluacion, { foreignKey: "evaluacion_id" });


Diagnostico.hasMany(Resultado, {
  foreignKey: "diagnostico_id",
  onDelete: "CASCADE",
});
Resultado.belongsTo(Diagnostico, { foreignKey: "diagnostico_id" });


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
