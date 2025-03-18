const Diagnostico = require("../models/Diagnostico");

exports.crearDiagnostico = async (req, res) => {
  const { descripcion, recomendacion } = req.body;

  if (!descripcion || !recomendacion) {
    return res.status(400).send("Todos los campos son obligatorios");
  }

  try {
    await Diagnostico.create({descripcion, recomendacion });
    res.status(200).send("Diagnóstico guardado exitosamente");
  } catch (error) {
    console.error("Error al guardar el diagnóstico:", error.message);
    res.status(500).send("Error al guardar el diagnóstico");
  }
};