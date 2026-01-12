const validarSenha = require('./Ex2.js');

describe('Validação de senha segura', () => {

  test('Senha válida completa deve retornar 1', () => {
    expect(validarSenha('Segura@2025')).toBe(1);
    expect(validarSenha('Strong#1Password')).toBe(1);
  });

  test('Senha sem caractere especial deve retornar 0', () => {
    expect(validarSenha('Senha123')).toBe(0);
    expect(validarSenha('Maiuscula1')).toBe(0);
  });

  test('Senha com menos de 8 caracteres deve retornar 0', () => {
    expect(validarSenha('S@1a')).toBe(0);
    expect(validarSenha('S@1xyz')).toBe(0);
  });

  test('Senha sem letra maiúscula deve retornar 0', () => {
    expect(validarSenha('segura@2025')).toBe(0);
  });

  test('Senha sem número deve retornar 0', () => {
    expect(validarSenha('Senha@Segura')).toBe(0);
  });

  test('Senha contendo apenas requisitos parciais deve retornar 0', () => {
    expect(validarSenha('12345678')).toBe(0);
    expect(validarSenha('ABCDEFGH')).toBe(0);
    expect(validarSenha('abc@defg')).toBe(0);
  });

  test('Senha com caracteres especiais fora da whitelist deve retornar 0', () => {
    expect(validarSenha('Senha^2025')).toBe(0); // ^ não está na lista
  });

  test('Entrada não string (número) deve retornar 0', () => {
    expect(validarSenha(12345678)).toBe(0);
  });

  test('Entrada vazia deve retornar 0', () => {
    expect(validarSenha('')).toBe(0);
  });

});