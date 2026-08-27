from datetime import datetime
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Metodologias Ativas na Saúde", page_icon="🩺", layout="wide"
)

# Ano atual dinâmico para o rodapé
ano_atual = datetime.now().year

# --- BARRA LATERAL (LOGO E APRESENTAÇÃO) ---
st.sidebar.markdown("---")
st.sidebar.image(
    "https://via.placeholder.com/150",
    caption="Sua Logo Aqui",
    use_container_width=True,
)

st.sidebar.header("Sobre o Site")
st.sidebar.info(
    "Ambiente digital interativo desenvolvido para apoiar a aplicação de "
    "metodologias ativas no ensino superior em saúde, promovendo engajamento, "
    "pensamento crítico e colaboração entre estudantes."
)

st.sidebar.markdown("---")

# --- ESTILIZAÇÃO CSS PROFISSIONAL ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .element-container {
        color: #333333;
    }
    .footer-box {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        padding: 15px;
        border-radius: 8px;
        font-size: 13px;
        color: #555555;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- MENU LATERAL DE NAVEGAÇÃO ---
menu = st.sidebar.selectbox(
    "Navegue pelas Atividades:",
    [
        "Apresentação",
        "1. Perguntas & Respostas (Q&A)",
        "2. Nuvem de Ideias",
        "3. Feedback da Aula",
        "📚 FST1040",
        "📚 FST7001",
        "📚 FST8004",
    ],
)

# --- CONTEÚDO PRINCIPAL ---
if menu == "Apresentação":
    st.header("🩺 Ambiente de Aprendizagem Ativa")
    st.markdown(
        "Ferramenta de apoio pedagógico para metodologias ativas com estudantes"
        " da graduação em saúde."
    )

    st.subheader("Bem-vindos à nossa sala interativa!")
    st.write(
        "Este espaço foi estruturado para dinamizar nossa discussão de hoje,"
        " permitindo a participação ativa, o levantamento de conceitos-chave e a"
        " avaliação contínua do processo de ensino-aprendizagem."
    )

    st.info(
        "💡 **Dica para o Professor:** Utilize o menu lateral para alternar"
        " entre as ferramentas gerais e as seções específicas de cada disciplina durante a sessão."
    )

elif menu == "1. Perguntas & Respostas (Q&A)":
    st.header("💬 Espaço de Perguntas")
    st.write("Envie sua dúvida ou reflexão sobre o caso clínico ou tema discutido.")

    # Formulário Tally.so padrão (Q&A)
    st.components.v1.iframe(
        "https://tally.so/r/A7eGAB",
        height=500,
        scrolling=True,
    )

elif menu == "2. Nuvem de Ideias":
    st.header("☁️ Nuvem de Ideias / Brainstorming")
    st.write(
        "Participe da dinâmica colaborativa respondendo à questão nortear da"
        " aula."
    )

    # Incorporação do AnswerGarden
    answergarden_html = """
    <div style="display: flex; justify-content: center; width: 100%;">
        <iframe src="https://answergarden.ch/embed/5215672" width="640px" height="400px" style="border: none;" scrolling="no" frameborder="0" title="AnswerGarden" allowTransparency="true">
            <p><a href="https://answergarden.ch/5215672">Go to AnswerGarden</a></p>
        </iframe>
    </div>
    """
    st.components.v1.html(answergarden_html, height=430, scrolling=False)

elif menu == "3. Feedback da Aula":
    st.header("📝 Avaliação de Reação (Feedback)")
    st.write(
        "Sua opinião é fundamental para avaliarmos a dinâmica e melhorarmos as"
        " próximas atividades."
    )

    # Formulário Tally.so padrão (Feedback)
    st.components.v1.iframe(
        "https://tally.so/embed/SEU_LINK_DE_FEEDBACK_DO_TALLY?transparentBackground=1",
        height=500,
        scrolling=True,
    )

# --- ESPAÇOS ESPECÍFICOS PARA AS DISCIPLINAS ---
elif menu == "📚 FST1040":
    st.header("🩺 Disciplina: FST1040")
    st.write("Espaço dedicado aos conteúdos, materiais de apoio e interações específicas desta disciplina.")
    
    # Sub-abas internas para organizar a disciplina
    aba_disc1, aba_disc2 = st.tabs(["💬 Perguntas da Turma", "☁️ Nuvem / Dinâmica"])
    
    with aba_disc1:
        st.subheader("Q&A - FST1040")
        st.write("Envie suas dúvidas específicas para esta disciplina:")
        # Aqui você pode colocar um link/iframe do Tally exclusivo para a FST1040 se desejar
        st.components.v1.iframe("https://tally.so/r/A7eGAB", height=400, scrolling=True)
        
    with aba_disc2:
        st.subheader("Brainstorming - FST1040")
        st.write("Palavras-chave e conceitos centrais da aula de FST1040:")
        st.components.v1.html(answergarden_html, height=400, scrolling=False)

elif menu == "📚 FST7001":
    st.header("🩺 Disciplina: FST7001")
    st.write("Espaço dedicado aos conteúdos, materiais de apoio e interações específicas desta disciplina.")
    
    aba_disc1, aba_disc2 = st.tabs(["💬 Perguntas da Turma", "☁️ Nuvem / Dinâmica"])
    
    with aba_disc1:
        st.subheader("Q&A - FST7001")
        st.write("Envie suas dúvidas específicas para esta disciplina:")
        st.components.v1.iframe("https://tally.so/r/A7eGAB", height=400, scrolling=True)
        
    with aba_disc2:
        st.subheader("Brainstorming - FST7001")
        st.write("Palavras-chave e conceitos centrais da aula de FST7001:")
        st.components.v1.html(answergarden_html, height=400, scrolling=False)

elif menu == "📚 FST8004":
    st.header("🩺 Disciplina: FST8004")
    st.write("Espaço dedicado aos conteúdos, materiais de apoio e interações específicas desta disciplina.")
    
    aba_disc1, aba_disc2 = st.tabs(["💬 Perguntas da Turma", "☁️ Nuvem / Dinâmica"])
    
    with aba_disc1:
        st.subheader("Q&A - FST8004")
        st.write("Envie suas dúvidas específicas para esta disciplina:")
        st.components.v1.iframe("https://tally.so/r/A7eGAB", height=400, scrolling=True)
        
    with aba_disc2:
        st.subheader("Brainstorming - FST8004")
        st.write("Palavras-chave e conceitos centrais da aula de FST8004:")
        st.components.v1.html(answergarden_html, height=400, scrolling=False)

# --- RODAPÉ ---
st.markdown("---")

# 1. Copyright e Direitos Autorais
st.markdown(
    f"<p style='text-align: center; color: gray; font-size: 14px;'>© {ano_atual} OLIVEIRA, L.M.V. Todos os direitos reservados.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 13px;'>O conteúdo deste website (textos, imagens e dados) está protegido pela Lei de Direitos Autorais (Lei nº 9.610/1998).</p>",
    unsafe_allow_html=True,
)

# 2. Caixa de citação acadêmica formatada
st.markdown(
    """
<div class='footer-box'>
    <strong>Como citar este site:</strong><br>
    OLIVEIRA, L.M.V. <em>Metodologias Ativas na Saúde</em>. Disponível em: &lt;https://metodologiasativasnasaude.streamlit.app/&gt;. Acesso em: [Data de Acesso].
</div>
""",
    unsafe_allow_html=True,
)

# 3. Assinatura da marca
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 13px;'>Ambiente de Aprendizagem Ativa | Metodologias Ativas na Saúde</p>",
    unsafe_allow_html=True,
)
