// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.querySelector(anchor.getAttribute('href'));
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});

// Toggle mobile menu
function toggleMenu() {
    const menu = document.getElementById('nav-menu');
    const isExpanded = menu.classList.toggle('hidden');
    document.querySelector('[aria-label="Toggle menu"]').setAttribute('aria-expanded', !isExpanded);
}

// GSAP animations
document.addEventListener('DOMContentLoaded', () => {
    gsap.registerPlugin(ScrollTrigger);
    document.querySelectorAll('.fade-in').forEach((element) => {
        gsap.to(element, {
            scrollTrigger: {
                trigger: element,
                start: 'top 80%',
                toggleActions: 'play none none none',
            },
            opacity: 1,
            y: 0,
            duration: 0.6,
        });
    });
});

// Chatbot functionality
function toggleChatbot() {
    const chatbotWindow = document.getElementById('chatbot-window');
    chatbotWindow.classList.toggle('active');
}

function submitChat() {
    const input = document.getElementById('chatbot-input').value;
    alert(`Your question: ${input}\nWe’ll get back to you soon! For now, use email or WhatsApp.`);
    // Future: Integrate Rust WebAssembly chatbot
}