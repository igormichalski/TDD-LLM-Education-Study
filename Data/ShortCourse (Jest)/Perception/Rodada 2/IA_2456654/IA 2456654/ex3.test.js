const converteTemperatura = require('./ex3.js');

describe('Testes para a função converteTemperatura', () => {

    test('Entrada: 0, "C". Saída esperada: 32 (0°C = 32°F)', () => {
        expect(converteTemperatura(0, 'C')).toBe(32);
    });

    test('Entrada: 100, "C". Saída esperada: 212 (100°C = 212°F)', () => {
        expect(converteTemperatura(100, 'C')).toBe(212);
    });

    test('Entrada: 32, "F". Saída esperada: 0 (32°F = 0°C)', () => {
        expect(converteTemperatura(32, 'F')).toBe(0);
    });

    test('Entrada: 212, "F". Saída esperada: 100 (212°F = 100°C)', () => {
        expect(converteTemperatura(212, 'F')).toBe(100);
    });

    test('Entrada: "trinta", "C". Saída esperada: Erro (valor inválido)', () => {
        expect(converteTemperatura("trinta", "C")).toBe('Erro');
    });

    test('Entrada: 50, "K". Saída esperada: Erro (unidade inválida)', () => {
        expect(converteTemperatura(50, 'K')).toBe('Erro');
    });

    test('Entrada: null, "F". Saída esperada: Erro', () => {
        expect(converteTemperatura(null, 'F')).toBe('Erro');
    });

    test('Entrada: 0, "f". Saída esperada: Erro (sensível a maiúsculas)', () => {
        expect(converteTemperatura(0, 'f')).toBe('Erro');
    });

});
