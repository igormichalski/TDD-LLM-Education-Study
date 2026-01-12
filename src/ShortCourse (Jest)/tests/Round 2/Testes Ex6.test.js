// supondo que convCtoF e convFtoC estejam exportadas
// const { convCtoF, convFtoC } = require('./conversoes');

describe('Conversão de temperatura - casos principais', () => {
  test('conversões básicas entre Celsius e Fahrenheit', () => {
    expect(convCtoF(0.0)).toBeCloseTo(32.0, 5);
    expect(convFtoC(32.0)).toBeCloseTo(0.0, 5);
    expect(convCtoF(100.0)).toBeCloseTo(212.0, 5);
  });
});

describe('Conversão de temperatura - casos de borda', () => {
  test('valores extremos e especiais', () => {
    expect(convCtoF(-40.0)).toBeCloseTo(-40.0, 5);
    expect(convFtoC(98.6)).toBeCloseTo(37.0, 5);
    expect(convCtoF(-10.0)).toBeCloseTo(14.0, 5);
    expect(convCtoF(1e6)).toBeCloseTo(1800032.0, 5);
  });
});

