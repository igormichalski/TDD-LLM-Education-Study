const EXPECT_ERR = -1;

// supondo que conta_vogais esteja exportada de algum módulo
// const { conta_vogais } = require('./conta_vogais');

describe('conta_vogais - casos principais', () => {
  test('deve contar corretamente as vogais em strings comuns', () => {
    expect(conta_vogais('ChatGPT')).toBe(1);
    expect(conta_vogais('Inteligência Artificial')).toBe(10);
  });
});

describe('conta_vogais - casos de borda (incluindo inválidos)', () => {
  test('strings válidas especiais', () => {
    expect(conta_vogais('')).toBe(0);
    expect(conta_vogais('rhythm')).toBe(0);
    expect(conta_vogais('aeiouAEIOU')).toBe(10);
    expect(conta_vogais('Olá, mundo!')).toBe(4);
    expect(conta_vogais('  a  A  \t \n  ')).toBe(2);
    expect(conta_vogais('àéîõü café CAÇÃO')).toBe(8);
  });

  test('caso inválido', () => {
    expect(conta_vogais(null)).toBe(EXPECT_ERR);
  });
});

