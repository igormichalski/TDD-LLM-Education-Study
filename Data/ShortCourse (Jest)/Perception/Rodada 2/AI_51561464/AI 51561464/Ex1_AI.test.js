// funcoes.test.js
const EhPrimo = require('./Ex1_AI.js');

describe('Função EhPrimo', () => {
    // Casos para números não primos
    test('Deve retornar 0 para números negativos', () => {
        expect(EhPrimo(-1)).toBe(0);
        expect(EhPrimo(-10)).toBe(0);
    });

    test('Deve retornar 0 para 0', () => {
        expect(EhPrimo(0)).toBe(0);
    });

    test('Deve retornar 0 para 1', () => {
        expect(EhPrimo(1)).toBe(0);
    });

    test('Deve retornar 0 para números compostos', () => {
        expect(EhPrimo(4)).toBe(0); // 4 não é primo
        expect(EhPrimo(6)).toBe(0); // 6 não é primo
        expect(EhPrimo(9)).toBe(0); // 9 não é primo
        expect(EhPrimo(25)).toBe(0); // 25 não é primo
    });

    // Casos para números primos
    test('Deve retornar 1 para números primos', () => {
        expect(EhPrimo(2)).toBe(1); // 2 é primo
        expect(EhPrimo(3)).toBe(1); // 3 é primo
        expect(EhPrimo(5)).toBe(1); // 5 é primo
        expect(EhPrimo(7)).toBe(1); // 7 é primo
        expect(EhPrimo(11)).toBe(1); // 11 é primo
        expect(EhPrimo(13)).toBe(1); // 13 é primo
        expect(EhPrimo(17)).toBe(1); // 17 é primo
        expect(EhPrimo(19)).toBe(1); // 19 é primo
    });

    
    test('Deve retornar 0 para um número grande não primo', () => {
        expect(EhPrimo(104730)).toBe(0); // 104730 não é primo
    });
});
