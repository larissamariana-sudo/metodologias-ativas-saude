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

# --- BARRA LATERAL (LOGO NO TOPO E APRESENTAÇÃO) ---
st.sidebar.markdown("---")

# 1. Logo principal no topo da barra lateral (aaa.jpg)
try:
    st.sidebar.image("aaa.jpg", width=150, use_container_width=True)
except Exception:
    try:
        st.sidebar.image("sala.jpg", width=150, use_container_width=True)
    except Exception:
        st.sidebar.info("📌 **Logo:** Adicione a imagem 'aaa.jpg' na pasta do repositório.")

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

# --- MENU LATERAL DE NAVEGAÇÃO NUMERADO (FEEDBACK NO FINAL) ---
menu = st.sidebar.selectbox(
    "Navegue pelas Atividades:",
    [
        "Apresentação",
        "1. Perguntas & Respostas (Q&A)",
        "2. Nuvem de Ideias",
        "3. Mentimeter",
        "4. Mural Colaborativo (Padlet)",
        "5. Typeform",
        "6. Quiz (Kahoot)",
        "7. Google Forms",
        "8. QR Code de Acesso",
        "9. Feedback da Aula",
    ],
)

# --- CONTEÚDO PRINCIPAL ---

if menu == "Apresentação":
    st.header("🩺 Ambiente de Aprendizagem Ativa")
    st.markdown("Ferramenta de apoio pedagógico para metodologias ativas com estudantes da graduação em saúde.")

    # Exibição da imagem principal na apresentação
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
    
    # Códigos AnswerGarden específicos para cada disciplina (você pode alterar os IDs conforme necessário)
    answergarden_html_1 = """
    <div style="display: flex; justify-content: center; width: 100%;">
        <iframe src="https://answergarden.ch/embed/5215714" width="640px" height="400px" style="border: none;" scrolling="no" frameborder="0" title="AnswerGarden" allowTransparency="true"><p><a href="https://answergarden.ch/5215714">Go to AnswerGarden</a></p></iframe>
                    <p><a href="https://answergarden.ch/5215672">Go to AnswerGarden</a></p>
        </iframe>
    </div>
    """
    
    answergarden_html_2 = """
    <div style="display: flex; justify-content: center; width: 100%;">
        <iframe src="https://answergarden.ch/embed/5215672" width="640px" height="400px" style="border: none;" scrolling="no" frameborder="0" title="AnswerGarden FST7001" allowTransparency="true">
            <p><a href="https://answergarden.ch/5215672">Go to AnswerGarden</a></p>
        </iframe>
    </div>
    """
    
    answergarden_html_3 = """
    <div style="display: flex; justify-content: center; width: 100%;">
        <iframe src="https://answergarden.ch/embed/5215672" width="640px" height="400px" style="border: none;" scrolling="no" frameborder="0" title="AnswerGarden FST8004" allowTransparency="true">
            <p><a href="https://answergarden.ch/5215672">Go to AnswerGarden</a></p>
        </iframe>
    </div>
    """

    with tab_n1:
        st.subheader("Nuvem de Palavras - FST1040")
        st.components.v1.html(answergarden_html_1, height=420, scrolling=False)
    with tab_n2:
        st.subheader("Nuvem de Palavras - FST7001")
        st.components.v1.html(answergarden_html_2, height=420, scrolling=False)
    with tab_n3:
        st.subheader("Nuvem de Palavras - FST8004")
        st.components.v1.html(answergarden_html_3, height=420, scrolling=False)

elif menu == "3. Mentimeter":
    st.header("📊 Dinâmica Interativa - Mentimeter por Disciplina")
    st.write("Participe das enquetes e perguntas em tempo real.")
    
    tab_m1, tab_m2, tab_m3 = st.tabs(["FST1040", "FST7001", "FST8004"])
    with tab_m1:
        st.subheader("Mentimeter - FST1040")
        st.components.v1.iframe("https://www.mentimeter.com/embed/SEU_CODIGO_MENTIMETER_1", height=450, scrolling=True)
    with tab_m2:
        st.subheader("Mentimeter - FST7001")
        st.components.v1.iframe("https://www.mentimeter.com/embed/SEU_CODIGO_MENTIMETER_2", height=450, scrolling=True)
    with tab_m3:
        st.subheader("Mentimeter - FST8004")
        st.components.v1.iframe("https://www.mentimeter.com/embed/SEU_CODIGO_MENTIMETER_3", height=450, scrolling=True)

elif menu == "4. Mural Colaborativo (Padlet)":
    st.header("📌 Mural Colaborativo - Padlet por Disciplina")
    st.write("Compartilhe post-its, ideias e analise os materiais fixados no mural.")
    
    tab_p1, tab_p2, tab_p3 = st.tabs(["FST1040", "FST7001", "FST8004"])
    with tab_p1:
        st.subheader("Mural Padlet - FST1040")
        st.components.v1.html('<iframe src="https://padlet.com/embed/SEU_ID_PADLET_1" width="100%" height="450px" style="border:none; border-radius:8px;"></iframe>', height=470, scrolling=True)
    with tab_p2:
        st.subheader("Mural Padlet - FST7001")
        st.components.v1.html('<iframe src="https://padlet.com/embed/SEU_ID_PADLET_2" width="100%" height="450px" style="border:none; border-radius:8px;"></iframe>', height=470, scrolling=True)
    with tab_p3:
        st.subheader("Mural Padlet - FST8004")
        st.components.v1.html('<iframe src="https://padlet.com/embed/SEU_ID_PADLET_3" width="100%" height="450px" style="border:none; border-radius:8px;"></iframe>', height=470, scrolling=True)

