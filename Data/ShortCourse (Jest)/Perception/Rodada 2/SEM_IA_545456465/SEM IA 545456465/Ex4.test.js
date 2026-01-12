const cnp = require ('./Ex4');

describe('Checar se é primo', () =>{
    test('Deve retornar 1 para números primos', () => {
        expect(cnp(2)).toBe(1);
    });

    test('Deve retornar 0 para números não primos', () => {
        expect(cnp(4)).toBe(0);
    }); 

    test('Deve retornar 1 para números primos', () => {
        expect(cnp(3)).toBe(0);
    }); 

    test('Deve retornar 1 para números primos', () => {
        expect(cnp(5)).toBe(0);
    }); 
});