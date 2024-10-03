(function (win, doc){
    "use strict";

    //Função para editar usuário
    // Função para abrir o pop-up centralizado
    function abrirPopup(url) {
        // Tamanho do pop-up
        var width = 800;
        var height = 1280;

        // Calcula a posição no centro da tela
        var left = (win.innerWidth / 2) - (width / 2);
        var top = (win.innerHeight / 2) - (height / 2);

        // Abre a janela pop-up centralizada
        win.open(url, 'popUpWindow', `height=${height},width=${width},left=${left},top=${top},resizable=yes,scrollbars=yes,toolbar=no,menubar=no,location=no,directories=no,status=yes`);
    }

    // Expondo a função ao escopo global
    win.abrirPopup = abrirPopup;


// Para a página password_reset_form.html
    // Aguarda que o DOM esteja totalmente carregado
  doc.addEventListener("DOMContentLoaded", function() {
    // Seleciona o elemento pelo ID
    var passwordField1 = doc.getElementById('id_new_password1');
    var passwordField2 = doc.getElementById('id_new_password2');
    
    // Adiciona as classes desejadas
    if (passwordField1 && passwordField2) {
      passwordField1.classList.add('form-control');
      passwordField2.classList.add('form-control');

      passwordField1.setAttribute('aria-describedby', 'togglePassword');
      passwordField1.setAttribute('placeholder', 'Nova Senha');

      passwordField2.setAttribute('aria-describedby', 'togglePassword2');
      passwordField2.setAttribute('placeholder', 'Confirmar Nova Senha');
    }
  });

  doc.addEventListener("DOMContentLoaded", function() {
    var passwordField = doc.getElementById('id_new_password1');
    var toggleButton = doc.getElementById('togglePassword');

    toggleButton.addEventListener('click', function() {
      if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleButton.textContent = 'Esconder';
      } else {
        passwordField.type = 'password';
        toggleButton.textContent = 'Mostrar';
      }
    });

    // Para o segundo campo de senha
    var passwordField2 = doc.getElementById('id_new_password2');
    var toggleButton2 = doc.getElementById('togglePassword');

    toggleButton2.addEventListener('click', function() {
      if (passwordField2.type === 'password') {
        passwordField2.type = 'text';
        toggleButton2.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-eye" viewBox="0 0 16 16">
  <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8M1.173 8a13 13 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5s3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5s-3.879-1.168-5.168-2.457A13 13 0 0 1 1.172 8z"/>
  <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5M4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0"/>
</svg>`;
      } else {
        passwordField2.type = 'password';
        toggleButton2.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-eye-slash" viewBox="0 0 16 16">
  <path d="M13.359 11.238C15.06 9.72 16 8 16 8s-3-5.5-8-5.5a7 7 0 0 0-2.79.588l.77.771A6 6 0 0 1 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755q-.247.248-.517.486z"/>
  <path d="M11.297 9.176a3.5 3.5 0 0 0-4.474-4.474l.823.823a2.5 2.5 0 0 1 2.829 2.829zm-2.943 1.299.822.822a3.5 3.5 0 0 1-4.474-4.474l.823.823a2.5 2.5 0 0 0 2.829 2.829"/>
  <path d="M3.35 5.47q-.27.24-.518.487A13 13 0 0 0 1.172 8l.195.288c.335.48.83 1.12 1.465 1.755C4.121 11.332 5.881 12.5 8 12.5c.716 0 1.39-.133 2.02-.36l.77.772A7 7 0 0 1 8 13.5C3 13.5 0 8 0 8s.939-1.721 2.641-3.238l.708.709zm10.296 8.884-12-12 .708-.708 12 12z"/>
</svg>`;
      }
    });
  });

})(window, document);