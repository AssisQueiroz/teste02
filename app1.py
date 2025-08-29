import streamlit as st
import random
import base64

# -------------------------
# Inicializa variáveis da sessão
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "sentimento" not in st.session_state:
    st.session_state.sentimento = None
if "feedback" not in st.session_state:
    st.session_state.feedback = None

# Configuração da página
st.set_page_config(page_title="Feedback de Sentimento", page_icon="🙂", layout="wide")

# -------------------------
# Estilos responsivos
# -------------------------
st.markdown("""
<style>
/* Botões */
div.stButton > button {
    background-color: #e0f0ff !important;
    color: #2563eb !important;
    font-size: 18px !important;
    font-weight: bold !important;
    height: auto !important;
    padding: 0.8em !important;
    border-radius: 12px !important;
    margin: 0.5em !important;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    min-width: 120px;
}

/* Título principal */
.main-title {
    text-align: center;
    font-size: 28px;
    color: #FF8C00;
    font-weight: bold;
    margin-bottom: 1em;
}

.title-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.5em;
    font-size: 22px;
    text-align: center;
}

.title-heart {
    animation: heartbeat 1s infinite;
    color: #FFD700;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    25%, 75% { transform: scale(1.2); }
    50% { transform: scale(1); }
}

/* Footer */
.footer-container {
    text-align: center;
    margin-top: 3em;
}
.footer-text {
    font-size: 18px;
    font-weight: bold;
    color: #FF8C00;
    margin-bottom: 1em;
}
.footer-logo img {
    max-width: 150px;
    width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
}

/* Mobile: aumenta proporcionalmente */
@media(max-width: 768px) {
    div.stButton > button { font-size: 5vw !important; }
    .main-title { font-size: 6vw; }
    .title-container { font-size: 4.5vw; }
    .footer-text { font-size: 4vw; }
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Funções
# -------------------------
def go_to_feedback(sentimento):
    st.session_state.sentimento = sentimento
    st.session_state.feedback = random.choice(feedbacks.get(sentimento, ["Não há feedback disponível."]))
    st.session_state.page = "feedback"
    st.rerun()

def load_image_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -------------------------
# Feedbacks
# -------------------------
feedbacks = {
    "feliz": ["Sorria, a felicidade é contagiante.", "Hoje é um bom dia para ser feliz.", "A alegria nasce de pequenos momentos."],
    "triste": ["Você é mais forte do que imagina.", "A tristeza é passageira, assim como as nuvens no céu.", "Um passo de cada vez já é progresso."],
    "ansioso": ["Respire fundo, você está seguro agora.", "Um pensamento de cada vez, um passo de cada vez.", "Acalme sua mente, seu coração sabe o caminho."],
    "motivado": ["Levante-se e faça acontecer.", "Cada passo conta para a vitória.", "O esforço de hoje será a conquista de amanhã.", "A ação transforma sonhos em realidade."],
    "calmo": ["Que bom que você está calmo, isso é ótimo para tomar decisões claras.", "Sua calma é inspiradora para quem está ao seu redor.", "Manter a calma ajuda a enfrentar qualquer desafio.", "É admirável ver você tão centrado."],
    "grato": ["A gratidão transforma qualquer dia.", "Valorize o que você tem hoje.", "Ser grato é reconhecer o valor da vida.", "Cada momento merece gratidão."],
    "cansado": ["Você merece descansar, não se culpe por isso.", "O descanso é parte da conquista.", "Pausar é tão importante quanto agir.", "Seu corpo precisa de cuidado e carinho.", "Você já fez muito, reconheça sua entrega."],
    "confuso": ["A confusão é parte do processo de aprender algo novo.", "Está tudo bem não ter todas as respostas agora.", "A clareza vem com o tempo.", "Você não precisa decidir tudo hoje.", "O caminho se mostra passo a passo."],
    "confiante": ["Acredite na sua força interior.", "Você é capaz de grandes conquistas.", "Confiança é a chave para o sucesso.", "Tenha fé em suas decisões."],
    "esperançoso": ["Sempre há um amanhã melhor.", "A esperança é o combustível da vida.", "Acredite em dias melhores.", "Mesmo na dificuldade, a luz vem.", "O futuro guarda boas surpresas."],
    "animado": ["Hoje é um dia cheio de possibilidades!", "Energia positiva atrai coisas boas.", "Sinta a empolgação e siga em frente.", "A vida é mais divertida quando você se anima."],
    "leve": ["Respire fundo e sinta a leveza.", "Deixe a vida fluir com tranquilidade.", "Sinta-se livre para ser você mesmo.", "Solte o que não te faz bem."],
    "realizado": ["Você conquistou algo incrível hoje.", "Sinta orgulho de cada vitória.", "O esforço valeu a pena, parabéns!"],
    "inspirado": ["Acredite no poder que existe dentro de você.", "Todo passo que você dá é um avanço.", "Grandes conquistas começam com pequenos esforços."],
    "estressado": ["Respire fundo: você é maior que o estresse.", "Uma pausa agora pode trazer clareza depois.", "O descanso faz parte da vitória."],
    "sozinho": ["Você nunca está realmente sozinho, sempre há alguém que se importa.", "Sua presença já é valiosa neste mundo.", "Às vezes, a solidão é apenas um pedido da alma por descanso.", "Há pessoas que torcem por você, mesmo em silêncio."]
}

# -------------------------
# Emojis + labels
# -------------------------
opcoes = [
    {"emoji": "😊", "label": "Feliz", "key": "feliz"},
    {"emoji": "😞", "label": "Triste", "key": "triste"},
    {"emoji": "😰", "label": "Ansioso", "key": "ansioso"},
    {"emoji": "💪", "label": "Motivado", "key": "motivado"},
    {"emoji": "😌", "label": "Calmo", "key": "calmo"},
    {"emoji": "🙏", "label": "Grato", "key": "grato"},
    {"emoji": "😴", "label": "Cansado", "key": "cansado"},
    {"emoji": "🤔", "label": "Confuso", "key": "confuso"},
    {"emoji": "😎", "label": "Confiante", "key": "confiante"},
    {"emoji": "🌅", "label": "Esperançoso", "key": "esperançoso"},
    {"emoji": "🤩", "label": "Animado", "key": "animado"},
    {"emoji": "🍃", "label": "Leve", "key": "leve"},
    {"emoji": "🏆", "label": "Realizado", "key": "realizado"},
    {"emoji": "✨", "label": "Inspirado", "key": "inspirado"},
    {"emoji": "😣", "label": "Estressado", "key": "estressado"},
    {"emoji": "🌙", "label": "Sozinho", "key": "sozinho"}
]

# -------------------------
# Página Inicial
# -------------------------
if st.session_state.page == "home":
    st.markdown("""
        <div class="main-title">Setembro Amarelo - Falar é a melhor solução</div>
        <div class="title-container">
            <span class="title-heart">💛</span>
            <span class="title-text" style="color:#FF8C00;">A TGA quer saber: Como você está se sentindo hoje?</span>
        </div>
    """, unsafe_allow_html=True)

    # Determina número de colunas: desktop = 4, mobile = 2
    cols_desktop = 4
    cols_mobile = 2

    # Usando a API estável st.query_params
    screen_width_param = st.query_params.get("screen_width", ["1200"])
    try:
        screen_width = int(screen_width_param[0])
    except:
        screen_width = 1200

    num_cols = cols_mobile if screen_width <= 768 else cols_desktop

    # Organiza botões
    for i in range(0, len(opcoes), num_cols):
        cols = st.columns(num_cols)
        for j, opcao in enumerate(opcoes[i:i+num_cols]):
            if cols[j].button(f"{opcao['emoji']} {opcao['label']}", key=opcao["key"]):
                go_to_feedback(opcao["key"])

    # Frase + logo centralizada
    encoded = load_image_base64("tga.png")
    st.markdown(
        f"""
        <div class="footer-container">
            <div class="footer-text">Cada resposta é única e exclusiva para você</div>
            <div class="footer-logo">
                <img src="data:image/png;base64,{encoded}">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# Página de Feedback
# -------------------------
elif st.session_state.page == "feedback":
    emoji = next(o['emoji'] for o in opcoes if o['key'] == st.session_state.sentimento)
    st.markdown(
        f"<h2 style='text-align: center; font-size: 28px; color: #2563eb;'>Você escolheu: {st.session_state.sentimento.capitalize()} {emoji}</h2>",
        unsafe_allow_html=True
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='font-size:22px; font-weight:600; color:#2563eb; text-align:center; margin-top:25px;'>{st.session_state.feedback}</div>",
        unsafe_allow_html=True
    )
