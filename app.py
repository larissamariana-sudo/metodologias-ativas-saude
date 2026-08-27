import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Metodologias Ativas na Saúde",
    page_icon="🩺",
    layout="wide"
)

# Título Principal
st.title("🩺 Ambiente Interativo de Aprendizagem")
st.markdown("Ferramenta de apoio para metodologias ativas com estudantes da graduação em saúde.")

# Menu Lateral para Navegação
menu = st.sidebar.selectbox(
    "Navegue pelas Atividades:",
    ["Apresentação", "1. Perguntas & Respostas (Q&A)", "2. Nuvem de Ideias", "3. Feedback da Aula"]
)

if menu == "Apresentação":
    st.header("Bem-vindos à aula interativa!")
    st.write("Utilize o menu lateral para acessar as dinâmicas propostas para a sessão de hoje.")
    st.info("💡 **Dica para o Professor:** Compartilhe o link desta página com os estudantes via QR Code ou chat.")

elif menu == "1. Perguntas & Respostas (Q&A)":
    st.header("💬 Espaço de Perguntas")
    st.write("Envie sua dúvida ou reflexão sobre o caso clínico/tema discutido.")
    
    # Opção 1: Formulário integrado gratuito (ex: Google Forms ou Tally.so embutido)
    # Substitua a URL abaixo pelo link de incorporação do seu formulário gratuito
    st.markdown("Envie sua resposta através do formulário abaixo:")
    st.components.v1.iframe("https://tally.so/embed/3y8869?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1", height=400)

elif menu == "2. Nuvem de Ideias":
    st.header("☁️ Nuvem de Ideias / Brainstorming")
    st.write("Digite palavras-chave que resumem o conceito abordado na discussão de hoje.")

    # Código HTML/JS do AnswerGarden inserido via componente Streamlit
    answergarden_codigo = """
    <div style="width: 100%; height: 500px;">
        <script type="text/javascript" src="https://answergarden.ch/embed/<iframe src="https://answergarden.ch/embed/5215672" width="640px" height="400px" style="border: none;" scrolling="no" frameborder="0" title="AnswerGarden" allowTransparency="true"><p><a href="https://answergarden.ch/5215672">Go to AnswerGarden</a></p></iframe>"></script>
    </div>
    """
    st.components.v1.html(answergarden_codigo, height=520, scrolling=True)

elif menu == "3. Feedback da Aula":
    st.header("📝 Avaliação de Reação (Feedback)")
    st.write("Sua opinião é fundamental para melhorarmos as próximas dinâmicas.")
    
    # Formulário rápido de feedback
    with st.form("feedback_form"):
        pontos = st.slider("Como você avalia a dinâmica de hoje?", 1, 5, 5)
        comentario = st.text_area("O que foi mais marcante ou poderia ser melhorado?")
        enviado = st.form_submit_button("Enviar Feedback")
        
        if enviado:
            st.success("Obrigado! Seu feedback foi registrado com sucesso.")
