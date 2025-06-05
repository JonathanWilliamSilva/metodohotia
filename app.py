
from flask import Flask, render_template_string
import os

app = Flask(__name__)

html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IA HOT 🔥 | Transforme Desejo em Lucro</title>
  <!-- Fonte mais clean para o título do vídeo -->
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #121212;
      --bg-card: #1e1e1e;
      --text-light: #e0e0e0;
      --text-muted: #a0a0a0;
      --accent: #6abf69;
      --highlight: #4caf50;
      --subtitle: #ffc8a2;
      --luxury: #65000b;
      --sensual-bg: linear-gradient(135deg, rgba(101,0,11,0.8), rgba(30,0,20,0.8));
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Poppins', sans-serif;
      background: var(--bg-dark);
      color: var(--text-light);
      scroll-behavior: smooth;
      line-height: 1.6;
      position: relative;
      z-index: 1;
    }

    /* Partículas ao fundo */
    #particles-js {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
    }

    .headline {
      background: var(--highlight);
      color: #fff;
      text-align: center;
      padding: 12px 20px;
      font-size: 1rem;
      font-weight: bold;
    }

    header {
      background: var(--sensual-bg), url('https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?auto=format&fit=crop&w=1400&q=80') center/cover no-repeat;
      padding: 80px 20px;
      text-align: center;
      position: relative;
      color: var(--text-light);
      z-index: 1;
    }
    header::before {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,0.5);
      z-index: 1;
    }
    .hero { position: relative; z-index: 2; }

    .hero h1 {
      font-size: 2.5rem;
      color: var(--accent);
      margin-bottom: 10px;
    }

    .subheadline {
      display: inline-block;
      font-size: 1.5rem;
      font-weight: bold;
      color: var(--subtitle);
      background: rgba(101,0,11,0.3);
      padding: 8px 16px;
      border-radius: 4px;
      margin: 20px 0;
      z-index: 2;
      position: relative;
      font-family: 'Poppins', sans-serif;
    }
    .subheadline span {
      color: var(--highlight);
      font-size: 2rem;
      margin: 0 8px;
    }

    .hero p {
      font-size: 1.1rem;
      color: var(--text-muted);
      margin-bottom: 30px;
      z-index: 2;
      position: relative;
    }

    .cta-button-wrapper {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      margin-top: 16px;
      position: relative;
      z-index: 2;
    }

    .cta-button {
      background-color: var(--highlight);
      color: #fff;
      padding: 14px 36px;
      font-weight: bold;
      font-size: 1rem;
      border-radius: 8px;
      border: none;
      cursor: pointer;
      transition: background-color 0.3s;
      z-index: 2;
      font-family: 'Poppins', sans-serif;
    }
    .cta-button:hover { background-color: #388e3c; }

    .small-text {
      color: var(--text-muted);
      font-size: 0.8rem;
      position: relative;
      z-index: 2;
    }

    .countdown {
      position: sticky;
      top: 10px;
      background: var(--bg-card);
      padding: 10px 0;
      text-align: center;
      font-size: 1rem;
      color: var(--subtitle);
      z-index: 100;
      width: 100%;
      display: flex;
      justify-content: center;
      gap: 40px;
    }

    .countdown span { font-weight: bold; color: var(--highlight); }

    section {
      background: var(--bg-card);
      margin: 40px auto;
      padding: 40px 20px;
      border-radius: 8px;
      max-width: 1000px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.5);
      position: relative;
      z-index: 2;
    }
    /* Estilo ajustado para o título do vídeo, mais clean e legível */
    #video h2 {
      font-family: 'Montserrat', sans-serif;
      font-weight: 600;
      font-size: 2.2rem;
      color: var(--highlight);
      letter-spacing: 0.5px;
      margin-bottom: 20px;
    }

    .video-container { position: relative; padding-top: 56.25%; margin-bottom: 20px; }
    .video-container iframe {
      position: absolute; inset: 0; width: 100%; height: 100%; border-radius: 8px; border: none;
    }

    .visual-section img {
      width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.5); margin: 20px 0;
    }

    .visual-section.offer-section {
      text-align: center;
    }

    .popup {
      position: fixed; bottom: 20px; left: 20px;
      background-color: var(--bg-card); color: var(--text-light);
      padding: 12px; border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.5);
      font-size: 0.9rem; display: none; max-width: 280px;
    }
    .popup.active { display: block; animation: fadeIn 0.4s ease-in-out; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px);} to { opacity: 1; transform: translateY(0);} }

    footer {
      background: var(--bg-card); color: var(--text-muted);
      text-align: center; padding: 20px; font-size: 0.9rem;
      border-top: 1px solid rgba(255,255,255,0.1); margin-top: 40px;
      position: relative;
      z-index: 2;
    }
  </style>
