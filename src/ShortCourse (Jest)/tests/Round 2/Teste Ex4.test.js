describe('Checador de Número Primo - casos principais', () => {
  test('números primos', () => {
    expect(ehPrimo(2)).toBe(true);
    expect(ehPrimo(3)).toBe(true);
    expect(ehPrimo(7)).toBe(true);
    expect(ehPrimo(13)).toBe(true);
  });
});

describe('Checador de Número Primo - casos de borda e inválidos', () => {
  test('números não primos', () => {
    expect(ehPrimo(1)).toBe(false);
    expect(ehPrimo(0)).toBe(false);
    expect(ehPrimo(-7)).toBe(false);
    expect(ehPrimo(4)).toBe(false);
    expect(ehPrimo(100)).toBe(false);
  });

  test('valores especiais', () => {
    expect(ehPrimo(99991)).toBe(true);   // primo grande
    expect(ehPrimo(99999)).toBe(false);
  });
});

