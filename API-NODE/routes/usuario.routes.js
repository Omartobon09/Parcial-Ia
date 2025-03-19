const express = require("express");
const router = express.Router();
const Usuario = require("../models/usuario");
const bcrypt = require("bcrypt");

router.get("/", async (req, res) => {
  try {
    const usuarios = await Usuario.findAll();
    res.json(usuarios);
  } catch (error) {
    res.status(500).json({ error: "Error al obtener los usuarios" });
  }
});

router.get("/:id", async (req, res) => {
  try {
    const usuario = await Usuario.findByPk(req.params.id);
    if (!usuario)
      return res.status(404).json({ error: "Usuario no encontrado" });
    res.json(usuario);
  } catch (error) {
    res.status(500).json({ error: "Error al obtener el usuario" });
  }
});

router.post("/", async (req, res) => {
  try {
    const { nombre, apellido, usuario, contrasena, rol_id } = req.body;
    const hashedPassword = await bcrypt.hash(contrasena, 10);
    const nuevoUsuario = await Usuario.create({
      nombre,
      apellido,
      usuario,
      contrasena: hashedPassword,
      rol_id,
    });
    res.status(201).json(nuevoUsuario);
  } catch (error) {
    res.status(500).json({ error: "Error al crear el usuario" });
  }
});

router.put("/:id", async (req, res) => {
  try {
    const { nombre, apellido, usuario, contrasena, rol_id } = req.body;
    const usuarioExistente = await Usuario.findByPk(req.params.id);
    if (!usuarioExistente)
      return res.status(404).json({ error: "Usuario no encontrado" });

    let hashedPassword = usuarioExistente.contrasena;
    if (contrasena) {
      hashedPassword = await bcrypt.hash(contrasena, 10);
    }

    await usuarioExistente.update({
      nombre,
      apellido,
      usuario,
      contrasena: hashedPassword,
      rol_id,
    });
    res.json(usuarioExistente);
  } catch (error) {
    res.status(500).json({ error: "Error al actualizar el usuario" });
  }
});

router.delete("/:id", async (req, res) => {
  try {
    const usuario = await Usuario.findByPk(req.params.id);
    if (!usuario)
      return res.status(404).json({ error: "Usuario no encontrado" });
    await usuario.destroy();
    res.json({ message: "Usuario eliminado correctamente" });
  } catch (error) {
    res.status(500).json({ error: "Error al eliminar el usuario" });
  }
});

module.exports = router;
