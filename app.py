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
# Espaço para exibir a logo (você pode subir um arquivo PNG/JPG no GitHub na mesma pasta e colocar o nome aqui, ou usar URL)
# Exemplo: st.sidebar.image("logo.png", width=150)
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

# Menu Lateral para Navegação
menu = st.sidebar.selectbox(
    "Navegue pelas Atividades:",
    [
        "Apresentação",
        "1. Perguntas & Respostas (Q&A)",
        "2. Nuvem de Ideias",
        "3. Feedback da Aula",
    ],
)

# --- CONTEÚDO PRINCIPAL ---
if menu == "Apresentação":
  st.header("🩺 Ambiente Interativo de Aprendizagem")
  st.markdown(
      "Ferramenta de apoio pedagógico para metodologias ativas com estudantes"
      " da graduação em saúde."
  )

  st.subheader("Bem-vindos à aula interativa!")
  st.write(
      "Este espaço foi estruturado para dinamizar nossa discussão de hoje,"
      " permitindo a participação ativa, o levantamento de conceitos-chave e a"
      " avaliação contínua do processo de ensino-aprendizagem."
  )

  st.info(
      "💡 **Dica para o Professor:** Utilize o menu lateral para alternar"
      " entre as ferramentas de Q&A, nuvem de palavras e feedback durante a"
      " sessão."
  )

elif menu == "1. Perguntas & Respostas (Q&A)":
  st.header("💬 Espaço de Perguntas")
  st.write("Envie sua dúvida ou reflexão sobre o caso clínico ou tema discutido.")

  # Insira o link do seu formulário Tally.so para perguntas
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

  # Incorporação exata do AnswerGarden fornecida
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

  # Insira o link do seu formulário Tally.so para feedback
  st.components.v1.iframe(
      "https://tally.so/embed/SEU_LINK_DE_FEEDBACK_DO_TALLY?transparentBackground=1",
      height=500,
      scrolling=True,
  )

# --- RODAPÉ ---
st.markdown("---")

# Estilo CSS opcional para a caixa de citação acadêmica
st.markdown(
    """
<style>
.footer-box {
    background-color: #f8f9fa;
    padding: 15px;
    border-radius: 5px;
    border-left: 4px solid #4b6cb7;
    font-size: 13px;
    color: #333;
    margin-bottom: 15px;
}
</style>
""",
    unsafe_allow_html=True,
)

# 1. Copyright e Direitos Autorais
st.markdown(
    f"<p style='text-align: center; color: gray; font-size:"
    f" 14px;'>© {ano_atual} OLIVEIRA, L.M.V. Todos os direitos reservados.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 13px;'>O conteúdo"
    " deste website (textos, imagens e dados) está protegido pela Lei de"
    " Direitos Autorais (Lei nº 9.610/1998).</p>",
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
    "<p style='text-align: center; color: gray; font-size: 13px;'>NOME LEGAL"
    " PARA O SITE | Metodologias Ativas na Saúde</p>",
    unsafe_allow_html=True,
)
