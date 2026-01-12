function validarSenha(senha) {
  if (typeof senha !== 'string') return 0;

  const minLength = senha.length >= 8;
  const hasUppercase = /[A-Z]/.test(senha);
  const hasNumber = /[0-9]/.test(senha);
  const hasSpecialChar = /[!@#$%&*]/.test(senha);

  return (minLength && hasUppercase && hasNumber && hasSpecialChar) ? 1 : 0;
}

module.exports = validarSenha;