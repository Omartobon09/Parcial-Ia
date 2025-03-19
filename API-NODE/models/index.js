const { sequelize } = require("../config/database");
const Rol = require("./rol");
const Usuario = require("./usuario");
const Diagnostico = require("./diagnostico");
const Resultado = require("./resultado");
const Historial = require("./historial");

Rol.hasMany(Usuario, { foreignKey: "rol_id", onDelete: "CASCADE" });
Usuario.belongsTo(Rol, { foreignKey: "rol_id" });

Usuario.hasMany(Historial, { foreignKey: "usuario_id", onDelete: "CASCADE" });
Historial.belongsTo(Usuario, { foreignKey: "usuario_id" });

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
  Historial,
  sincronizarModelos,
};
