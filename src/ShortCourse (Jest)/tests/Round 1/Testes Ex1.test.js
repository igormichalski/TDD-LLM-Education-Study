const EXPECT_ERR = -1;

// supondo que mdc esteja exportada de algum módulo
// const { mdc } = require('./mdc');

describe('mdc - casos principais', () => {
  test('deve calcular corretamente o máximo divisor comum', () => {
    expect(mdc(12, 18)).toBe(6);
    expect(mdc(25, 30)).toBe(5);
    expect(mdc(7, 7)).toBe(7);
    expect(mdc(18, 12)).toBe(6);
  });
});

describe('mdc - casos de borda (incluindo inválidos)', () => {
  test('casos válidos de borda', () => {
    expect(mdc(8, 32)).toBe(8);
    expect(mdc(35, 64)).toBe(1);
    expect(mdc(1, 99991)).toBe(1);
    expect(mdc(123456, 789012)).toBe(12);
  });

  test('casos inválidos', () => {
    expect(mdc(0, 5)).toBe(EXPECT_ERR);
    expect(mdc(-4, 10)).toBe(EXPECT_ERR);
  });
});

