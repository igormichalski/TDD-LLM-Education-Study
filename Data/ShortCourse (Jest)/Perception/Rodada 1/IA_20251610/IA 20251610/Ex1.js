function mdc(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Ambos os argumentos devem ser números');
    }

    a = Math.abs(Math.floor(a));
    b = Math.abs(Math.floor(b));

    while (b != 0) {
        var temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

module.exports = mdc;