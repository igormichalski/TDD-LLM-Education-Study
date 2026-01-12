function somarDigitos(numero) {
  if (typeof numero !== 'number' || !Number.isInteger(numero) || numero < 0) {
    throw new Error('Entrada inválida: forneça um número inteiro positivo');
  }

  return numero
    .toString()
    .split('')
    .reduce((soma, digito) => soma + Number(digito), 0);
}

module.exports = somarDigitos;
