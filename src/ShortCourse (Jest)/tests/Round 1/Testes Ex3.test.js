const EXPECT_ERR = -1;

// supondo que soma_digitos esteja exportada de algum módulo
// const { soma_digitos } = require('./soma_digitos');

describe('soma_digitos - casos principais', () => {
  test('deve somar corretamente os dígitos', () => {
    expect(soma_digitos(492)).toBe(15);
    expect(soma_digitos(12345)).toBe(15);
  });
});

describe('soma_digitos - casos de borda (incluindo inválidos)', () => {
  test('casos válidos simples', () => {
    expect(soma_digitos(7)).toBe(7);
    expect(soma_digitos(100000)).toBe(1);
  });

  test('números grandes', () => {
    expect(soma_digitos(9999999999n)).toBe(90);
    expect(soma_digitos(98765432109876543210n)).toBe(90);
  });

  test('casos inválidos', () => {
    expect(soma_digitos(0)).toBe(EXPECT_ERR);
    expect(soma_digitos(-123)).toBe(EXPECT_ERR);
  });
});

