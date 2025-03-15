const express = require('express');
const bodyParser = require('body-parser');
const UsuarioService = require('./services/usuarioService');
const ConsultaService = require('./services/consultaService');
const RulesEngine = require('./rulesEngine');

const app = express();
const port = 8000;

app.use(bodyParser.json());

const usuarioService = new UsuarioService();
const consultaService = new ConsultaService();

app.get('/', (req, res) => {
  res.json({ message: 'Bienvenido a la API del Sistema de Diagnóstico Circulatorio' });
});

app.post('/usuarios/', async (req, res) => {
  const usuarioExistente = await usuarioService.buscarUsuarioPorIdentificacion(req.body.identificacion);
  if (usuarioExistente) {
    res.json({ id: usuarioExistente.id, message: 'Usuario ya existe' });
    return;
  }

  const usuarioId = await usuarioService.crearUsuario(req.body);
  res.status(201).json({ id: usuarioId, message: 'Usuario creado exitosamente' });
});

app.post('/consultas/', async (req, res) => {
  const consultaId = await consultaService.crearConsulta(req.body);
  res.status(201).json({ id: consultaId, message: 'Consulta registrada exitosamente' });
});

app.get('/consultas/todas/', async (req, res) => {
  const consultas = await consultaService.obtenerTodasConsultas();
  res.json(consultas);
});

app.post('/consultas/buscar/', async (req, res) => {
  const consultas = await consultaService.buscarConsultas(req.body);
  res.json(consultas);
});

app.post('/diagnosticar/', (req, res) => {
  const diagnostico = RulesEngine.diagnosticar(req.body);
  res.json({ diagnostico });
});

app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});