const express = require("express");
const router = express.Router();
const diagnosticoController = require("../controllers/diagnosticoController");

router.post("/enviardiagnostico", diagnosticoController.crearDiagnostico);

module.exports = router;