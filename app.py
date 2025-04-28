<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Nexlify Solutions: Fintech & ESG Solutions for SMEs, Powered by AI and Blockchain. Automate financial modeling, optimize ESG compliance, and leverage DeFi for growth.">
    <meta name="keywords" content="fintech for SMEs, ESG compliance, DeFi financing, AI analytics, financial strategist, startup growth">
    <meta name="author" content="Nexlify Solutions">
    <title>Nexlify Solutions - Fintech & ESG Specialist for SMEs</title>
    <link rel="icon" type="image/x-icon" href="data:image/x-icon;base64,AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAKCgoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .gradient-hero {
            background: linear-gradient(135deg, #0f766e, #10b981, #047857, #0f766e);
            background-size: 200% 200%;
            animation: gradientFlow 10s ease infinite;
        }
        @keyframes gradientFlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
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
            padding: 12px;
            border-radius: 50%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            z-index: 1000;
            transition: transform 0.3s ease, background-color 0.3s ease;
        }
        .chatbot-btn:hover {
            transform: scale(1.1) rotate(10deg);
            background-color: #10b981;
        }
        .chatbot-btn[aria-expanded="true"] {
            background-color: #f59e0b;
        }
        .chatbot-window {
            position: fixed;
            bottom: 80px;
            right: 20px;
            width: 320px;
            max-height: 400px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            display: none;
            z-index: 1000;
            border: 1px solid #10b981;
            animation: slideIn 0.3s ease forwards;
        }
        .chatbot-window.active {
            display: block;
        }
        @keyframes slideIn {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        .chatbot-messages p {
            margin-bottom: 8px;
            padding: 8px;
            border-radius: 8px;
        }
        .chatbot-messages p.bot {
            background: #e6fffa;
            text-align: left;
        }
        .chatbot-messages p.user {
            background: #10b981;
            color: white;
            text-align: right;
        }
        nav, footer {
            background-color: #0f766e;
        }
        .btn-accent {
            background-color: #f59e0b;
            color: white;
        }
        .btn-accent:hover {
            background-color: #d97706;
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
        <!-- Home Section -->
        <section id="home" class="gradient-hero text-white py-24" role="region" aria-label="Home">
            <div class="container mx-auto text-center">
                <h2 class="text-5xl font-extrabold mb-6 fade-in">Fintech & ESG Solutions for SMEs</h2>
                <p class="text-xl max-w-3xl mx-auto mb-8 fade-in">Nexlify Solutions delivers AI-driven fintech and ESG tools, cutting costs by up to 60% and boosting SME growth with blockchain and quantum tech.</p>
                <div class="flex justify-center space-x-4 flex-wrap gap-4">
                    <a href="#contact" class="inline-block btn-accent font-semibold py-3 px-8 rounded-full transition-colors fade-in">Book a Free Consultation</a>
                    <a href="#projects" class="inline-block bg-teal-600 text-white font-semibold py-3 px-8 rounded-full hover:bg-teal-700 transition-colors fade-in">Explore Solutions</a>
                </div>
            </div>
        </section>

        <!-- Why ESG & DeFi Section -->
        <section id="why-esg-defi" class="py-20 bg-gray-100" role="region" aria-label="Why ESG & DeFi">
            <div class="container mx-auto text-center">
                <h2 class="text-4xl font-bold mb-8 fade-in text-teal-800">Why ESG & DeFi Matter</h2>
                <p class="text-lg max-w-3xl mx-auto mb-8 fade-in text-gray-700">ESG compliance attracts investors and ensures sustainability, while DeFi unlocks low-cost financing. Our AI-driven tools simplify both for SMEs.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">ESG Benefits</h3>
                        <p class="text-gray-600 mb-4">Align with investor demands and cut reporting costs by 70% with *ESG Radar*.</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">DeFi Advantages</h3>
                        <p class="text-gray-600 mb-4">Access low-cost loans via blockchain with *InvoFi*, saving 60% on transactions.</p>
                    </div>
                </div>
                <a href="#contact" class="mt-6 inline-block btn-accent text-white py-3 px-8 rounded-full transition-colors fade-in">Learn How We Help</a>
            </div>
        </section>

        <!-- Case Studies Section -->
        <section id="case-studies" class="py-20 bg-white" role="region" aria-label="Case Studies">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800">Case Studies</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">InvoFi: Decentralized Financing</h3>
                        <p class="text-gray-600 mb-4">Reduced transaction costs by 60% for a logistics SME using blockchain-based invoice financing.</p>
                        <div class="mt-4 space-x-4">
                            <a href="path/to/invo-fi-case-study.pdf" target="_blank" class="text-teal-600 hover:underline">Download PDF</a>
                            <a href="#interactive-invofi" class="text-teal-600 hover:underline">View Interactive Chart</a>
                        </div>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">ESG Radar: Compliance for Startups</h3>
                        <p class="text-gray-600 mb-4">Cut ESG reporting costs by 70% for a green tech startup, attracting $2M in funding.</p>
                        <div class="mt-4 space-x-4">
                            <a href="path/to/esg-radar-case-study.pdf" target="_blank" class="text-teal-600 hover:underline">Download PDF</a>
                            <a href="#interactive-esg" class="text-teal-600 hover:underline">View Interactive Chart</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Projects Section -->
        <section id="projects" class="py-20 bg-gray-100" role="region" aria-label="Projects">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800">Our Solutions</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <!-- Fintech Tools -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">Fintech Tools</h3>
                        <p class="text-gray-600 mb-4">Track KPIs with *FinDash* and automate models with *AutoModeler*, saving 50% on reporting time.</p>
                        <p><strong>Tools:</strong> Tableau, SQL, Python, Streamlit</p>
                        <p class="text-gray-600 mt-2">Mockup: FinDash dashboard with KPI cards, line/pie charts, and real-time updates.</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/findash" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="https://samtech-crypto-automodeler.streamlit.app" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                    <!-- ESG Solutions -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">ESG Solutions</h3>
                        <p class="text-gray-600 mb-4">Simplify compliance with *ESG Radar* and *Automated ESG Suite*, cutting costs by 70%.</p>
                        <p><strong>Tools:</strong> Python, BI Tools, Streamlit</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/esg-radar" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="path/to/esg-demo" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                    <!-- DeFi & Blockchain -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">DeFi & Blockchain</h3>
                        <p class="text-gray-600 mb-4">Streamline financing with *InvoFi*, reducing transaction costs by 60%.</p>
                        <p><strong>Tools:</strong> Ethereum, Solidity, Chainlink, Streamlit</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/InvoFi" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="https://invofi.streamlit.app/" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                    <!-- AI & Risk Management -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">AI & Risk Management</h3>
                        <p class="text-gray-600 mb-4">Boost retention by 30% with *Customer Retention Engine* and *Predictive Risk Modeling*.</p>
                        <p><strong>Tools:</strong> TensorFlow, scikit-learn, Streamlit</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/CustomerChurnPredictor" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="https://predictive-risk-app.streamlit.app" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                    <!-- Quantum Optimization -->
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">Quantum Optimization</h3>
                        <p class="text-gray-600 mb-4">Reduce portfolio risk by 40% with *Quantum Financial Optimizer*.</p>
                        <p><strong>Tools:</strong> Qiskit, Python, AWS Braket</p>
                        <div class="mt-4 space-x-4">
                            <a href="https://github.com/SamTech-crypto/quantum-financial-optimizer" target="_blank" class="text-teal-600 hover:underline">GitHub</a>
                            <a href="path/to/quantum-demo" target="_blank" class="text-teal-600 hover:underline">Live Demo</a>
                        </div>
                    </div>
                </div>
            </section>

        <!-- Solutions Section -->
        <section id="solutions" class="py-20 bg-gray-100" role="region" aria-label="Solutions">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800">Solve Your Challenges</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">Inefficient Financial Modeling</h3>
                        <p class="text-gray-600 mb-4">Automate with *AutoModeler* for 50% faster models. Onboard in 1 week.</p>
                        <a href="#contact" class="text-teal-600 hover:underline">Start Free Trial</a>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">ESG Compliance</h3>
                        <p class="text-gray-600 mb-4">Simplify reporting with *ESG Radar*. Cut costs by 70%. Ready in 1 week.</p>
                        <a href="#contact" class="text-teal-600 hover:underline">Start Free Trial</a>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">DeFi Navigation</h3>
                        <p class="text-gray-600 mb-4">Gain clarity with *DeFi Analytics Suite*. Deploy in 1 week.</p>
                        <a href="#contact" class="text-teal-600 hover:underline">Start Free Trial</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Testimonials Section -->
        <section id="testimonials" class="py-20 bg-white" role="region" aria-label="Testimonials">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800">Client Success Stories</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div class="bg-white p-6 rounded-xl shadow-lg fade-in">
                        <p class="text-gray-600 mb-4">"*FinDash* streamlined our financial tracking, saving us 20 hours monthly."</p>
                        <p class="font-semibold text-teal-800">Sarah Lee, Owner of FitPulse Gym</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg fade-in">
                        <p class="text-gray-600 mb-4">"*ESG Radar* helped us secure $1.5M by showcasing our sustainability efforts."</p>
                        <p class="font-semibold text-teal-800">Michael Chen, CEO of TravelTech Ventures</p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg fade-in">
                        <p class="text-gray-600 mb-4">"*InvoFi* cut our transaction costs by 60%."</p>
                        <p class="font-semibold text-teal-800">Ahmed Khan, CEO of TradeFlow</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Blog Section -->
        <section id="blog" class="py-20 bg-gray-100" role="region" aria-label="Blog">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800">Insights & Updates</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">Blockchain's Financial Impact on Traditional Banking</h3>
                        <p class="text-gray-600 mb-4">Explore how blockchain is reshaping banking with decentralized finance solutions like *InvoFi*.</p>
                        <a href="https://www.linkedin.com/pulse/blockchains-financial-impact-traditional-banking-new-era-mwendwa-miyif/?trackingId=kLo%2Bi4p%2BQ8iJoMgLmMUMNA%3D%3D" target="_blank" class="text-teal-600 hover:underline">Read on LinkedIn</a>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">How Fintech Dashboards Save SMEs Time</h3>
                        <p class="text-gray-600 mb-4">Learn how *FinDash* cuts reporting time by 50% with real-time KPI tracking.</p>
                        <a href="path/to/blog-fintech-dashboards" class="text-teal-600 hover:underline">Read More</a>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg animate-card fade-in">
                        <h3 class="text-2xl font-semibold mb-3 text-teal-800">ESG Compliance on a Budget</h3>
                        <p class="text-gray-600 mb-4">Discover how *ESG Radar* reduces costs by 70% for SMEs.</p>
                        <a href="path/to/blog-esg-compliance" class="text-teal-600 hover:underline">Read More</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- FAQ Section -->
        <section id="faq" class="py-20 bg-gray-100" role="region" aria-label="FAQ">
            <div class="container mx-auto">
                <h2 class="text-4xl font-bold text-center mb-16 fade-in text-teal-800">Frequently Asked Questions</h2>
                <div class="bg-white p-6 rounded-xl shadow-lg fade-in">
                    <p class="text-gray-600 mb-4">Find answers to common questions about our fintech and ESG solutions.</p>
                    <a href="path/to/faq" class="text-teal-600 hover:underline">View Full FAQ</a>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="gradient-hero text-white py-20" role="region" aria-label="Contact">
            <div class="container mx-auto text-center">
                <h2 class="text-4xl font-bold mb-8 fade-in">Unlock Your Potential</h2>
                <p class="text-lg max-w-2xl mx-auto mb-8 fade-in">Discuss consulting, SaaS, or partnerships to drive growth.</p>
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
                    <h3 class="text-2xl font-semibold mb-6 fade-in">Subscribe to Our Newsletter</h3>
                    <div class="flex justify-center gap-4 flex-wrap mb-8">
                        <a href="https://www.linkedin.com/newsletters/nexlify-solutions-7280665831749898242/" target="_blank" class="inline-block btn-accent font-semibold py-3 px-8 rounded-full transition-colors fade-in">
                            Subscribe on LinkedIn
                        </a>
                        <form action="your-email-service-signup-url" method="POST" class="flex justify-center gap-2 flex-wrap">
                            <input type="email" name="email" placeholder="Enter your email" class="p-3 rounded-full text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-500" required>
                            <button type="submit" class="inline-block bg-teal-600 text-white font-semibold py-3 px-6 rounded-full hover:bg-teal-700 transition-colors fade-in">
                                Join Email List
                            </button>
                        </form>
                    </div>
                    <p class="text-sm mb-6 fade-in">Get exclusive fintech tips via email!</p>

                    <!-- Solve Your Challenges Subsection -->
                    <div class="mt-12">
                        <h4 class="text-xl font-semibold mb-6 fade-in">Solve Your Challenges</h4>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                            <div class="bg-white p-4 rounded-xl shadow-lg fade-in">
                                <h5 class="text-lg font-semibold mb-2 text-teal-800">Inefficient Financial Modeling</h5>
                                <p class="text-gray-600 mb-2">Automate with *AutoModeler* for 50% faster models.</p>
                                <a href="#solutions" class="text-teal-600 hover:underline">Learn More</a>
                            </div>
                            <div class="bg-white p-4 rounded-xl shadow-lg fade-in">
                                <h5 class="text-lg font-semibold mb-2 text-teal-800">ESG Compliance</h5>
                                <p class="text-gray-600 mb-2">Simplify reporting with *ESG Radar*. Cut costs by 70%.</p>
                                <a href="#solutions" class="text-teal-600 hover:underline">Learn More</a>
                            </div>
                            <div class="bg-white p-4 rounded-xl shadow-lg fade-in">
                                <h5 class="text-lg font-semibold mb-2 text-teal-800">DeFi Navigation</h5>
                                <p class="text-gray-600 mb-2">Gain clarity with *DeFi Analytics Suite*.</p>
                                <a href="#solutions" class="text-teal-600 hover:underline">Learn More</a>
                            </div>
                        </div>
                    </div>

                    <!-- Client Success Stories Subsection -->
                    <div class="mt-12">
                        <h4 class="text-xl font-semibold mb-6 fade-in">Client Success Stories</h4>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                            <div class="bg-white p-4 rounded-xl shadow-lg fade-in">
                                <p class="text-gray-600 mb-2">"*FinDash* streamlined our financial tracking, saving us 20 hours monthly."</p>
                                <p class="font-semibold text-teal-800">Sarah Lee, FitPulse Gym</p>
                            </div>
                            <div class="bg-white p-4 rounded-xl shadow-lg fade-in">
                                <p class="text-gray-600 mb-2">"*AutoModeler* reduced our forecasting time by 40%."</p>
                                <p class="font-semibold text-teal-800">Emma Brown, RetailEasy SME</p>
                            </div>
                            <div class="bg-white p-4 rounded-xl shadow-lg fade-in">
                                <p class="text-gray-600 mb-2">"*ESG Radar* helped us attract $500K in green funding."</p>
                                <p class="font-semibold text-teal-800">Liam Carter, GreenEnergy Co.</p>
                            </div>
                        </div>
                        <a href="#testimonials" class="inline-block mt-6 text-teal-200 hover:underline fade-in">See More Success Stories</a>
                    </div>

                    <!-- Great Other Solutions Subsection -->
                    <div class="mt-12">
                        <h4 class="text-xl font-semibold mb-6 fade-in">Great Other Solutions</h4>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="bg-white p-4 rounded-xl shadow-lg fade-in">
                                <h5 class="text-lg font-semibold mb-2 text-teal-800">Data-Driven Decision Making</h5>
                                <p class="text-gray-600 mb-2">Leverage AI to analyze financial and ESG data for actionable insights.</p>
                                <p class="text-gray-600 mb-2"><strong>Tools:</strong> Python, TensorFlow, Power BI</p>
                                <a href="#projects" class="text-teal-600 hover:underline">Learn More</a>
                            </div>
                            <div class="bg-white p-4 rounded-xl shadow-lg fade-in">
                                <h5 class="text-lg font-semibold mb-2 text-teal-800">Blockchain Supply Chain Financing</h5>
                                <p class="text-gray-600 mb-2">Streamline supply chain financing, reducing costs by 50% with blockchain.</p>
                                <p class="text-gray-600 mb-2"><strong>Tools:</strong> Hyperledger, Solidity, Streamlit</p>
                                <a href="#projects" class="text-teal-600 hover:underline">Learn More</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Chatbot Button & Window -->
    <button class="chatbot-btn" onclick="toggleChatbot()" aria-label="Open chatbot" aria-expanded="false" title="Chat with us">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path>
        </svg>
    </button>
    <div class="chatbot-window" id="chatbot-window" role="dialog" aria-label="Chatbot">
        <div class="p-4 flex flex-col h-96">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-lg font-semibold text-teal-800">Nexlify Assistant</h3>
                <button onclick="toggleChatbot()" class="text-gray-600 hover:text-teal-800" aria-label="Close chatbot">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                    </svg>
                </button>
            </div>
            <div class="flex-1 overflow-y-auto mb-4 p-2 bg-gray-50 rounded-lg" id="chatbot-messages">
                <p class="text-gray-600">Hi! Ask about our fintech or ESG solutions.</p>
            </div>
            <div class="flex flex-col gap-2">
                <div class="flex gap-2">
                    <input type="text" id="chatbot-input" placeholder="Type your question..." class="flex-1 p-2 rounded border focus:outline-none focus:ring-2 focus:ring-teal-500" aria-label="Chatbot input">
                    <button onclick="submitChat()" class="btn-accent py-2 px-4 rounded" aria-label="Send message">Send</button>
                </div>
                <div class="flex flex-wrap gap-2">
                    <button onclick="quickReply('What is ESG Radar?')" class="text-sm text-teal-600 hover:underline">What is ESG Radar?</button>
                    <button onclick="quickReply('How does InvoFi work?')" class="text-sm text-teal-600 hover:underline">How does InvoFi work?</button>
                    <button onclick="quickReply('Can I get a demo?')" class="text-sm text-teal-600 hover:underline">Can I get a demo?</button>
                </div>
            </div>
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
        });

        // Chatbot functionality
        function toggleChatbot() {
            const chatbotWindow = document.getElementById('chatbot-window');
            const chatbotBtn = document.querySelector('.chatbot-btn');
            const isActive = chatbotWindow.classList.toggle('active');
            chatbotBtn.setAttribute('aria-expanded', isActive);
            if (isActive) {
                document.getElementById('chatbot-input').focus();
            }
        }

        function submitChat() {
            const input = document.getElementById('chatbot-input');
            const messages = document.getElementById('chatbot-messages');
            const message = input.value.trim();
            if (!message) return;

            const userMsg = document.createElement('p');
            userMsg.className = 'user';
            userMsg.textContent = message;
            messages.appendChild(userMsg);

            setTimeout(() => {
                const botMsg = document.createElement('p');
                botMsg.className = 'bot';
                botMsg.textContent = getBotResponse(message);
                messages.appendChild(botMsg);
                messages.scrollTop = messages.scrollHeight;
            }, 500);

            input.value = '';
            messages.scrollTop = messages.scrollHeight;
        }

        function quickReply(message) {
            document.getElementById('chatbot-input').value = message;
            submitChat();
        }

        function getBotResponse(message) {
            message = message.toLowerCase();
            if (message.includes('esg radar')) {
                return 'ESG Radar simplifies compliance, cutting reporting costs by 70%. Want to learn more?';
            } else if (message.includes('invofi')) {
                return 'InvoFi uses blockchain for low-cost invoice financing, saving 60% on transactions. Interested in a demo?';
            } else if (message.includes('demo')) {
                return 'We can schedule a free demo! Contact us via email (nexlifysolutions.team@gmail.com) or WhatsApp.';
            } else {
                return 'Thanks for your question! For detailed answers, contact us via email or WhatsApp.';
            }
        }

        document.getElementById('chatbot-input').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') submitChat();
        });
    </script>
</body>
</html>
