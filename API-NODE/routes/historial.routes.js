const express = require('express');
const router = express.Router();
const Historial = require('../models/historial');

router.get('/', async (req, res) => {
  try {
    const historial = await Historial.findAll();
    res.json(historial);
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener el historial' });
  }
});


router.get('/:id', async (req, res) => {
  try {
    const historial = await Historial.findByPk(req.params.id);
    if (!historial) {
      return res.status(404).json({ error: 'Registro no encontrado' });
    }
    res.json(historial);
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener el registro' });
  }
});


router.post('/', async (req, res) => {
  try {
    const { usuario_id, descripcion } = req.body;
    if (!usuario_id || !descripcion) {
      return res.status(400).json({ error: 'usuario_id y descripcion son requeridos' });
    }
    const nuevoHistorial = await Historial.create({ usuario_id, descripcion });
    res.status(201).json(nuevoHistorial);
  } catch (error) {
    res.status(500).json({ error: 'Error al crear el registro' });
  }
});


router.delete('/:id', async (req, res) => {
  try {
    const historial = await Historial.findByPk(req.params.id);
    if (!historial) {
      return res.status(404).json({ error: 'Registro no encontrado' });
    }
    await historial.destroy();
    res.json({ message: 'Registro eliminado correctamente' });
  } catch (error) {
    res.status(500).json({ error: 'Error al eliminar el registro' });
  }
});

module.exports = router;