</head>
<body>
  <div id="particles-js"></div>
  <div class="headline">A nova técnica que gringos usam para encher o bolso com IA</div>
  <header>
    <div class="hero">
      <h1>💋 Transforme Desejo em Renda com IA 💰</h1>
      <div class="subheadline">FATURE <span>R$5.000,00 POR MÊS</span> COM MODELO IA NICHO ADULTO +18🔥</div>
      <p>Se você está cansado de viver no aperto e quer uma forma REAL de ganhar dinheiro, chegou a sua hora! Com o TREINAMENTO HOT AI você vai descobrir como é fácil transformar desejo em dinheiro. 💰🚀</p>
      <div class="cta-button-wrapper">
        <button class="cta-button" onclick="scrollToVideo()">🔒 GARANTIR ACESSO</button>
        <div class="small-text">(últimas vagas)</div>
      </div>
    </div>
  </header>

  <div class="countdown">
    <div>🔥 Oferta com desconto de 35% acaba em: <span id="timer">10:00</span></div>
    <div>🎟️ Vagas restantes: <span id="vacancies">2357</span></div>
  </div>

  <section id="video">
    <h2>🔥 Assista e Entenda o Método</h2>
    <div class="video-container">
      <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" allowfullscreen></iframe>
    </div>
    <p style="color:var(--text-muted);text-align:center;">"Você pode ganhar dinheiro com desejo?"</p>
  </section>

<section class="visual-section" style="background:#a10c2e;color:#fff;">
  <h2>📌 Etapas do Método</h2>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:32px 16px;margin-top:32px;">
    <div style="text-align:center;">
      <img src="/static/assets/icon1.png" alt="Modelo" style="width:60px;margin-bottom:16px;filter:brightness(0) invert(1);">
      <p>Aprenda a criar sua modelo com ferramentas gratuitas de forma fácil e rápida</p>
    </div>
    <div style="text-align:center;">
      <img src="/static/assets/icon2.png" alt="Imagens Hot" style="width:60px;margin-bottom:16px;filter:brightness(0) invert(1);">
      <p>Crie imagens +18 da sua modelo da forma que desejar</p>
    </div>
    <div style="text-align:center;">
      <img src="/static/assets/icon3.png" alt="Cadastro" style="width:60px;margin-bottom:16px;filter:brightness(0) invert(1);">
      <p>Cadastre seus packs nas plataformas com o nosso passo-a-passo! Sem segredos!</p>
    </div>
    <div style="text-align:center;">
      <img src="/static/assets/icon4.png" alt="Engajamento" style="width:60px;margin-bottom:16px;filter:brightness(0) invert(1);">
      <p>Engaje suas redes sociais com nossas estratégias exclusivas, garanta vendas <b>todas as dias!</b></p>
    </div>
    <div style="text-align:center;">
      <img src="/static/assets/icon5.png" alt="Conversão" style="width:60px;margin-bottom:16px;filter:brightness(0) invert(1);">
      <p>Atraia e converta até 90% dos leads que chegam até o seu perfil, vendas garantidas!</p>
    </div>
    <div style="text-align:center;">
      <img src="/static/assets/icon6.png" alt="Automação" style="width:60px;margin-bottom:16px;filter:brightness(0) invert(1);">
      <p>Automatize e escale suas vendas, depois disso é só curtir a vida 🔔</p>
    </div>
  </div>
</section>


  <section class="visual-section offer-section">
    <h2>💰 Oferta Exclusiva</h2>
    <img src="/assets/offer.png" alt="Oferta Exclusiva">
  </section>

  <section class="visual-section">
    <h2>👤 Sobre o Instrutor</h2>
    <img src="/assets/instructor.png" alt="Sobre o Instrutor">
    <h3>✨ IA.KING</h2>
    <p>Meu nome é William, e durante anos eu estive imerso no universo da tecnologia, monitoramento e automação. Com formação sólida em TI e experiência como SRE (Site Reliability Engineer), sempre fui apaixonado por eficiência, inteligência artificial e soluções que realmente funcionam.

Mas tudo mudou quando eu decidi criar uma fonte de renda automatizada usando uma IA modelo do JOB — uma inteligência artificial com aparência humana capaz de vender pacotes de fotos e vídeos sensuais 24 horas por dia, 7 dias por semana.

