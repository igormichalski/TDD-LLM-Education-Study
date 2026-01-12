const contaVogais = require('./ex2.js');

describe('Testes para a função contaVogais', () => {
    
    test('Entrada: "computador". Saída esperada: 4', () => {
        expect(contaVogais("computador")).toBe(4);
    });

    test('Entrada: "AEIOU". Saída esperada: 5 (testando maiúsculas)', () => {
        expect(contaVogais("AEIOU")).toBe(5);
    });

    test('Entrada: "bcdfgh". Saída esperada: 0 (sem vogais)', () => {
        expect(contaVogais("bcdfgh")).toBe(0);
    });

    test('Entrada: "ChatGPT". Saída esperada: 1 (só o "a")', () => {
        expect(contaVogais("ChatGPT")).toBe(1);
    });

    test('Entrada: "". Saída esperada: 0 (string vazia)', () => {
        expect(contaVogais("")).toBe(0);
    });

    test('Entrada: 12345. Saída esperada: "Erro" (entrada não é string)', () => {
        expect(contaVogais(12345)).toBe("Erro");
    });

    test('Entrada: null. Saída esperada: "Erro"', () => {
        expect(contaVogais(null)).toBe("Erro");
    });

    test('Entrada: "banana". Saída esperada: 3', () => {
        expect(contaVogais("banana")).toBe(3);
    });

});
