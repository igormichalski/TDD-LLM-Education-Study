const contarVogais = require('./Ex2_AI.js');

describe('contarVogais', () => {
  test('Conta vogais em uma palavra normal', () => {
    expect(contarVogais('abacaxi')).toBe(4);
  });

  test('Conta vogais em palavra sem vogais', () => {
    expect(contarVogais('rhythm')).toBe(0);
  });

  test('Conta vogais em palavra com letras maiúsculas', () => {
    expect(contarVogais('AbAcAxI')).toBe(4);
  });

  test('Conta vogais em string vazia', () => {
    expect(contarVogais('')).toBe(0);
  });

  test('Conta vogais em palavra com acentos (considerando só aeiou)', () => {
    expect(contarVogais('coração')).toBe(3); // o, a, o
  });

  test('Conta vogais em frase com espaços', () => {
    expect(contarVogais('O rato roeu a roupa')).toBe(10);
  });
});
