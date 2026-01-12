// const { validaSenha, ehPrimo } = require('./funcoes');

describe('Validador de Senha - casos principais', () => {
  test('senhas válidas', () => {
    expect(validaSenha('Senha@123')).toBe(true);
    expect(validaSenha('Abcdef1!')).toBe(true);
  });
});

describe('Validador de Senha - casos de borda e inválidos', () => {
  test('senhas inválidas', () => {
    expect(validaSenha('')).toBe(false);                 // vazia
    expect(validaSenha('senha123')).toBe(false);         // sem maiúscula e especial
    expect(validaSenha('SENHA123')).toBe(false);         // sem minúscula
    expect(validaSenha('SenhaSemNum!')).toBe(false);     // sem número
    expect(validaSenha('Senha123')).toBe(false);         // sem caractere especial
    expect(validaSenha('Ab1!')).toBe(false);             // muito curta
    expect(validaSenha(null)).toBe(false);               // inválida
  });
});

