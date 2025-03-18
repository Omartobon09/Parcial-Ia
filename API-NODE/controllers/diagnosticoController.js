const Diagnostico = require("../models/diagnostico");

exports.crearDiagnostico = async (req, res) => {
  const { descripcion, recomendacion } = req.body;

  if (!descripcion || !recomendacion) {
    return res.status(400).json({
      success: false,
      message: "Todos los campos son obligatorios"
    });
  }

  try {
    const nuevoDiagnostico = await Diagnostico.create({ descripcion, recomendacion });
    
    res.status(200).json({
      success: true,
      message: "Diagnóstico guardado exitosamente",
      diagnostico: {
        
        descripcion,
        recomendacion,
    
      }
    });
  } catch (error) {
    console.error("Error al guardar el diagnóstico:", error.message);
    res.status(500).json({
      success: false,
      message: "Error al guardar el diagnóstico",
      error: error.message
    });
  }
};