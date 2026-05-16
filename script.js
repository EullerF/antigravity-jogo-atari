// script.js - Lógica interativa para o portfólio

// Função para exibir um alerta simples ao clicar no botão 'Ver mais'
function showDetails(projectName) {
    alert(`Detalhes sobre o projeto: ${projectName}\n\nEssa é uma funcionalidade interativa construída com JavaScript puro!`);
}

// Configuração da animação de revelação ao rolar a página (Scroll Reveal)
document.addEventListener('DOMContentLoaded', () => {
    // Configura as opções para o Intersection Observer
    const observerOptions = {
        root: null, // usa a viewport do navegador
        rootMargin: '0px',
        threshold: 0.15 // 15% do elemento precisa estar visível para disparar
    };

    // Callback que adiciona a classe 'visible' quando o elemento aparece na tela
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Opcional: pode descomentar a linha abaixo para que a animação aconteça apenas uma vez
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Seleciona todos os elementos com a classe .fade-in e os observa
    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach(el => observer.observe(el));
});
