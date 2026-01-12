const isPrimo = require('./ex1.js');
describe('Testes para a função isPrimo', () => {
    
    test('Deve retornar true para 2, pois é o menor número primo', () => {
        expect(isPrimo(2)).toBe(true);
    });

    test('Deve retornar true para 5, pois é primo', () => {
        expect(isPrimo(5)).toBe(true);
    });

    test('Deve retornar false para 1, pois não é primo', () => {
        expect(isPrimo(1)).toBe(false);
    });

    test('Deve retornar false para 4, pois não é primo', () => {
        expect(isPrimo(4)).toBe(false);
    });

    test('Deve retornar true para 13, pois é primo', () => {
        expect(isPrimo(13)).toBe(true);
    });

    test('Deve retornar false para 9, pois não é primo', () => {
        expect(isPrimo(9)).toBe(false);
    });

    test('Deve retornar false para 0, pois não é primo', () => {
        expect(isPrimo(0)).toBe(false);
    });

    test('Deve retornar false para números negativos, ex: -7', () => {
        expect(isPrimo(-7)).toBe(false);
    });
    
    test('Deve retornar true para 29, pois é primo', () => {
        expect(isPrimo(29)).toBe(true);
    });

    test('Deve retornar false para 100, pois não é primo', () => {
        expect(isPrimo(100)).toBe(false);
    });

});
