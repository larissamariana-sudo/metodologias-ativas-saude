from datetime import datetime
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Metodologias Ativas na Saúde", 
    page_icon="🩺", 
    layout="wide"
)

# Ano atual dinâmico para o rodapé
ano_atual = datetime.now().year

# --- BARRA LATERAL (LOGO E APRESENTAÇÃO) ---
st.sidebar.markdown("---")

# Correção de reconhecimento de imagem na barra lateral
# Dica: Certifique-se de que o arquivo 'logo.png' ou 'sala.jpg' está na mesma pasta no GitHub
try:
    st.sidebar.image("sala.png", width=150, use_container_width=True)
except Exception:
    try:
        st.sidebar.image("sala.jpg", width=150, use_container_width=True)
    except Exception:
        st.sidebar.info("📌 **Logo:** Adicione sua imagem na pasta do repositório.")

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

# --- MENU LATERAL DE NAVEGAÇÃO COMPLETO ---
menu = st.sidebar.selectbox(
    "Navegue pelas Atividades:",
    [
        "Apresentação",
        "1. Perguntas & Respostas (Q&A)",
        "2. Nuvem de Ideias",
        "3. Feedback da Aula",
        "📊 Mentimeter",
        "📌 Padlet (Mural)",
        "📝 Typeform",
        "🎮 Kahoot / Quiz",
        "📋 Google Forms",
        "📱 QR Code de Acesso",
        "📚 Disciplina FST1040",
        "📚 Disciplina FST7001",
        "📚 Disciplina FST8004",
    ],
)

# --- CONTEÚDO PRINCIPAL ---

if menu == "Apresentação":
    st.header("🩺 Ambiente de Aprendizagem Ativa")
    st.markdown("Ferramenta de apoio pedagógico para metodologias ativas com estudantes da graduação em saúde.")

    # Exibição segura da imagem principal na apresentação
    try:
        st.image("aaa.jpg", width=600)
    except Exception:
        st.info("💡 *Dica: Envie uma imagem chamada 'aaa.jpg' para o repositório do GitHub para exibi-la aqui.*")

    st.subheader("Bem-vindos à nossa sala interativa!")
    st.write(
        "Este espaço foi estruturado para dinamizar nossa discussão de hoje, "
        "permitindo a participação ativa, o levantamento de conceitos-chave e a "
        "avaliação contínua do processo de ensino-aprendizagem."
    )
    st.info("💡 **Dica para o Professor:** Utilize o menu lateral para alternar entre as ferramentas e disciplinas durante a sessão.")

elif menu == "1. Perguntas & Respostas (Q&A)":
    st.header("💬 Espaço de Perguntas & Respostas por Disciplina")
    st.write("Selecione a disciplina correspondente para enviar ou consultar dúvidas.")
    
    tab_f1, tab_f2, tab_f3 = st.tabs(["FST1040", "FST7001", "FST8004"])
    
    with tab_f1:
        st.subheader("Q&A - FST1040")
        st.components.v1.iframe("https://tally.so/embed/SEU_LINK_FST1040?transparentBackground=1", height=450, scrolling=True)
        
    with tab_f2:
        st.subheader("Q&A - FST7001")
        st.components.v1.iframe("https://tally.so/embed/SEU_LINK_FST7001?transparentBackground=1", height=450, scrolling=True)
        
    with tab_f3:
        st.subheader("Q&A - FST8004")
        st.components.v1.iframe("https://tally.so/embed/SEU_LINK_FST8004?transparentBackground=1", height=450, scrolling=True)

elif menu == "2. Nuvem de Ideias":
    st.header("☁️ Nuvem de Ideias / Brainstorming por Disciplina")
    st.write("Participe da dinâmica colaborativa respondendo à questão nortear da sua turma.")
    
    tab_n1, tab_n2, tab_n3 = st.tabs(["FST1040", "FST7001", "FST8004"])
    
    # Exemplo com o AnswerGarden fornecido (você pode duplicar ou ajustar os IDs se tiver um para cada)
    answergarden_html = """
    <div style="display: flex; justify-content: center; width: 100%;">
        <iframe src="https://answergarden.ch/embed/5215672" width="640px" height="400px" style="border: none;" scrolling="no" frameborder="0" title="AnswerGarden" allowTransparency="true">
            <p><a href="https://answergarden.ch/5215672">Go to AnswerGarden</a></p>
        </iframe>
    </div>
    """
    
    with tab_n1:
        st.subheader("Nuvem de Palavras - FST1040")
        st.components.v1.html(answergarden_html, height=420, scrolling=False)
        
    with tab_n2:
        st.subheader("Nuvem de Palavras - FST7001")
        st.components.v1.html(answergarden_html, height=420, scrolling=False)
        
    with tab_n3:
        st.subheader("Nuvem de Palavras - FST8004")
        st.components.v1.html(answergarden_html, height=420, scrolling=False)

