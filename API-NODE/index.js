const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");
const authRoutes = require('./routes/auth.routes'); // Importa las rutas de autenticación
const diagnosticoRoutes = require('./routes/diagnostico.routes');
const { testConnection } = require("./config/database");

// Cargar variables de entorno
dotenv.config();

// Crear la aplicación Express
const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rutas
app.use('/api/auth', authRoutes); // Agregar rutas de autenticación
app.use('/api', diagnosticoRoutes);

// Ruta de prueba
app.get('/', (req, res) => {
  res.send('API de Centro Médico funcionando correctamente');
});

// Puerto
const PORT = process.env.PORT || 5000;

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
});