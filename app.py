import streamlit as st
import streamlit.components.v1 as components

# Title for the Streamlit app
st.title("Nexlify Solutions - Fintech & ESG Specialist for SMEs")

# Embed the HTML content
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Nexlify Solutions: Fintech & ESG Solutions for SMEs, Powered by AI and Blockchain.">
    <meta name="keywords" content="fintech for SMEs, ESG compliance, DeFi financing, AI analytics, financial strategist, startup growth">
    <meta name="author" content="Nexlify Solutions">
    <meta name="robots" content="index, follow">
    <title>Nexlify Solutions - Fintech & ESG Specialist for SMEs</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
        }
        .gradient-hero {
            background: linear-gradient(135deg, #0f766e 0%, #10b981 100%);
        }
        .animate-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            background: linear-gradient(145deg, #ffffff, #f3f4f6);
        }
        .animate-card:hover {
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }
        .btn-accent {
            background-color: #10b981;
            color: white;
            font-weight: 600;
            padding: 0.75rem 2rem;
            border-radius: 9999px;
            text-decoration: none;
            transition: background-color 0.3s ease;
        }
        .btn-accent:hover {
            background-color: #059669;
        }
        .chatbot-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #0f766e;
            color: white;
            padding: 12px;
            border-radius: 50%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            z-index: 1000;
            transition: transform 0.2s ease;
        }
        .chatbot-btn:hover {
            transform: scale(1.1);
        }
        .chatbot-window {
            position: fixed;
            bottom: 80px;
            right: 20px;
            width: 300px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            display: none;
            z-index: 1000;
            border: 1px solid #10b981;
            padding: 10px;
        }
        .chatbot-window.active {
            display: block;
        }
        .chatbot-window input {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #10b981;
            border-radius: 4px;
        }
        .chatbot-window button {
            background-color: #10b981;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .chatbot-window button:hover {
            background-color: #059669;
        }
    </style>
</head>
<body class="bg-gray-100">
    <!-- Navbar -->
    <nav class="bg-teal-700 text-white p-4 sticky top-0 z-20 shadow-lg" role="navigation" aria-label="Main navigation">
        <div class="container mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold">Nexlify Solutions</h1>
            <button class="md:hidden focus:outline-none" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav-menu" onclick="toggleMenu()">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
                </svg>
                <span class="sr-only">Toggle menu</span>
            </button>
            <ul class="hidden md:flex space-x-6" id="nav-menu">
                <li><a href="#home" class="hover:text-emerald-200 transition-colors">Home</a></li>
                <li><a href="#projects" class="hover:text-emerald-200 transition-colors">Projects</a></li>
                <li><a href="#case-studies" class="hover:text-emerald-200 transition-colors">Case Studies</a></li>
                <li><a href="#solutions" class="hover:text-emerald-200 transition-colors">Solutions</a></li>
                <li><a href="#why-esg-defi" class="hover:text-emerald-200 transition-colors">Why ESG & DeFi</a></li>
                <li><a href="#blog" class="hover:text-emerald-200 transition-colors">Blog</a></li>
                <li><a href="#faq" class="hover:text-emerald-200 transition-colors">FAQ</a></li>
                <li><a href="#contact" class="hover:text-emerald-200 transition-colors">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content -->
    <main>
        <section id="home" class="gradient-hero text-white py-24" role="region" aria-label="Home">
            <div class="container mx-auto text-center">
                <h2 class="text-5xl font-extrabold mb-6 fade-in">Fintech & ESG Solutions for SMEs</h2>
                <p class="text-xl max-w-3xl mx-auto mb-8 fade-in">Nexlify Solutions delivers AI-driven fintech and ESG tools, cutting costs by up to 60% and boosting SME growth with blockchain and quantum tech.</p>
                <div class="flex justify-center space-x-4 flex-wrap gap-4">
                    <a href="#contact" class="btn-accent fade-in">Book a Free Consultation</a>
                    <a href="#projects" class="inline-block bg-teal-600 text-white font-semibold py-3 px-8 rounded-full hover:bg-teal-700 transition-colors fade-in">Explore Solutions</a>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-teal-700 text-white py-6" role="contentinfo">
        <div class="container mx-auto text-center">
            <p>© 2025 Nexlify Solutions. All rights reserved.</p>
        </div>
    </footer>

    <!-- Chatbot -->
    <div class="chatbot-btn" onclick="toggleChatbot()" aria-label="Open chatbot">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path>
        </svg>
    </div>
    <div class="chatbot-window" id="chatbot-window">
        <h3 class="text-lg font-semibold mb-2">Chat with Us</h3>
        <input type="text" id="chatbot-input" placeholder="Type your question..." aria-label="Chatbot input">
        <button onclick="submitChat()">Send</button>
    </div>

    <script>
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
            anchor.addEventListener('click', (e) => {
                e.preventDefault();
                const target = document.querySelector(anchor.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
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
                gsap.fromTo(element, 
                    { opacity: 0, y: 50 },
                    { 
                        opacity: 1, 
                        y: 0, 
                        duration: 0.6,
                        scrollTrigger: {
                            trigger: element,
                            start: 'top 80%',
                            toggleActions: 'play none none none',
                        }
                    }
                );
            });
        });

        // Chatbot functionality
        function toggleChatbot() {
            const chatbotWindow = document.getElementById('chatbot-window');
            chatbotWindow.classList.toggle('active');
        }

        function submitChat() {
            const input = document.getElementById('chatbot-input').value;
            if (input.trim()) {
                alert(`Your question: ${input}\nWe’ll get back to you soon! For now, use email or WhatsApp.`);
                document.getElementById('chatbot-input').value = '';
            }
        }
    </script>
</body>
</html>
"""

# Render the HTML in Streamlit
components.html(html_code, height=800, scrolling=True)
