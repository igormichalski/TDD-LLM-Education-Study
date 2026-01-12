const somarDigitos = require('./Ex3.js');

describe('Função somarDigitos(numero)', () => {

  test('Deve somar os dígitos corretamente - exemplo 492', () => {
    expect(somarDigitos(492)).toBe(15); // 4 + 9 + 2 = 15
  });

  test('Deve retornar o próprio número se tiver apenas um dígito', () => {
    expect(somarDigitos(7)).toBe(7);
  });

  test('Deve funcionar com números grandes', () => {
    expect(somarDigitos(9876543210)).toBe(45); // Soma de 0 a 9
  });

  test('Deve retornar 0 se entrada for 0', () => {
    expect(somarDigitos(0)).toBe(0);
  });

  test('Deve lançar erro se entrada for número negativo', () => {
    expect(() => somarDigitos(-123)).toThrow('Entrada inválida');
  });

  test('Deve lançar erro se entrada for decimal', () => {
    expect(() => somarDigitos(12.34)).toThrow('Entrada inválida');
  });

  test('Deve lançar erro se entrada for string', () => {
    expect(() => somarDigitos('123')).toThrow('Entrada inválida');
  });

  test('Deve lançar erro se entrada for null ou undefined', () => {
    expect(() => somarDigitos(null)).toThrow('Entrada inválida');
    expect(() => somarDigitos(undefined)).toThrow('Entrada inválida');
  });

});