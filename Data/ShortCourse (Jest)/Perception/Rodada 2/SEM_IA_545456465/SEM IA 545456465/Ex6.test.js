const c = require ('./Ex6');
describe('Verificar a conversão', () =>{
    test('Caso celcius', () =>{
        expect(ccf()).toBe(32);
    });
    test('Caso fah', () =>{
        expect(ccf(32)).toBe(0);
    });
    test('Caso celcius', () =>{
        expect(ccf(100)).toBe(212);
    });
});