<h1>Preditor de Câncer de Mama</h1>

<p>Este repositório contém um aplicativo web desenvolvido em Python usando a biblioteca <strong>Streamlit</strong>, que permite prever se um tumor mamário é benigno ou maligno com base em medidas de núcleos celulares.</p>

<h2>Descrição</h2>

<p>O aplicativo utiliza um modelo de aprendizado de máquina treinado para classificar tumores mamários. Ele coleta medidas de núcleos celulares através de controles deslizantes e gera um gráfico de radar que visualiza as características selecionadas. Os resultados incluem a previsão da classe do tumor e as probabilidades associadas.</p>

<h2>Funcionalidades</h2>
<ul>
    <li><strong>Interface interativa</strong>: Os usuários podem inserir medidas de núcleos celulares usando controles deslizantes na barra lateral.</li>
    <li><strong>Gráfico de Radar</strong>: Visualização das características do tumor em formato de gráfico de radar.</li>
    <li><strong>Previsão</strong>: O aplicativo fornece a previsão de classe do tumor (Benigno ou Maligno) e suas respectivas probabilidades.</li>
</ul>

<h2>Pré-requisitos</h2>

<p>Antes de executar o aplicativo, verifique se você tem os seguintes pacotes instalados:</p>

<pre><code>pip install streamlit pandas plotly scikit-learn</code></pre>

<h2>Estrutura do Projeto</h2>

<pre><code>
/projeto
│
├── data/
│   └── data.csv               # Conjunto de dados para a previsão
│
├── model/
│   ├── model.pkl              # Modelo treinado
│   └── scaler.pkl             # Scaler para normalização dos dados
│
├── assets/
│   └── style.css              # Estilos CSS para o aplicativo
│
└── app.py                     # Código principal do aplicativo
</code></pre>

<h2>Como Executar o Aplicativo</h2>

<p>Para executar o aplicativo, navegue até o diretório do projeto e use o seguinte comando:</p>

<pre><code>streamlit run app.py</code></pre>

<h2>Uso</h2>
<ol>
    <li>Acesse a barra lateral para inserir as medidas dos núcleos celulares.</li>
    <li>Visualize o gráfico de radar correspondente às medidas inseridas.</li>
    <li>O aplicativo exibirá a previsão do tumor e as probabilidades de ser benigno ou maligno.</li>
</ol>

<h2>Aviso</h2>

<p>Este aplicativo pode auxiliar profissionais médicos no diagnóstico, mas não deve ser utilizado como substituto de um diagnóstico profissional.</p>

<h2>Acesse o Web App</h2>

<p>Você pode acessar o aplicativo web diretamente através do link: <a href="(https://cancermamadetector.streamlit.app/)">Preditor de Câncer de Mama</a></p>

<h2>Contribuições</h2>

<p>Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.</p>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a <strong>MIT License</strong>. Veja o arquivo LICENSE para mais detalhes.</p>
