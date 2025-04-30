# test---Nextlify code....update May 1st 2025

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Nexlify Solutions: AI-driven Fintech & ESG Solutions for SMEs, powered by blockchain and quantum tech. Explore Samuel Mwendwa’s mentorship at The Founder Institute since 2023, competitor benchmarking, financial projections, and technical deep dives.">
    <meta name="keywords" content="fintech for SMEs, ESG compliance, DeFi financing, AI analytics, blockchain developer, Samuel Mwendwa, Founder Institute mentor, competitor benchmarking, financial projections, technical deep dives">
    <meta name="author" content="Nexlify Solutions">
    <title>Nexlify Solutions - Fintech & ESG Specialist for SMEs</title>
    <link rel="icon" type="image/x-icon" href="data:image/x-icon;base64,AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAKCgoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background: #f3f4f6;
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
        .fade-in {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease-out, transform 0.6s ease-out;
        }
        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            border: 0;
        }
        .chatbot-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #0f766e;
            color: white;
            padding: 16px;
            border-radius: 50%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            z-index: 1000;
            transition: transform 0.2s ease, background-color 0.3s ease;
        }
        .chatbot-btn:hover {
            transform: scale(1.1);
            background-color: #10b981;
        }
        .chatbot-window {
            position: fixed;
            bottom: 80px;
            right: 20px;
            width: 320px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            display: none;
            z-index: 1000;
            border: 1px solid #10b981;
        }
        .chatbot-window.active {
            display: block;
        }
        .quick-reply-btn {
            background-color: #f3f4f6;
            color: #0f766e;
            padding: 8px 12px;
            margin: 4px;
            border-radius: 20px;
            cursor: pointer;
            transition: background-color 0.2s ease, color 0.2s ease;
        }
        .quick-reply-btn:hover {
            background-color: #10b981;
            color: white;
        }
        nav, footer {
            background-color: #0f766e;
            transition: background-color 0.3s ease;
        }
        nav:hover {
            background-color: #115e59;
        }
        .btn-accent {
            background-color: #f59e0b;
            color: white;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        .btn-accent:hover {
            background-color: #d97706;
            transform: scale(1.05);
        }
        .testimonial-container {
            background: linear-gradient(135deg, #10b981 0%, #0f766e 100%);
            padding: 20px;
            border-radius: 12px;
            overflow: hidden;
            position: relative;
        }
        .testimonial-track {
            display: flex;
            animation: scroll-left 20s linear infinite;
        }
        .testimonial-track:hover {
            animation-play-state: paused;
        }
        .testimonial-card {
            flex: 0 0 auto;
            background: white;
            padding: 16px;
            margin-right: 16px;
            border-radius: 8px;
            width: 300px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        @keyframes scroll-left {
            0% { transform: translateX(0); }
            100% { transform: translateX(-100%); }
        }
        .faq-item {
            cursor: pointer;
            transition: background-color 0.2s ease;
        }
        .faq-item:hover {
            background-color: #f3f4f6;
        }
        .faq-answer {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
        }
        .faq-answer.active {
            max-height: 200px;
        }
        .color-change-text {
            animation: colorChange 5s infinite;
        }
        @keyframes colorChange {
            0% { color: #f59e0b; }
            50% { color: #10b981; }
            100% { color: #f59e0b; }
        }
        .filter-btn {
            background-color: #e5e7eb;
            color: #0f766e;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .filter-btn.active, .filter-btn:hover {
            background-color: #10b981;
            color: white;
        }
        .project-img {
            border-radius: 8px;
            transition: transform 0.3s ease;
        }
        .project-img:hover {
            transform: scale(1.1);
        }
        .chart-container {
            max-width: 600px;
            margin: 0 auto;
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 16px;
        }
        .comparison-table th, .comparison-table td {
            border: 1px solid #e5e7eb;
            padding: 12px;
            text-align: left;
        }
        .comparison-table th {
            background-color: #0f766e;
            color: white;
        }
        .comparison-table tr:nth-child(even) {
            background-color: #f3f4f6;
        }
    </style>
</head>
<body class="bg-gray-100">
    <!-- Navbar -->
    <nav class="bg-teal-700 text-white p-4 sticky top-0 z-20 shadow-lg" role="navigation" aria-label="Main navigation">
        <div class="container mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold">Nexlify Solutions</h1>
            <button class="md:hidden focus:outline-none" aria-label="Toggle menu" onclick="toggleMenu()">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
                </svg>
                <span class="sr-only">Toggle menu</span>
            </button>
            <ul class="hidden md:flex space-x-6" id="nav-menu">
                <li><a href="#home" class="hover:text-emerald-200 transition-colors">Home</a></li>
                <li><a href="#projects" class="hover:text-emerald-200 transition-colors">Solutions</a></li>
                <li><a href="#innovators" class="hover:text-emerald-200 transition-colors">Our Innovators</a></li>
                <li><a href="#expertise" class="hover:text-emerald-200 transition-colors">Expertise Showcase</a></li>
                <li><a href="#case-studies" class="hover:text-emerald-200 transition-colors">Case Studies</a></li>
                <li><a href="#blog" class="hover:text-emerald-200 transition-colors">Blog</a></li>
                <li><a href="#faq" class="hover:text-emerald-200 transition-colors">FAQ</a></li>
                <li><a href="#contact" class="hover:text-emerald-200 transition-colors">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content -->
    <main>
        <!-- Home Section -->
        <section id="home" class="gradient-hero text-white py-24" role="region" aria-label="Home">
            <div class="container mx-auto text-center">
                <h2 class="text-5xl font-extrabold mb-6 fade-in color-change-text">AI-Driven Fintech & ESG Solutions</h2>
                <p class="text-xl max-w-3xl mx-auto mb-8 fade-in">Nexlify Solutions, powered by Samuel Mwendwa’s expertise and mentorship at The Founder Institute since 2023, delivers AI, blockchain, and quantum tools to cut SME costs by up to 60% and drive growth.</p>
                <div class="flex justify-center space-x-4 flex-wrap gap-4">
                    <a href="#contact" class="inline-block btn-accent font-semibold py-3 px-8 rounded-full transition-colors fade-in">Book a Free Consultation</a>
                    <a href="#projects" class="inline-block bg-teal-600 text-white font-semibold py-3 px-8 rounded-full hover:bg-teal-700 transition-colors fade-in">Explore Solutions</a>
                </div>
            </div>
        </section>

        <!-- Why ESG & DeFi Section -->
        <section id="why-esg-defi" class="py-20 bg-gray-100" role="region" aria-label="Why ESG & DeFi">
            <div class="container mx-auto text-center">
                <h2 class="text-4xl font-bold mb-8 fade-in text-teal-800 color-change-text">Why ESG & DeFi Matter</h2>
                <p class="text-lg max-w-3xl mx-auto mb-8 fade-in text-gray-700">ESG compliance attracts investors, while DeFi unlocks low-cost financing. Our AI and blockchain tools simplify both for SMEs.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">ESG Benefits</h3>
                        <p class="text-gray-600 mb-4">Align with investor demands and cut reporting costs by 70% with <span class="color-change-text">*ESG Scoring Engine*</span>.</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">DeFi Advantages</h3>
                        <p class="text-gray-600 mb-4">Access low-cost loans via blockchain with <span class="color-change-text">*InvoFi*</span>, saving 60% on transactions.</p>
                    </div>
                </div>
                <a href="#contact" class="mt-6 inline-block btn-accent text-white py-3 px-8 rounded-full transition-colors fade-in">Learn How We Help</a>
            </div>
        </section>

        <!-- Projects Section -->
        <section id="projects" class="py-20 bg-gray-100" role="region" aria-label="Projects">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-8 fade-in text-teal-800 color-change-text">Our Solutions</h2>
                <p class="text-lg text-center max-w-2xl mx-auto mb-8 fade-in text-gray-700">Discover our AI, blockchain, and quantum solutions, developed by Samuel Mwendwa, tailored for SMEs and showcasing expertise for employers.</p>
                <!-- Project Filters -->
                <div class="flex justify-center space-x-4 mb-12 fade-in">
                    <button class="filter-btn active" onclick="filterProjects('all')">All</button>
                    <button class="filter-btn" onclick="filterProjects('ai')">AI</button>
                    <button class="filter-btn" onclick="filterProjects('blockchain')">Blockchain</button>
                    <button class="filter-btn" onclick="filterProjects('esg')">ESG</button>
                    <button class="filter-btn" onclick="filterProjects('quantum')">Quantum</button>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8" id="project-grid">
                    <!-- ESG Scoring Engine -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in project-card" data-category="esg ai">
                        <img src="https://via.placeholder.com/300x150.png?text=ESG+Scoring+Engine" alt="ESG Scoring Engine dashboard" class="w-full h-40 object-cover mb-4 project-img">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">ESG Scoring Engine</h3>
                        <p class="text-gray-600 mb-4">AI-powered ESG scoring with Ethereum blockchain transparency, reducing compliance costs by 70%.</p>
                        <p><strong>Tools:</strong> TensorFlow, Ethereum, Streamlit</p>
                        <p class="text-gray-600 mt-2"><strong>Impact:</strong> Attracted $2M in funding for startups.</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/esg-scoring-engine" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="https://esg-scoring-engine.streamlit.app" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                    <!-- CFO AI Agent -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in project-card" data-category="ai">
                        <img src="https://via.placeholder.com/300x150.png?text=CFO+AI+Agent" alt="CFO AI Agent interface" class="w-full h-40 object-cover mb-4 project-img">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">CFO AI Agent</h3>
                        <p class="text-gray-600 mb-4">AI assistant for CFOs with forecasting and anomaly detection, saving 40% on reporting time.</p>
                        <p><strong>Tools:</strong> LangChain, Pinecone, Streamlit</p>
                        <p class="text-gray-600 mt-2"><strong>Impact:</strong> Improved forecasting accuracy by 30%.</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/cfo-ai-agent" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="https://cfo-ai-agent.streamlit.app" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                    <!-- InvoFi -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in project-card" data-category="blockchain">
                        <img src="https://via.placeholder.com/300x150.png?text=InvoFi" alt="InvoFi platform" class="w-full h-40 object-cover mb-4 project-img">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">InvoFi</h3>
                        <p class="text-gray-600 mb-4">Decentralized invoice financing platform, cutting transaction costs by 60%.</p>
                        <p><strong>Tools:</strong> Solidity, Chainlink, Streamlit</p>
                        <p class="text-gray-600 mt-2"><strong>Impact:</strong> Improved cash flow for 50+ SMEs.</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/invofi" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="https://invofi.streamlit.app" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                    <!-- Fraud Monitoring Dashboard -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in project-card" data-category="ai">
                        <img src="https://via.placeholder.com/300x150.png?text=Fraud+Monitoring" alt="Fraud Monitoring Dashboard" class="w-full h-40 object-cover mb-4 project-img">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">Fraud Monitoring Dashboard</h3>
                        <p class="text-gray-600 mb-4">Real-time transaction monitoring with AI, reducing fraud detection time by 50%.</p>
                        <p><strong>Tools:</strong> scikit-learn, Tableau, Streamlit</p>
                        <p class="text-gray-600 mt-2"><strong>Impact:</strong> Saved $500K in fraud losses.</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/fraud-monitoring-dashboard" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="https://fraud-monitoring-dashboard.streamlit.app" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                    <!-- Quantum Financial Optimizer -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in project-card" data-category="quantum">
                        <img src="https://via.placeholder.com/300x150.png?text=Quantum+Optimizer" alt="Quantum Financial Optimizer" class="w-full h-40 object-cover mb-4 project-img">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">Quantum Financial Optimizer</h3>
                        <p class="text-gray-600 mb-4">Reduces portfolio risk by 40% using quantum computing.</p>
                        <p><strong>Tools:</strong> Qiskit, AWS Braket, Python</p>
                        <p class="text-gray-600 mt-2"><strong>Impact:</strong> Optimized $10M portfolios.</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/quantum-financial-optimizer" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="https://quantum-financial-optimizer.streamlit.app" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                    <!-- AuditFlow -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in project-card" data-category="ai">
                        <img src="https://via.placeholder.com/300x150.png?text=AuditFlow" alt="AuditFlow workflow" class="w-full h-40 object-cover mb-4 project-img">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">AuditFlow</h3>
                        <p class="text-gray-600 mb-4">Automated audit workflows for compliance, saving 30% on audit time.</p>
                        <p><strong>Tools:</strong> Python, Streamlit, LangChain</p>
                        <p class="text-gray-600 mt-2"><strong>Impact:</strong> Streamlined audits for 20 SMEs.</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/auditflow" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="https://auditflow.streamlit.app" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                    <!-- ChurnGuard -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in project-card" data-category="ai">
                        <img src="https://via.placeholder.com/300x150.png?text=ChurnGuard" alt="ChurnGuard analytics" class="w-full h-40 object-cover mb-4 project-img">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">ChurnGuard</h3>
                        <p class="text-gray-600 mb-4">AI-driven customer retention with churn prediction, boosting retention by 25%.</p>
                        <p><strong>Tools:</strong> TensorFlow, Streamlit</p>
                        <p class="text-gray-600 mt-2"><strong>Impact:</strong> Retained 15% more customers.</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/churnguard" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="https://churnguard.streamlit.app" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Meet Our Innovators Section -->
        <section id="innovators" class="py-20 bg-white" role="region" aria-label="Meet Our Innovators">
            <div class="container mx-auto text-center">
                <h2 class="text-4xl font-bold mb-8 fade-in text-teal-800 color-change-text">Meet Our Innovators</h2>
                <p class="text-lg max-w-2xl mx-auto mb-12 fade-in text-gray-700">Our solutions are powered by top talent like Samuel Mwendwa, a fintech and ESG innovator and mentor at The Founder Institute since 2023.</p>
                <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in max-w-lg mx-auto">
                    <img src="https://via.placeholder.com/150x150.png?text=Samuel+Mwendwa" alt="Samuel Mwendwa profile" class="w-32 h-32 rounded-full mx-auto mb-4">
                    <h3 class="text-2xl font-semibold mb-2 text-teal-800">Samuel Mwendwa</h3>
                    <p class="text-gray-600 mb-4">Lead Developer | AI, Blockchain, ESG Specialist | Founder Institute Mentor (2023–Present)</p>
                    <p class="text-gray-600 mb-4">Samuel drives innovation at Nexlify, building tools like *ESG Scoring Engine* and *CFO AI Agent* that save SMEs millions. As a mentor at <a href="https://fi.co/mentors" target="_blank" class="text-teal-600 hover:underline">The Founder Institute</a> since 2023, he guides startups on competitor benchmarking, financial projections, and technical deep dives, helping over 20 founders secure funding. His expertise in TensorFlow, Solidity, and Qiskit powers our cutting-edge solutions.</p>
                    <div class="flex justify-center space-x-4">
                        <a href="https://github.com/SamTech-crypto" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                        <a href="https://linkedin.com/in/samuel-mwendwa" target="_blank" class="text-teal-600 hover:underline">LinkedIn</a>
                        <a href="/path/to/samuel-resume.pdf" download class="text-teal-600 hover:underline">Download Resume</a>
                        <a href="/path/to/fi-mentorship-case-study.pdf" download class="text-teal-600 hover:underline">Mentorship Case Study</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Expertise Showcase Section -->
        <section id="expertise" class="py-20 bg-gray-100" role="region" aria-label="Expertise Showcase">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800 color-change-text">Expertise Showcase</h2>
                <p class="text-lg text-center max-w-2xl mx-auto mb-8 fade-in text-gray-700">Explore how Samuel Mwendwa’s expertise in competitor benchmarking, financial projections, and technical deep dives drives Nexlify’s solutions.</p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Competitor Benchmarking -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">Competitor Benchmarking</h3>
                        <p class="text-gray-600 mb-4">Our *ESG Scoring Engine* outperforms competitors like Sustainalytics and MSCI by integrating blockchain for transparency, reducing reporting time by 30%.</p>
                        <table class="comparison-table">
                            <thead>
                                <tr>
                                    <th>Feature</th>
                                    <th>ESG Scoring Engine</th>
                                    <th>Sustainalytics</th>
                                    <th>MSCI</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Blockchain Transparency</td>
                                    <td>✅ Yes</td>
                                    <td>❌ No</td>
                                    <td>❌ No</td>
                                </tr>
                                <tr>
                                    <td>Reporting Speed</td>
                                    <td>2 hours</td>
                                    <td>3 hours</td>
                                    <td>4 hours</td>
                                </tr>
                                <tr>
                                    <td>Cost Reduction</td>
                                    <td>70%</td>
                                    <td>50%</td>
                                    <td>40%</td>
                                </tr>
                            </tbody>
                        </table>
                        <a href="#contact" class="mt-4 inline-block text-teal-600 hover:underline">Request a Benchmark Report</a>
                    </div>
                    <!-- Financial Projections -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">Financial Projections</h3>
                        <p class="text-gray-600 mb-4">*CFO AI Agent* delivers 30% more accurate revenue forecasts for SMEs, as shown in this 24-month projection.</p>
                        <div class="chart-container">
                            <canvas id="revenueChart"></canvas>
                        </div>
                        <div class="mt-4 space-x-4">
                            <a href="/path/to/financial-model.pdf" download class="text-teal-600 hover:underline">Download Template</a>
                            <a href="#contact" class="text-teal-600 hover:underline">Request a Demo</a>
                        </div>
                    </div>
                    <!-- Technical Deep Dives -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">Technical Deep Dives</h3>
                        <p class="text-gray-600 mb-4">*InvoFi*’s blockchain architecture uses Solidity smart contracts and Chainlink oracles, optimized by Samuel for 40% lower gas fees.</p>
                        <ul class="text-gray-600 mb-4 list-disc pl-5">
                            <li><strong>Solidity:</strong> Secure invoice financing contracts</li>
                            <li><strong>Chainlink:</strong> Real-time market data integration</li>
                            <li><strong>Ethereum:</strong> Scalable transaction processing</li>
                        </ul>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/invofi" target="_blank" class="text-teal-600 hover:underline">View Code</a>
                            <a href="/path/to/invofi-technical-whitepaper.pdf" download class="text-teal-600 hover:underline">Whitepaper</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Case Studies Section -->
        <section id="case-studies" class="py-20 bg-white" role="region" aria-label="Case Studies">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800 color-change-text">Case Studies</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">InvoFi: Decentralized Financing</h3>
                        <p class="text-gray-600 mb-4">Reduced transaction costs by 60% for a logistics SME using blockchain-based invoice financing.</p>
                        <div class="mt-4 space-x-4">
                            <a href="/path/to/invo-fi-case-study.pdf" target="_blank" class="text-teal-600 hover:underline">Download PDF</a>
                            <a href="#interactive-invofi" class="text-teal-600 hover:underline">View Interactive Chart</a>
                        </div>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">ESG Scoring Engine: Compliance for Startups</h3>
                        <p class="text-gray-600 mb-4">Cut ESG reporting costs by 70% for a green tech startup, attracting $2M in funding.</p>
                        <div class="mt-4 space-x-4">
                            <a href="/path/to/esg-case-study.pdf" target="_blank" class="text-teal-600 hover:underline">Download PDF</a>
                            <a href="#interactive-esg" class="text-teal-600 hover:underline">View Interactive Chart</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Testimonials Section -->
        <section id="testimonials" class="py-20 bg-white" role="region" aria-label="Testimonials">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800 color-change-text">Client Success Stories</h2>
                <div class="testimonial-container">
                    <div class="testimonial-track">
                        <div class="testimonial-card">
                            <p class="text-gray-600 mb-4">"*CFO AI Agent* saved us 20 hours monthly on reporting."</p>
                            <p class="font-semibold text-teal-800">Sarah Lee, FitPulse Gym</p>
                        </div>
                        <div class="testimonial-card">
                            <p class="text-gray-600 mb-4">"*ESG Scoring Engine* secured $1.5M in funding."</p>
                            <p class="font-semibold text-teal-800">Michael Chen, Travel Ventures</p>
                        </div>
                        <div class="testimonial-card">
                            <p class="text-gray-600 mb-4">"*InvoFi* cut our transaction costs by 60%."</p>
                            <p class="font-semibold text-teal-800">Ahmed Khan, TradeFlow</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Blog Section -->
        <section id="blog" class="py-20 bg-gray-100" role="region" aria-label="Blog">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800 color-change-text">Insights & Updates</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">Blockchain’s Impact on Banking</h3>
                        <p class="text-gray-600 mb-4">How <span class="color-change-text">*InvoFi*</span> reshapes finance with DeFi.</p>
                        <a href="https://www.linkedin.com/pulse/blockchains-financial-impact-traditional-banking-new-era-mwendwa-miyif/" target="_blank" class="text-teal-600 hover:underline">Read on LinkedIn</a>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">AI for SME Growth</h3>
                        <p class="text-gray-600 mb-4">How <span class="color-change-text">*CFO AI Agent*</span> boosts efficiency.</p>
                        <a href="/path/to/blog-ai-smes" class="text-teal-600 hover:underline">Read More</a>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">ESG Compliance on a Budget</h3>
                        <p class="text-gray-600 mb-4">How <span class="color-change-text">*ESG Scoring Engine*</span> saves 70%.</p>
                        <a href="/path/to/blog-esg-compliance" class="text-teal-600 hover:underline">Read More</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- FAQ Section -->
        <section id="faq" class="py-20 bg-gray-100" role="region" aria-label="FAQ">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800 color-change-text">Frequently Asked Questions</h2>
                <div class="bg-white p-6 rounded-xl shadow-lg fade-in">
                    <div class="faq-item" onclick="toggleFAQ(this)">
                        <h3 class="text-lg font-semibold text-teal-800 mb-2">What is ESG compliance?</h3>
                        <div class="faq-answer">
                            <p class="text-gray-600 mb-4">ESG compliance ensures sustainable and ethical practices, simplified by our *ESG Scoring Engine*.</p>
                        </div>
                    </div>
                    <div class="faq-item" onclick="toggleFAQ(this)">
                        <h3 class="text-lg font-semibold text-teal-800 mb-2">How does InvoFi work?</h3>
                        <div class="faq-answer">
                            <p class="text-gray-600 mb-4">InvoFi uses blockchain for decentralized financing, reducing costs by 60%.</p>
                        </div>
                    </div>
                    <div class="faq-item" onclick="toggleFAQ(this)">
                        <h3 class="text-lg font-semibold text-teal-800 mb-2">Can I try your tools for free?</h3>
                        <div class="faq-answer">
                            <p class="text-gray-600 mb-4">Yes, we offer free trials for tools like *CFO AI Agent*. Contact us!</p>
                        </div>
                    </div>
                    <div class="faq-item" onclick="toggleFAQ(this)">
                        <h3 class="text-lg font-semibold text-teal-800 mb-2">How does Nexlify perform competitor benchmarking?</h3>
                        <div class="faq-answer">
                            <p class="text-gray-600 mb-4">We use AI to analyze competitor performance, as shown in our <a href="#expertise" class="text-teal-600 hover:underline">*ESG Scoring Engine* benchmark</a>, improving market positioning by 25%.</p>
                        </div>
                    </div>
                    <div class="faq-item" onclick="toggleFAQ(this)">
                        <h3 class="text-lg font-semibold text-teal-800 mb-2">How accurate are your financial projections?</h3>
                        <div class="faq-answer">
                            <p class="text-gray-600 mb-4">Our *CFO AI Agent* delivers 30% more accurate forecasts, as demonstrated in our <a href="#expertise" class="text-teal-600 hover:underline">financial projections showcase</a>.</p>
                        </div>
                    </div>
                    <div class="faq-item" onclick="toggleFAQ(this)">
                        <h3 class="text-lg font-semibold text-teal-800 mb-2">What are technical deep dives at Nexlify?</h3>
                        <div class="faq-answer">
                            <p class="text-gray-600 mb-4">Samuel’s technical expertise drives innovation, like optimizing *InvoFi*’s blockchain for 40% lower costs. See our <a href="#expertise" class="text-teal-600 hover:underline">technical deep dive</a>.</p>
                        </div>
                    </div>
                    <a href="/path/to/faq" class="text-teal-600 hover:underline mt-4 inline-block">View Full FAQ</a>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="gradient-hero text-white py-20" role="region" aria-label="Contact">
            <div class="container mx-auto text-center">
                <h2 class="text-4xl font-bold mb-8 fade-in color-change-text">Unlock Your Potential</h2>
                <p class="text-lg max-w-2xl mx-auto mb-8 fade-in">Discuss consulting, SaaS, or career opportunities with our team.</p>
                <div class="flex justify-center space-x-4 flex-wrap gap-4">
                    <a href="mailto:nexlifysolutions.team@gmail.com" class="inline-block btn-accent font-semibold py-3 px-8 rounded-full transition-colors fade-in">Email Us</a>
                    <a href="https://wa.me/254712238286" target="_blank" class="inline-block bg-teal-600 text-white font-semibold py-3 px-6 rounded-full hover:bg-teal-700 transition-colors fade-in flex items-center">
                        <span class="mr-2">💬</span> WhatsApp
                    </a>
                    <a href="https://www.linkedin.com/in/samuel-mwendwa/" target="_blank" class="inline-block bg-teal-800 text-white font-semibold py-3 px-6 rounded-full hover:bg-teal-900 transition-colors fade-in flex items-center">
                        <span class="mr-2">🔗</span> LinkedIn
                    </a>
                </div>
                <!-- Newsletter Signup -->
                <div class="mt-12">
                    <h3 class="text-2xl font-semibold mb-6 fade-in color-change-text">Subscribe to Our Newsletter</h3>
                    <div class="flex justify-center gap-4 flex-wrap mb-8">
                        <a href="https://www.linkedin.com/newsletters/nexlify-solutions-7280665831749898242/" target="_blank" class="inline-block btn-accent font-semibold py-3 px-8 rounded-full transition-colors fade-in">
                            Subscribe on LinkedIn
                        </a>
                        <form action="https://your-mailchimp-form-url" method="POST" class="flex justify-center gap-2 flex-wrap">
                            <input type="email" name="email" placeholder="Enter your email" class="p-3 rounded-full text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-500" required>
                            <button type="submit" class="inline-block bg-teal-600 text-white font-semibold py-3 px-6 rounded-full hover:bg-teal-700 transition-colors fade-in">
                                Join Email List
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Chatbot Button & Window -->
    <div class="chatbot-btn" onclick="toggleChatbot()" title="Chat with us">
        💬
    </div>
    <div class="chatbot-window" id="chatbot-window">
        <div class="p-4">
            <h3 class="text-lg font-semibold text-teal-800">Welcome to Nexlify!</h3>
            <p class="text-gray-600 mb-2">Ask about our fintech/ESG solutions or Samuel’s expertise.</p>
            <input type="text" id="chatbot-input" placeholder="Type your question..." class="w-full p-2 rounded border mb-2">
            <button onclick="submitChat()" class="btn-accent py-2 px-4 rounded">Send</button>
            <div class="mt-4">
                <p class="text-gray-600 mb-2">Quick Questions:</p>
                <div class="quick-reply-btn" onclick="quickReply('What is ESG compliance?')">What is ESG?</div>
                <div class="quick-reply-btn" onclick="quickReply('How does InvoFi work?')">How does InvoFi work?</div>
                <div class="quick-reply-btn" onclick="quickReply('Tell me about Samuel’s projects')">Samuel’s Projects</div>
                <div class="quick-reply-btn" onclick="quickReply('How does Nexlify perform competitor benchmarking?')">Competitor Benchmarking</div>
                <div class="quick-reply-btn" onclick="quickReply('How accurate are your financial projections?')">Financial Projections</div>
                <div class="quick-reply-btn" onclick="quickReply('What are technical deep dives at Nexlify?')">Technical Deep Dives</div>
            </div>
            <p class="text-gray-600 mt-2">Contact us via <a href="mailto:nexlifysolutions.team@gmail.com" class="text-teal-600">email</a> or <a href="https://wa.me/254712238286" class="text-teal-600">WhatsApp</a>.</p>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-teal-700 text-white py-6" role="contentinfo">
        <div class="container mx-auto text-center">
            <p>© 2025 Nexlify Solutions. All rights reserved.</p>
            <div class="mt-2 space-y-2">
                <p><a href="https://wa.me/254712238286" target="_blank" class="text-emerald-200 hover:underline flex justify-center items-center"><span class="mr-2">💬</span> WhatsApp</a></p>
                <p><a href="https://www.linkedin.com/in/samuel-mwendwa/" target="_blank" class="text-emerald-200 hover:underline flex justify-center items-center"><span class="mr-2">🔗</span> LinkedIn</a></p>
            </div>
        </div>
    </footer>

    <!-- JavaScript -->
    <script>
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Toggle mobile menu
        function toggleMenu() {
            const menu = document.getElementById('nav-menu');
            menu.classList.toggle('hidden');
        }

        // GSAP animations
        document.addEventListener('DOMContentLoaded', () => {
            gsap.registerPlugin(ScrollTrigger);
            document.querySelectorAll('.fade-in').forEach(element => {
                gsap.to(element, {
                    scrollTrigger: {
                        trigger: element,
                        start: 'top 80%',
                        toggleActions: 'play none none none'
                    },
                    opacity: 1,
                    y: 0,
                    duration: 0.6
                });
            });

            // Animate project cards
            document.querySelectorAll('.project-card').forEach(card => {
                gsap.from(card, {
                    scrollTrigger: {
                        trigger: card,
                        start: 'top 85%',
                    },
                    x: -100,
                    opacity: 0,
                    duration: 0.5,
                    ease: 'power2.out'
                });
            });

            // Duplicate testimonial track for seamless looping
            const track = document.querySelector('.testimonial-track');
            track.innerHTML += track.innerHTML;
        });

        // Project filter
        function filterProjects(category) {
            const cards = document.querySelectorAll('.project-card');
            const buttons = document.querySelectorAll('.filter-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            cards.forEach(card => {
                if (category === 'all' || card.dataset.category.includes(category)) {
                    card.style.display = 'block';
                    gsap.to(card, { opacity: 1, y: 0, duration: 0.5 });
                } else {
                    gsap.to(card, { 
                        opacity: 0, 
                        y: 20, 
                        duration: 0.5, 
                        onComplete: () => { card.style.display = 'none'; }
                    });
                }
            });
        }

        // Chatbot functionality
        function toggleChatbot() {
            const chatbotWindow = document.getElementById('chatbot-window');
            chatbotWindow.classList.toggle('active');
        }

        function submitChat() {
            const input = document.getElementById('chatbot-input').value.toLowerCase();
            let response = 'We’ll get back to you soon! Use email or WhatsApp.';
            if (input.includes('esg compliance')) {
                response = 'ESG compliance ensures sustainable practices. Learn more in our <a href="#expertise">Expertise Showcase</a>.';
            } else if (input.includes('invofi work')) {
                response = 'InvoFi uses blockchain for decentralized financing. See our <a href="#expertise">technical deep dive</a>.';
            } else if (input.includes('samuel’s projects')) {
                response = 'Samuel’s projects include *ESG Scoring Engine* and *InvoFi*. Explore them in our <a href="#projects">Solutions</a>.';
            } else if (input.includes('competitor benchmarking')) {
                response = 'We use AI for competitor analysis. Check our <a href="#expertise">benchmarking showcase</a>.';
            } else if (input.includes('financial projections')) {
                response = 'Our *CFO AI Agent* offers accurate forecasts. View our <a href="#expertise">projections demo</a>.';
            } else if (input.includes('technical deep dives')) {
                response = 'Samuel optimizes blockchain solutions like *InvoFi*. See our <a href="#expertise">technical deep dive</a>.';
            }
            alert('Your question: ' + input + '\n' + response);
        }

        function quickReply(question) {
            document.getElementById('chatbot-input').value = question;
            submitChat();
        }

        // FAQ toggle
        function toggleFAQ(element) {
            const answer = element.querySelector('.faq-answer');
            answer.classList.toggle('active');
        }

        // Lazy load images
        document.addEventListener('DOMContentLoaded', () => {
            const images = document.querySelectorAll('img');
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src || img.src;
                        observer.unobserve(img);
                    }
                });
            });
            images.forEach(img => imageObserver.observe(img));
        });

        // Financial projection chart
        document.addEventListener('DOMContentLoaded', () => {
            const ctx = document.getElementById('revenueChart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['Jan 2025', 'Apr 2025', 'Jul 2025', 'Oct 2025', 'Jan 2026', 'Apr 2026'],
                    datasets: [{
                        label: 'Projected Revenue ($)',
                        data: [50000, 75000, 100000, 130000, 170000, 200000],
                        borderColor: '#10b981',
                        backgroundColor: 'rgba(16, 185, 129, 0.2)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Revenue ($)'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Month'
                            }
                        }
                    }
                }
            });
        });

        // Note: For CMS integration, consider Strapi (https://strapi.io) with API endpoints like:
        // GET /api/projects for dynamic project updates
        // POST /api/newsletter for form submissions
        // GET /api/competitor-data for benchmarking (e.g., Crunchbase API)
        // GET /api/financial-data for projections (e.g., QuickBooks API)
        // Example: fetch('https://your-strapi-url/api/projects').then(res => res.json()).then(data => updateProjects(data));
    </script>
</body>
</html>
