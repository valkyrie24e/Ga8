mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"21f1005652@student.onlindegree.iitm.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
