const express = require('express');
const router = express.Router();
const authController = require('../controllers/auth.controller.js');
const authMiddleware = require('../middlewares/auth.middleware.js');

// Ruta de login
router.post('/login', authMiddleware.validateAuth, authController.login);

module.exports = router;