elif menu == "3. Feedback da Aula":
    st.header("📝 Avaliação de Reação (Feedback)")
    st.write("Sua opinião é fundamental para avaliarmos a dinâmica e melhorarmos as próximas atividades.")
    st.components.v1.iframe("https://tally.so/embed/SEU_LINK_DE_FEEDBACK_DO_TALLY?transparentBackground=1", height=500, scrolling=True)

elif menu == "📊 Mentimeter":
    st.header("📊 Dinâmica Interativa - Mentimeter")
    st.write("Participe das enquetes e perguntas em tempo real.")
    # Insira o link de embed do seu Mentimeter
    st.components.v1.iframe("https://www.mentimeter.com/embed/SEU_CODIGO_MENTIMETER", height=550, scrolling=True)

elif menu == "📌 Padlet (Mural)":
    st.header("📌 Mural Colaborativo - Padlet")
    st.write("Compartilhe post-its, ideias e analise os materiais fixados no mural.")
    # Insira o link de embed do seu Padlet
    st.components.v1.html('<iframe src="https://padlet.com/embed/SEU_ID_PADLET" width="100%" height="550px" style="border:none; border-radius:8px;"></iframe>', height=570, scrolling=True)

elif menu == "📝 Typeform":
    st.header("📝 Formulário Dinâmico - Typeform")
    st.write("Responda à avaliação ou atividade proposta.")
    # Insira o link do seu Typeform
    st.components.v1.iframe("https://form.typeform.com/to/SEU_ID_TYPEFORM", height=550, scrolling=True)

elif menu == "🎮 Kahoot / Quiz":
    st.header("🎮 Quiz Interativo - Kahoot")
    st.write("Preparem-se para o desafio gamificado!")
    st.info("👉 Acesse o link abaixo ou insira o PIN fornecido pelo professor no projetor.")
    st.markdown("[Acessar Kahoot! (kahoot.it)](https://kahoot.it)", unsafe_allow_html=True)
    # Opcional: incorporação de iframe se houver visualização web direta
    st.components.v1.iframe("https://kahoot.it/", height=600, scrolling=True)

elif menu == "📋 Google Forms":
    st.header("📋 Avaliação / Coleta - Google Forms")
    st.write("Preencha o formulário institucional abaixo:")
    # Insira o link de incorporação do Google Forms
    st.components.v1.iframe("https://docs.google.com/forms/d/e/SEU_LINK_GOOGLE_FORMS/viewform?embedded=true", height=600, scrolling=True)

elif menu == "📱 QR Code de Acesso":
    st.header("📱 QR Code para Acesso Rápido via Celular")
    st.write("Aponte a câmera do seu smartphone para acessar o site ou a atividade atual instantaneamente.")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Substitua 'qrcode.png' pelo arquivo de imagem do seu QR code enviado ao GitHub
        try:
            st.image("qrcode.png", width=350, caption="Escaneie para acessar o portal")
        except Exception:
            st.warning("⚠️ Coloque uma imagem chamada `qrcode.png` na pasta do seu repositório GitHub para exibi-la aqui.")

elif menu == "📚 Disciplina FST1040":
    st.header("📚 Disciplina: FST1040")
    st.write("Painel centralizado com todas as atividades e interações específicas da disciplina FST1040.")
    st.info("Utilize as abas superiores para navegar entre os recursos desta disciplina.")
    
    t1, t2, t3 = st.tabs(["💬 Perguntas", "☁️ Nuvem de Ideias", "📋 Atividade Prática"])
    with t1:
        st.components.v1.iframe("https://tally.so/embed/SEU_LINK_FST1040?transparentBackground=1", height=400, scrolling=True)
    with t2:
        st.components.v1.html(answergarden_html, height=400, scrolling=False)
    with t3:
        st.write("Espaço reservado para materiais ou formulários complementares da FST1040.")

elif menu == "📚 Disciplina FST7001":
    st.header("📚 Disciplina: FST7001")
    st.write("Painel centralizado com todas as atividades e interações específicas da disciplina FST7001.")
    
    t1, t2, t3 = st.tabs(["💬 Perguntas", "☁️ Nuvem de Ideias", "📋 Atividade Prática"])
    with t1:
        st.components.v1.iframe("https://tally.so/embed/SEU_LINK_FST7001?transparentBackground=1", height=400, scrolling=True)
    with t2:
        st.components.v1.html(answergarden_html, height=400, scrolling=False)
    with t3:
        st.write("Espaço reservado para materiais ou formulários complementares da FST7001.")

elif menu == "📚 Disciplina FST8004":
    st.header("📚 Disciplina: FST8004")
    st.write("Painel centralizado com todas as atividades e interações específicas da disciplina FST8004.")
    
    t1, t2, t3 = st.tabs(["💬 Perguntas", "☁️ Nuvem de Ideias", "📋 Atividade Prática"])
    with t1:
        st.components.v1.iframe("https://tally.so/embed/SEU_LINK_FST8004?transparentBackground=1", height=400, scrolling=True)
    with t2:
        st.components.v1.html(answergarden_html, height=400, scrolling=False)
    with t3:
        st.write("Espaço reservado para materiais ou formulários complementares da FST8004.")

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
