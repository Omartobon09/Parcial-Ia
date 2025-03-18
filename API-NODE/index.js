const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");
const authRoutes = require("./routes/auth.routes");
const diagnosticoRoutes = require("./routes/diagnostico.routes");
const usuarioRoutes = require("./routes/usuario.routes");
const historialRoutes = require("./routes/historial.routes");
const { testConnection } = require("./config/database");


dotenv.config();


const app = express();


app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.use("/api/auth", authRoutes);
app.use("/api", diagnosticoRoutes);
app.use("/api/usuarios", usuarioRoutes);
app.use("/api/historial", historialRoutes);

app.get("/", (req, res) => {
  res.send("API de Centro Médico funcionando correctamente");
});


const PORT = process.env.PORT || 5000;


app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
});
