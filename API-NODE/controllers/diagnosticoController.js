const Diagnostico = require("../models/Diagnostico");

exports.crearDiagnostico = async (req, res) => {
  const { nombre, diagnostico, recomendacion } = req.body;

  if (!nombre || !diagnostico || !recomendacion) {
    return res.status(400).send("Todos los campos son obligatorios");
  }

  try {
    await Diagnostico.create({ nombre, descripcion: diagnostico, recomendacion });
    res.status(200).send("Diagnóstico guardado exitosamente");
  } catch (error) {
    console.error("Error al guardar el diagnóstico:", error.message);
    res.status(500).send("Error al guardar el diagnóstico");
  }
};