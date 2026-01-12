function contarVogais(palavra) {
  return (palavra.match(/[aeiou]/gi) || []).length;
}

module.exports = contarVogais