elif menu == "5. Typeform":
    st.header("📝 Formulário Dinâmico - Typeform por Disciplina")
    st.write("Responda à avaliação ou atividade proposta.")
    
    tab_t1, tab_t2, tab_t3 = st.tabs(["FST1040", "FST7001", "FST8004"])
    with tab_t1:
        st.subheader("Typeform - FST1040")
        st.components.v1.iframe("https://form.typeform.com/to/SEU_ID_TYPEFORM_1", height=450, scrolling=True)
    with tab_t2:
        st.subheader("Typeform - FST7001")
        st.components.v1.iframe("https://form.typeform.com/to/SEU_ID_TYPEFORM_2", height=450, scrolling=True)
    with tab_t3:
        st.subheader("Typeform - FST8004")
        st.components.v1.iframe("https://form.typeform.com/to/SEU_ID_TYPEFORM_3", height=450, scrolling=True)

elif menu == "6. Quiz (Kahoot)":
    st.header("🎮 Quiz Interativo - Kahoot por Disciplina")
    st.write("Preparem-se para o desafio gamificado!")
    
    tab_k1, tab_k2, tab_k3 = st.tabs(["FST1040", "FST7001", "FST8004"])
    with tab_k1:
        st.subheader("Kahoot - FST1040")
        st.markdown("[Acessar Kahoot da Turma FST1040 (kahoot.it)](https://kahoot.it)", unsafe_allow_html=True)
        st.components.v1.iframe("https://kahoot.it/", height=450, scrolling=True)
    with tab_k2:
        st.subheader("Kahoot - FST7001")
        st.markdown("[Acessar Kahoot da Turma FST7001 (kahoot.it)](https://kahoot.it)", unsafe_allow_html=True)
        st.components.v1.iframe("https://kahoot.it/", height=450, scrolling=True)
    with tab_k3:
        st.subheader("Kahoot - FST8004")
        st.markdown("[Acessar Kahoot da Turma FST8004 (kahoot.it)](https://kahoot.it)", unsafe_allow_html=True)
        st.components.v1.iframe("https://kahoot.it/", height=450, scrolling=True)

elif menu == "7. Google Forms":
    st.header("📋 Avaliação / Coleta - Google Forms por Disciplina")
    st.write("Preencha o formulário institucional abaixo:")
    
    tab_g1, tab_g2, tab_g3 = st.tabs(["FST1040", "FST7001", "FST8004"])
    with tab_g1:
        st.subheader("Google Forms - FST1040")
        st.components.v1.iframe("https://docs.google.com/forms/d/e/SEU_LINK_FORMS_1/viewform?embedded=true", height=450, scrolling=True)
    with tab_g2:
        st.subheader("Google Forms - FST7001")
        st.components.v1.iframe("https://docs.google.com/forms/d/e/SEU_LINK_FORMS_2/viewform?embedded=true", height=450, scrolling=True)
    with tab_g3:
        st.subheader("Google Forms - FST8004")
        st.components.v1.iframe("https://docs.google.com/forms/d/e/SEU_LINK_FORMS_3/viewform?embedded=true", height=450, scrolling=True)

elif menu == "8. QR Code de Acesso":
    st.header("📱 QR Code para Acesso Rápido por Disciplina")
    st.write("Aponte a câmera do seu smartphone para acessar o site ou a atividade correspondente.")
    
    tab_q1, tab_q2, tab_q3 = st.tabs(["FST1040", "FST7001", "FST8004"])
    with tab_q1:
        st.subheader("QR Code - FST1040")
        try:
            st.image("qrcode_fst1040.png", width=300, caption="Acesso FST1040")
        except Exception:
            st.warning("⚠️ Adicione a imagem `qrcode_fst1040.png` na pasta do GitHub.")
    with tab_q2:
        st.subheader("QR Code - FST7001")
        try:
            st.image("qrcode_fst7001.png", width=300, caption="Acesso FST7001")
        except Exception:
            st.warning("⚠️ Adicione a imagem `qrcode_fst7001.png` na pasta do GitHub.")
    with tab_q3:
        st.subheader("QR Code - FST8004")
        try:
            st.image("qrcode_fst8004.png", width=300, caption="Acesso FST8004")
        except Exception:
            st.warning("⚠️ Adicione a imagem `qrcode_fst8004.png` na pasta do GitHub.")

elif menu == "9. Feedback da Aula":
    st.header("📝 Avaliação de Reação (Feedback)")
    st.write("Sua opinião é fundamental para avaliarmos a dinâmica e melhorarmos as próximas atividades.")
    
    tab_fb1, tab_fb2, tab_fb3 = st.tabs(["FST1040", "FST7001", "FST8004"])
    with tab_fb1:
        st.subheader("Feedback - FST1040")
        st.components.v1.iframe("https://tally.so/embed/SEU_LINK_FEEDBACK_1?transparentBackground=1", height=450, scrolling=True)
    with tab_fb2:
        st.subheader("Feedback - FST7001")
        st.components.v1.iframe("https://tally.so/embed/SEU_LINK_FEEDBACK_2?transparentBackground=1", height=450, scrolling=True)
    with tab_fb3:
        st.subheader("Feedback - FST8004")
        st.components.v1.iframe("https://tally.so/embed/SEU_LINK_FEEDBACK_3?transparentBackground=1", height=450, scrolling=True)

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