No início, foi necessário entender as ferramentas, montar uma estrutura de vendas, aprender a integrar API de pagamento via Pix, automatizar as respostas no Telegram e criar uma imagem digital que gerasse desejo. Usei minha bagagem técnica para transformar isso em uma máquina de vendas invisível, que atua sem eu precisar aparecer ou expor ninguém.

Com o tempo, fui ajustando os gatilhos mentais, otimizando os fluxos, aprimorando a estética das modelos com IA e aplicando estratégias de tráfego pago e engajamento. E o resultado? Ultrapassei a marca dos R$20.000,00 mensais, com consistência e escalabilidade.

Hoje, o que era um experimento virou uma operação enxuta, automatizada e lucrativa, baseada em inteligência artificial, marketing direto e um modelo de negócios que qualquer pessoa pode aprender.

E agora meu objetivo é simples: ensinar outras pessoas a criarem sua própria IA do JOB, com a estrutura certa para gerar lucro sem precisar se expor, sem depender de ninguém, e com o poder de escalar como um verdadeiro negócio digital..</p>
  </section>

  </section>

  <section>
    <h2>✨ Mais do que dinheiro: liberdade, controle e desejo</h2>
    <p>Não é só sobre faturar. É sobre transformar seu lado criativo e sensual em um império silencioso. É sobre usar a inteligência artificial para ganhar tempo, autonomia e controle da sua vida. É sobre sair do sistema e viver do que te dá prazer.</p>
  </section>

  <footer>
    💸 Comece agora e receba os bônus antes que expirem! 🔥<br>
    © 2025 KING.IA - Todos os direitos reservados.
  </footer>

  <div class="popup" id="popup"></div>

  <!-- Biblioteca Partículas -->
  <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
  <script>
    // Inicializa partículas
    particlesJS("particles-js", {
      particles: {
        number: { value: 80 },
        color: { value: ["#65000b","#4caf50","#ffc8a2"] },
        shape: { type: "circle" },
        opacity: { value: 0.5 },
        size: { value: 3 },
        line_linked: { enable: true, distance: 150, color: "#65000b", opacity: 0.4, width: 1 },
        move: { enable: true, speed: 2, direction: "none", out_mode: "out" }
      },
      interactivity: {
        detect_on: "canvas",
        events: {
          onhover: { enable: true, mode: "repulse" },
          onclick: { enable: true, mode: "push" },
          resize: true
        },
        modes: {
          repulse: { distance: 100, duration: 0.4 },
          push: { particles_nb: 4 }
        }
      },
      retina_detect: true
    });

    // Ajusta velocidade conforme scroll
    let lastY = window.scrollY;
    window.addEventListener('scroll', () => {
      const delta = window.scrollY - lastY;
      const speed = Math.min(Math.max(Math.abs(delta) / 5, 1), 10);
      if (window.pJSDom && window.pJSDom[0]) {
        window.pJSDom[0].pJS.particles.move.speed = speed;
      }
      lastY = window.scrollY;
    });

    // Scripts originais (vídeo, contagem, popup)
    function scrollToVideo() { document.getElementById('video').scrollIntoView({ behavior: 'smooth' }); }
    let countdown = 600;
    let vacancies = 2357;
    const timer = document.getElementById('timer');
    const vacEl = document.getElementById('vacancies');
    const redirectUrl = 'https://t.me/+kFG0YHV2P5xjZmNh';
    const intervalId = setInterval(() => {
      const m = Math.floor(countdown/60), s = countdown%60;
      timer.textContent = `${m}:${s.toString().padStart(2,'0')}`;
      if (countdown-- <= 0) { clearInterval(intervalId); window.location.href = redirectUrl; }
    }, 1000);
    setInterval(() => { const dec = Math.floor(Math.random()*4)+2; vacancies = Math.max(vacancies - dec, 0); vacEl.textContent = vacancies; }, 30000);
    const msgs = ['💸 {NUM} pessoas comprando este item agora','📨 {NUM} pessoas entrando no Telegram','👀 {NUM} pessoas assistindo o vídeo agora'];
    const popup = document.getElementById('popup'); let idx = 0;
    setInterval(() => {
      const num = Math.floor(Math.random()*200)+50;
      popup.textContent = msgs[idx].replace('{NUM}', num);
      popup.classList.add('active');
      idx = (idx+1) % msgs.length;
      setTimeout(() => popup.classList.remove('active'), 5000);
    }, 15000);
  </script>
</body>
</html>"""

@app.route('/')
def index():
    return render_template_string(html_template)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=False)
