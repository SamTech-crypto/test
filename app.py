import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Nexlify Solutions", layout="wide")

st.title("Nexlify Solutions - Fintech & ESG Specialist for SMEs")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Nexlify Solutions: Fintech & ESG Solutions for SMEs, Powered by AI and Blockchain.">
    <meta name="robots" content="index, follow">
    <title>Nexlify Solutions - Fintech & ESG Specialist for SMEs</title>
    
    <!-- TailwindCSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Fonts & Animations -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>

    <style>
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
        }

        .animated-bg {
            background: linear-gradient(270deg, #0f766e, #10b981, #06b6d4, #9333ea);
            background-size: 800% 800%;
            animation: gradientShift 18s ease infinite;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
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
    </style>
</head>
<body class="bg-gray-100 text-gray-800">

    <!-- Navbar -->
    <nav class="bg-teal-800 text-white p-4 shadow-lg">
        <div class="max-w-7xl mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold">Nexlify Solutions</h1>
            <ul class="hidden md:flex space-x-6 text-sm">
                <li><a href="#home" class="hover:text-emerald-300 transition">Home</a></li>
                <li><a href="#projects" class="hover:text-emerald-300 transition">Projects</a></li>
                <li><a href="#solutions" class="hover:text-emerald-300 transition">Solutions</a></li>
                <li><a href="#contact" class="hover:text-emerald-300 transition">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="animated-bg text-white py-28 px-6 text-center">
        <div class="max-w-3xl mx-auto">
            <h2 class="text-5xl font-extrabold mb-6">Powering SMEs with Fintech & ESG Intelligence</h2>
            <p class="text-xl mb-8">AI-driven insights, blockchain compliance, and DeFi-ready funding solutions.</p>
            <div class="flex justify-center gap-4 flex-wrap">
                <a href="#contact" class="bg-emerald-500 hover:bg-emerald-600 text-white font-bold py-3 px-6 rounded-full transition-all">Book a Consultation</a>
                <a href="#solutions" class="bg-white text-teal-800 font-semibold py-3 px-6 rounded-full hover:bg-gray-100 transition-all">Our Solutions</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-teal-800 text-white text-center py-6">
        <p>© 2025 Nexlify Solutions. All rights reserved.</p>
    </footer>

    <!-- Chatbot -->
    <div class="chatbot-btn" onclick="toggleChatbot()" aria-label="Open chatbot">
        💬
    </div>
    <div class="chatbot-window" id="chatbot-window">
        <h3 class="text-lg font-semibold mb-2">Chat with Us</h3>
        <input type="text" id="chatbot-input" placeholder="Ask something..." class="border border-teal-500 w-full p-2 rounded mb-2">
        <button onclick="submitChat()" class="bg-emerald-500 hover:bg-emerald-600 text-white px-4 py-2 rounded w-full">Send</button>
    </div>

    <script>
        // GSAP fade-in
        document.addEventListener('DOMContentLoaded', () => {
            gsap.registerPlugin(ScrollTrigger);
            document.querySelectorAll('.fade-in').forEach((el) => {
                gsap.fromTo(el, 
                    { opacity: 0, y: 40 }, 
                    { opacity: 1, y: 0, duration: 0.8, scrollTrigger: el }
                );
            });
        });

        // Chatbot functionality
        function toggleChatbot() {
            const bot = document.getElementById('chatbot-window');
            bot.classList.toggle('active');
        }

        function submitChat() {
            const input = document.getElementById('chatbot-input').value;
            if (input.trim()) {
                alert(`Your question: "${input}"\nWe'll reply soon via email or WhatsApp.`);
                document.getElementById('chatbot-input').value = '';
            }
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=1200, scrolling=True)
