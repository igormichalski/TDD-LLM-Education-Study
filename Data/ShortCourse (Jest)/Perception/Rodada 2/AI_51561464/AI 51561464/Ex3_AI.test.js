const fahrenheitParaCelsius = require('./Ex3_AI.js');

describe('Conversão de Fahrenheit para Celsius', () => {
  
  test('32°F deve ser 0°C', () => {
    expect(fahrenheitParaCelsius(32)).toBeCloseTo(0, 2);
  });

  test('212°F deve ser 100°C', () => {
    expect(fahrenheitParaCelsius(212)).toBeCloseTo(100, 2);
  });

  test('98.6°F deve ser aproximadamente 37°C (temperatura corporal)', () => {
    expect(fahrenheitParaCelsius(98.6)).toBeCloseTo(37, 1);
  });

  test('0°F deve ser -17.78°C', () => {
    expect(fahrenheitParaCelsius(0)).toBeCloseTo(-17.78, 2);
  });

  test('-40°F deve ser -40°C (único ponto igual)', () => {
    expect(fahrenheitParaCelsius(-40)).toBeCloseTo(-40, 2);
  });

});
