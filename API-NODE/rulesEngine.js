class RulesEngine {
    static diagnosticar(respuestas) {
      const facts = {
        dolorPecho: respuestas.find(r => r.pregunta_id === 1)?.respuesta || false,
        dificultadRespirar: respuestas.find(r => r.pregunta_id === 2)?.respuesta || false,
        mareos: respuestas.find(r => r.pregunta_id === 3)?.respuesta || false,
        hinchazonPiernas: respuestas.find(r => r.pregunta_id === 4)?.respuesta || false,
        palpitaciones: respuestas.find(r => r.pregunta_id === 5)?.respuesta || false,
      };
  
      if (facts.dolorPecho && facts.dificultadRespirar && facts.mareos && facts.palpitaciones) {
        return "Posible infarto agudo de miocardio. EMERGENCIA MÉDICA.";
      } else if (facts.dolorPecho && facts.dificultadRespirar && !facts.mareos) {
        return "Posible angina de pecho. Consulte a un médico urgentemente.";
      } 
      else if (!facts.dolorPecho && facts.mareos && facts.palpitaciones) {
          return "Posible hipertensión arterial. Mida su presión.";
      }
      else if (facts.hinchazonPiernas && !facts.dolorPecho && !facts.palpitaciones) {
          return "Posible insuficiencia venosa. Consulte a un especialista vascular.";
      }
      else if (!Object.values(facts).some(Boolean)) {
          return "No presenta síntomas específicos de problemas cardíacos.";
      }
      else {
          return "Síntomas inespecíficos. Consulte a su médico para una evaluación completa.";
      }
    }
  }
  
  module.exports = RulesEngine;