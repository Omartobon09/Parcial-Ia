const { Sequelize } = require("sequelize");
const dotenv = require("dotenv");

// Cargar variables de entorno
dotenv.config();

// Configuración de Sequelize
const sequelize = new Sequelize(
  process.env.DB_NAME || "centro_medico_db",
  process.env.DB_USER || "root",
  process.env.DB_PASSWORD || "",
  {
    host: process.env.DB_HOST || "localhost",
    dialect: "mysql",
    logging: false, // Desactiva logs de SQL en la consola
  }
);

// Función para probar la conexión
async function testConnection() {
  try {
    await sequelize.authenticate();
    console.log("Conexión exitosa a la base de datos");
    return true;
  } catch (error) {
    console.error("Error al conectar a la base de datos:", error.message);
    return false;
  }
}

// Exportar Sequelize y la función de prueba
module.exports = { sequelize, testConnection };