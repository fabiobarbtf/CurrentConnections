O Script busca as conexões atuais nos virtuais servers dos Big-IP’s passados no arquivo python “ips.py”, usando o login e senha informado no arquivo python “secret.py”. A busca é feita utilizando as bibliotecas Webdriver, Selenium, Pandas, Openpyxl e BeautifulSoup, através do navegador do ChromeDriver (Arquivo chromedriver.exe). 

Para a execução ser feita via VS Code você deve abrir a pasta do script como raiz, assim evitando erro na execução do Chromedriver. 

Ao executar o script o python irá importar todas as bibliotecas e os variáveis dos demais arquivos, trazendo tudo para o principal, executará o Chromedriver e começará a busca nos IP’s informados. As conexões são concatenadas em apenas um data frame, esse que recebe um export da tabela de conexões editada, como um filtro para melhor entendimento dos dados. 

Ao término da busca, edição e concatenação de data frame, será criado um arquivo Excel com os dados extraídos, sendo esse arquivo nomeado como “CurrentConnections.xlsx”, caso você tenha deixado o arquivo Excel aberto o script não conseguirá editar o mesmo e será criado um novo arquivo Excel. 

Obs.: Observar os dados apontados no arquivo Excel, alguns dos Virtuais Servers podem estar fora de ordem, como o primário embaixo do secundário. E o script pode precisar ser editado caso queira executar a busca em outros IP’s diferentes dos apontados no arquivo “ips.py” ou adicionar IP’s no arquivo. 