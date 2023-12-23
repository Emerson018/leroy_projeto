const wait = (delay = 0) =>
  new Promise(resolve => setTimeout(resolve, delay));

const setVisible = (elementOrSelector, visible) => 
  (typeof elementOrSelector === 'string'
    ? document.querySelector(elementOrSelector)
    : elementOrSelector
  ).style.display = visible ? 'block' : 'none';

  document.getElementById('myForm').addEventListener('submit', function() {
    // Exibe o elemento de carregamento antes de enviar o formulário
    setVisible('#loading', true);

    // Simula um carregamento com um atraso de 1000ms
    wait(1000).then(() => {
        // Continua com o envio normal do formulário após o término do carregamento
        // O navegador continuará a enviar o formulário para o servidor
        // após a execução completa deste bloco de código
    });
});