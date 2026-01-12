const mdc = require('./Ex1.js');

describe('Função mdc(a, b)', () => {

    test('Deve retornar 1 para números primos entre si (17, 4)', () => {
        expect(mdc(17, 4)).toBe(1);
    });

    test('Deve retornar o próprio número quando ambos forem iguais', () => {
        expect(mdc(9, 9)).toBe(9);
        expect(mdc(100, 100)).toBe(100);
    });

    test('Deve funcionar com múltiplos simples (20, 8) => 4', () => {
        expect(mdc(20, 8)).toBe(4);
    });

    test('Deve funcionar com números grandes (462, 1071)', () => {
        expect(mdc(462, 1071)).toBe(21);
    });

    test('Deve retornar o maior quando um divide o outro (36, 12)', () => {
        expect(mdc(36, 12)).toBe(12);
    });

    test('Deve retornar o outro número quando um deles é 0', () => {
        expect(mdc(0, 7)).toBe(7);
        expect(mdc(7, 0)).toBe(7);
        expect(mdc(0, 0)).toBe(0);  // Discussível: por definição matemática, pode lançar erro
    });

    test('Deve funcionar com números negativos', () => {
        expect(mdc(-20, 8)).toBe(4);
        expect(mdc(20, -8)).toBe(4);
        expect(mdc(-20, -8)).toBe(4);
    });

    test('Deve ignorar parte decimal e funcionar apenas com inteiros', () => {
        expect(mdc(15.9, 9.2)).toBe(mdc(15, 9)); // comportamento implícito
    });

    test('Deve lançar erro se entradas não forem números', () => {
        expect(() => mdc('a', 5)).toThrow();
        expect(() => mdc(10, null)).toThrow();
        expect(() => mdc(undefined, 3)).toThrow();
        expect(() => mdc({}, [])).toThrow();
    });

});
