import os
import jinja2 as j2
import webbrowser
from threading import Thread
import time
import subprocess
import platform

# Criar Directórios

def create_dirs():
	path = os.getcwd()
	projectfolder = path + '/gp8'
	os.mkdir(projectfolder)
	templatesfolder = path + '/gp8/templates'
	os.mkdir(templatesfolder)
	envfolder = path + '/gp8/env'

# Criar Templates

def criarbase():
    base = """
               <!DOCTYPE html>
<html>
<head>
 	{% block head %} {% endblock %}
	<meta charset="utf-8">
	<style>
		body {background-color:#bdcebe;
			  width:100%;
			  align-self: center;}
		div.nav {width:100%;
				align-self: center;
				padding-left: 12.5%}
		div.hed {}
		table.tab_nav {width:100%;}
		th.columnav{background-color:#bdcebe;
			border:0.5px solid lightgrey;
			height: 40px;
			width:25%;
		}
	</style>
					<form action="/" method='POST'>
					<label>Procurar:</label><br>
					<input type="text" name="userinput" placeholder="Procurar"><br>
					<input type="submit" value="Submit">
					</form>
	<!-- Assume-se o Navigator é igual em todas as páginas do trabalho -->
    
	<div class="nav">
    <style>
      button {
        display: inline-block;
        background-color: #ada397;
        border-radius: 8px;
        border: 4px double #cccccc;
        color: #eeeeee;
        text-align: center;
        font-size: 15px;
        padding: 15px;
        width: 300px;
        -webkit-transition: all 0.5s;
        -moz-transition: all 0.5s;
        -o-transition: all 0.5s;
        transition: all 0.5s;
        cursor: pointer;
        margin: 10px;
      }
body {
  font-family: Times New Roman;
}

* {
  box-sizing: border-box;
}

form.example input[type=text] {
  padding: 10px;
  font-size: 17px;
  border: 1px solid grey;
  float: left;
  width: 80%;
  background: #f1f1f1;
}

form.example button {
  float: left;
  width: 20%;
  padding: 10px;
  background: #2196F3;
  color: white;
  font-size: 17px;
  border: 1px solid grey;
  border-left: none;
  cursor: pointer;
}

form.example button:hover {
  background: #0b7dda;
}

form.example::after {
  content: "";
  clear: both;
  display: table;
}
</style>
  <body>
    <a href="/"><button type="button">Lista CDs</button></a>
  </body>
  
  <body>
    <a href="/cds/novocd"><button type="button">Adicionar CDs</button></a>
  </body>
  
  <body>
    <a href="/autores"><button type="button">Informações Adicionais</button></a>
  </body>
	
	</div>
    
    
	<!-- Real conteudo que aparece sempre que invocamos outras funçoes  -->

	{% block body %} {% endblock %}

</body>
</html>

                """

    path = os.getcwd() + '/gp8/templates/base.html'
    base_out = open(path, 'w', encoding='utf-8')
    base_out.write(base)
    base_out.close()

def criarindex():
    index ="""
{% extends 'base.html' %}
{% block head%} <title>Homepage</title>

	<style>
		body {background-color:#ECF9F9;
			  width:100%;
			  align-content: center;}
		div.nav {width:75%;
				align-self: center;
				padding-left: 12.5%}
		div.hed {padding-top: 15px;
				padding-bottom: 15px;
				text-align:center;
				margin-top:5px;
				font-size: 20px;
				color: black;
				border-radius: 20px;}
		table.tab_nav {width:100%;}
		th.columnav{background-color:#C7DBED;
			border:0.5px solid lightgrey;
			height: 40px;
			width:25%;}
		div.contents {

			width:100%;
			padding-top: 50px;
			padding-bottom:50px;
			padding-left:12.5%;
			align-content: center;}
		table.content {
			border-radius: 20px;
			background-color:#C7DBED;
			width:75%;
			padding-top:75px;
			padding-bottom:75px;
			align-content: center;}



	</style>
{% endblock %}
<!--

	Neste caso no body aparece a lista de relatórios como link para "ver relatório".( posteriormente em ver relatorio adicionamos tudo a caixas de texto de modo a ser editavel e podemos até ter uma primeira versão nao editavel e depois um botao para entrar em modo editavel)
	Na mesma linha do titulo é adicionado um botão para o apagar.
	O botão remover deve apagar o titulo e o relatório a ele associado e devolver a mesma página sem esse elemento

-->
<!-- Falta aqui a parte de procurar o relatório -->
{% block body%}
<div class='contents'>
	<table class='content'>

	{% for p in cds %}
			<tr>
				<th>
					<a href="/cds/{{p}}">{{p}}</a>
				</th>
				<th>
					<form action="/delete/{{p}}" method="post">
						<button type ="submit"> Delete </button>
					</form>
				</th>
			</tr>
		{% endfor %}
	</table>
</div>
{% endblock %}

                """

    path = os.getcwd() + '/gp8/templates/index.html'
    cindex_out = open(path, 'w', encoding='utf-8')
    cindex_out.write(index)
    cindex_out.close()

def criarcd():
    cd = """
              {% extends 'base.html' %}
<!-- O titulo passa a ser o nome do titulo do relatorio -->
{% block head%} <title>{{p[title]}}</title>

{% endblock %}

<!-- Neste caso aparece o titulo e o valor associado ao titulo -->
{% block body%}
<h1>{{p['title']}}</h1>
<h2><img src={{p['artwork']}} alt="Album Artwork"></h2>
<h2>{{p['artist']}}</h2>
<h2>País: {{p['country']}} <img src="https://flagcdn.com/h20/{{p['country']}}.png" alt="Bandeira"></h2>
<h2>Produtora: {{p['company']}}</h2>
<h2>Descrição: {{p['description']}}</h2>
<h2>Ano: {{p['year']}}</h2>
<form action="/delete/{{p['title']}}" method="post">
  <button type ="submit"> Delete </button>
</form>
{% endblock %}
 """
    path = os.getcwd() + '/gp8/templates/cd_view.html'
    cd_out = open(path, 'w', encoding='utf-8')
    cd_out.write(cd)
    cd_out.close()

def adicionarcd():
    add_cd = """
                {% extends 'base.html' %}

{% block head%} <title> Novo CD </title> {% endblock %}
<!--
	Neste caso no body aparece um form para ser possivel postar o novo relatório
	O relatório deve obedecer ao numero de parametros pré-determinado (Melhorar depois para qualquer conteudo) ( Neste caso está para receber os dados do ficheiro?? )
-->
{% block body%}
	<h3>Adicionar CD</h3>
  <style> 
input[type=text] {
  width: 55%;
  padding: 12px 16px;
  margin: 8px ;
  box-sizing: border-box;
  border: 2px solid green;
  border-radius: 4px;
}
</style>
	<form action="novocd" method='POST'>
		<label>Título</label><br>
		<input type="text" name="title"><br>
		<label>Artista</label><br>
		<input type="text" name="artist"><br>
		<label>Artwork</label><br>
		<input type="text" name="artwork"><br>
		<label>País</label><br>
    <input list="countries" name="country">
    <datalist id="countries">
        <option value="Afghanistan" />
        <option value="Albania" />
        <option value="Algeria" />
        <option value="American Samoa" />
        <option value="Andorra" />
        <option value="Angola" />
        <option value="Anguilla" />
        <option value="Antarctica" />
        <option value="Antigua and Barbuda" />
        <option value="Argentina" />
        <option value="Armenia" />
        <option value="Aruba" />
        <option value="Australia" />
        <option value="Austria" />
        <option value="Azerbaijan" />
        <option value="Bahamas" />
        <option value="Bahrain" />
        <option value="Bangladesh" />
        <option value="Barbados" />
        <option value="Belarus" />
        <option value="Belgium" />
        <option value="Belize" />
        <option value="Benin" />
        <option value="Bermuda" />
        <option value="Bhutan" />
        <option value="Bolivia" />
        <option value="Bosnia and Herzegovina" />
        <option value="Botswana" />
        <option value="Bouvet Island" />
        <option value="Brazil" />
        <option value="British Indian Ocean Territory" />
        <option value="Brunei Darussalam" />
        <option value="Bulgaria" />
        <option value="Burkina Faso" />
        <option value="Burundi" />
        <option value="Cambodia" />
        <option value="Cameroon" />
        <option value="Canada" />
        <option value="Cape Verde" />
        <option value="Cayman Islands" />
        <option value="Central African Republic" />
        <option value="Chad" />
        <option value="Chile" />
        <option value="China" />
        <option value="Christmas Island" />
        <option value="Cocos (Keeling) Islands" />
        <option value="Colombia" />
        <option value="Comoros" />
        <option value="Congo" />
        <option value="Congo, The Democratic Republic of The" />
        <option value="Cook Islands" />
        <option value="Costa Rica" />
        <option value="Cote D'ivoire" />
        <option value="Croatia" />
        <option value="Cuba" />
        <option value="Cyprus" />
        <option value="Czech Republic" />
        <option value="Denmark" />
        <option value="Djibouti" />
        <option value="Dominica" />
        <option value="Dominican Republic" />
        <option value="Ecuador" />
        <option value="Egypt" />
        <option value="El Salvador" />
        <option value="Equatorial Guinea" />
        <option value="Eritrea" />
        <option value="Estonia" />
        <option value="Ethiopia" />
        <option value="Falkland Islands (Malvinas)" />
        <option value="Faroe Islands" />
        <option value="Fiji" />
        <option value="Finland" />
        <option value="France" />
        <option value="French Guiana" />
        <option value="French Polynesia" />
        <option value="French Southern Territories" />
        <option value="Gabon" />
        <option value="Gambia" />
        <option value="Georgia" />
        <option value="Germany" />
        <option value="Ghana" />
        <option value="Gibraltar" />
        <option value="Greece" />
        <option value="Greenland" />
        <option value="Grenada" />
        <option value="Guadeloupe" />
        <option value="Guam" />
        <option value="Guatemala" />
        <option value="Guinea" />
        <option value="Guinea-bissau" />
        <option value="Guyana" />
        <option value="Haiti" />
        <option value="Heard Island and Mcdonald Islands" />
        <option value="Holy See (Vatican City State)" />
        <option value="Honduras" />
        <option value="Hong Kong" />
        <option value="Hungary" />
        <option value="Iceland" />
        <option value="India" />
        <option value="Indonesia" />
        <option value="Iran, Islamic Republic of" />
        <option value="Iraq" />
        <option value="Ireland" />
        <option value="Israel" />
        <option value="Italy" />
        <option value="Jamaica" />
        <option value="Japan" />
        <option value="Jordan" />
        <option value="Kazakhstan" />
        <option value="Kenya" />
        <option value="Kiribati" />
        <option value="Korea, Democratic People's Republic of" />
        <option value="Korea, Republic of" />
        <option value="Kuwait" />
        <option value="Kyrgyzstan" />
        <option value="Lao People's Democratic Republic" />
        <option value="Latvia" />
        <option value="Lebanon" />
        <option value="Lesotho" />
        <option value="Liberia" />
        <option value="Libyan Arab Jamahiriya" />
        <option value="Liechtenstein" />
        <option value="Lithuania" />
        <option value="Luxembourg" />
        <option value="Macao" />
        <option value="Macedonia, The Former Yugoslav Republic of" />
        <option value="Madagascar" />
        <option value="Malawi" />
        <option value="Malaysia" />
        <option value="Maldives" />
        <option value="Mali" />
        <option value="Malta" />
        <option value="Marshall Islands" />
        <option value="Martinique" />
        <option value="Mauritania" />
        <option value="Mauritius" />
        <option value="Mayotte" />
        <option value="Mexico" />
        <option value="Micronesia, Federated States of" />
        <option value="Moldova, Republic of" />
        <option value="Monaco" />
        <option value="Mongolia" />
        <option value="Montserrat" />
        <option value="Morocco" />
        <option value="Mozambique" />
        <option value="Myanmar" />
        <option value="Namibia" />
        <option value="Nauru" />
        <option value="Nepal" />
        <option value="Netherlands" />
        <option value="Netherlands Antilles" />
        <option value="New Caledonia" />
        <option value="New Zealand" />
        <option value="Nicaragua" />
        <option value="Niger" />
        <option value="Nigeria" />
        <option value="Niue" />
        <option value="Norfolk Island" />
        <option value="Northern Mariana Islands" />
        <option value="Norway" />
        <option value="Oman" />
        <option value="Pakistan" />
        <option value="Palau" />
        <option value="Palestinian Territory, Occupied" />
        <option value="Panama" />
        <option value="Papua New Guinea" />
        <option value="Paraguay" />
        <option value="Peru" />
        <option value="Philippines" />
        <option value="Pitcairn" />
        <option value="Poland" />
        <option value="Portugal" />
        <option value="Puerto Rico" />
        <option value="Qatar" />
        <option value="Reunion" />
        <option value="Romania" />
        <option value="Russian Federation" />
        <option value="Rwanda" />
        <option value="Saint Helena" />
        <option value="Saint Kitts and Nevis" />
        <option value="Saint Lucia" />
        <option value="Saint Pierre and Miquelon" />
        <option value="Saint Vincent and The Grenadines" />
        <option value="Samoa" />
        <option value="San Marino" />
        <option value="Sao Tome and Principe" />
        <option value="Saudi Arabia" />
        <option value="Senegal" />
        <option value="Serbia and Montenegro" />
        <option value="Seychelles" />
        <option value="Sierra Leone" />
        <option value="Singapore" />
        <option value="Slovakia" />
        <option value="Slovenia" />
        <option value="Solomon Islands" />
        <option value="Somalia" />
        <option value="South Africa" />
        <option value="South Georgia and The South Sandwich Islands" />
        <option value="Spain" />
        <option value="Sri Lanka" />
        <option value="Sudan" />
        <option value="Suriname" />
        <option value="Svalbard and Jan Mayen" />
        <option value="Swaziland" />
        <option value="Sweden" />
        <option value="Switzerland" />
        <option value="Syrian Arab Republic" />
        <option value="Taiwan, Province of China" />
        <option value="Tajikistan" />
        <option value="Tanzania, United Republic of" />
        <option value="Thailand" />
        <option value="Timor-leste" />
        <option value="Togo" />
        <option value="Tokelau" />
        <option value="Tonga" />
        <option value="Trinidad and Tobago" />
        <option value="Tunisia" />
        <option value="Turkey" />
        <option value="Turkmenistan" />
        <option value="Turks and Caicos Islands" />
        <option value="Tuvalu" />
        <option value="Uganda" />
        <option value="Ukraine" />
        <option value="United Arab Emirates" />
        <option value="United Kingdom" />
        <option value="United States" />
        <option value="United States Minor Outlying Islands" />
        <option value="Uruguay" />
        <option value="Uzbekistan" />
        <option value="Vanuatu" />
        <option value="Venezuela" />
        <option value="Viet Nam" />
        <option value="Virgin Islands, British" />
        <option value="Virgin Islands, U.S" />
        <option value="Wallis and Futuna" />
        <option value="Western Sahara" />
        <option value="Yemen" />
        <option value="Zambia" />
        <option value="Zimbabwe" />
    </datalist><br>
		<label>Produtora</label><br>
		<input type="text" name="company"><br>
		<label>Descrição</label><br>
    <textarea name="description" style="width:200px"></textarea><br>
		<label>Ano</label><br>
		<input type="text" name="year"><br>
		<input type="submit" value="Submit">
	</form>
{% endblock %}                """
    path = os.getcwd() + '/gp8/templates/add_cd_view.html'
    add_out = open(path, 'w', encoding='utf-8')
    add_out.write(add_cd)
    add_out.close()

def atualizarcd():
    atualizacd = """
                {% extends 'base.html' %}

                {% block head%} <title>{{p[title]}}</title> {% endblock %}
                <!--
                        Neste caso no body aparece um form para ser possivel postar o novo relatório
                        O relatório deve obedecer ao numero de parametros pré-determinado (Melhorar depois para qualquer conteudo) ( Neste caso está para receber os dados do ficheiro?? )
                -->
                {% block body%}
                        <h3>A atualizar {{p[title]}}</h3>
                        <form action="update" method='POST'>
                                <label>Título</label><br>
                                <input type="text" name="title"><br>
                                <label>Artista</label><br>
                                <input type="text" name="artist"><br>
                                <label>Artwork</label><br>
                                <input type="text" name="artwork"><br>
                                <label>País</label><br>
                    <input list="countries" name="country">
                    <datalist id="countries">
                        <option value="Afghanistan" />
                        <option value="Albania" />
                        <option value="Algeria" />
                        <option value="American Samoa" />
                        <option value="Andorra" />
                        <option value="Angola" />
                        <option value="Anguilla" />
                        <option value="Antarctica" />
                        <option value="Antigua and Barbuda" />
                        <option value="Argentina" />
                        <option value="Armenia" />
                        <option value="Aruba" />
                        <option value="Australia" />
                        <option value="Austria" />
                        <option value="Azerbaijan" />
                        <option value="Bahamas" />
                        <option value="Bahrain" />
                        <option value="Bangladesh" />
                        <option value="Barbados" />
                        <option value="Belarus" />
                        <option value="Belgium" />
                        <option value="Belize" />
                        <option value="Benin" />
                        <option value="Bermuda" />
                        <option value="Bhutan" />
                        <option value="Bolivia" />
                        <option value="Bosnia and Herzegovina" />
                        <option value="Botswana" />
                        <option value="Bouvet Island" />
                        <option value="Brazil" />
                        <option value="British Indian Ocean Territory" />
                        <option value="Brunei Darussalam" />
                        <option value="Bulgaria" />
                        <option value="Burkina Faso" />
                        <option value="Burundi" />
                        <option value="Cambodia" />
                        <option value="Cameroon" />
                        <option value="Canada" />
                        <option value="Cape Verde" />
                        <option value="Cayman Islands" />
                        <option value="Central African Republic" />
                        <option value="Chad" />
                        <option value="Chile" />
                        <option value="China" />
                        <option value="Christmas Island" />
                        <option value="Cocos (Keeling) Islands" />
                        <option value="Colombia" />
                        <option value="Comoros" />
                        <option value="Congo" />
                        <option value="Congo, The Democratic Republic of The" />
                        <option value="Cook Islands" />
                        <option value="Costa Rica" />
                        <option value="Cote D'ivoire" />
                        <option value="Croatia" />
                        <option value="Cuba" />
                        <option value="Cyprus" />
                        <option value="Czech Republic" />
                        <option value="Denmark" />
                        <option value="Djibouti" />
                        <option value="Dominica" />
                        <option value="Dominican Republic" />
                        <option value="Ecuador" />
                        <option value="Egypt" />
                        <option value="El Salvador" />
                        <option value="Equatorial Guinea" />
                        <option value="Eritrea" />
                        <option value="Estonia" />
                        <option value="Ethiopia" />
                        <option value="Falkland Islands (Malvinas)" />
                        <option value="Faroe Islands" />
                        <option value="Fiji" />
                        <option value="Finland" />
                        <option value="France" />
                        <option value="French Guiana" />
                        <option value="French Polynesia" />
                        <option value="French Southern Territories" />
                        <option value="Gabon" />
                        <option value="Gambia" />
                        <option value="Georgia" />
                        <option value="Germany" />
                        <option value="Ghana" />
                        <option value="Gibraltar" />
                        <option value="Greece" />
                        <option value="Greenland" />
                        <option value="Grenada" />
                        <option value="Guadeloupe" />
                        <option value="Guam" />
                        <option value="Guatemala" />
                        <option value="Guinea" />
                        <option value="Guinea-bissau" />
                        <option value="Guyana" />
                        <option value="Haiti" />
                        <option value="Heard Island and Mcdonald Islands" />
                        <option value="Holy See (Vatican City State)" />
                        <option value="Honduras" />
                        <option value="Hong Kong" />
                        <option value="Hungary" />
                        <option value="Iceland" />
                        <option value="India" />
                        <option value="Indonesia" />
                        <option value="Iran, Islamic Republic of" />
                        <option value="Iraq" />
                        <option value="Ireland" />
                        <option value="Israel" />
                        <option value="Italy" />
                        <option value="Jamaica" />
                        <option value="Japan" />
                        <option value="Jordan" />
                        <option value="Kazakhstan" />
                        <option value="Kenya" />
                        <option value="Kiribati" />
                        <option value="Korea, Democratic People's Republic of" />
                        <option value="Korea, Republic of" />
                        <option value="Kuwait" />
                        <option value="Kyrgyzstan" />
                        <option value="Lao People's Democratic Republic" />
                        <option value="Latvia" />
                        <option value="Lebanon" />
                        <option value="Lesotho" />
                        <option value="Liberia" />
                        <option value="Libyan Arab Jamahiriya" />
                        <option value="Liechtenstein" />
                        <option value="Lithuania" />
                        <option value="Luxembourg" />
                        <option value="Macao" />
                        <option value="Macedonia, The Former Yugoslav Republic of" />
                        <option value="Madagascar" />
                        <option value="Malawi" />
                        <option value="Malaysia" />
                        <option value="Maldives" />
                        <option value="Mali" />
                        <option value="Malta" />
                        <option value="Marshall Islands" />
                        <option value="Martinique" />
                        <option value="Mauritania" />
                        <option value="Mauritius" />
                        <option value="Mayotte" />
                        <option value="Mexico" />
                        <option value="Micronesia, Federated States of" />
                        <option value="Moldova, Republic of" />
                        <option value="Monaco" />
                        <option value="Mongolia" />
                        <option value="Montserrat" />
                        <option value="Morocco" />
                        <option value="Mozambique" />
                        <option value="Myanmar" />
                        <option value="Namibia" />
                        <option value="Nauru" />
                        <option value="Nepal" />
                        <option value="Netherlands" />
                        <option value="Netherlands Antilles" />
                        <option value="New Caledonia" />
                        <option value="New Zealand" />
                        <option value="Nicaragua" />
                        <option value="Niger" />
                        <option value="Nigeria" />
                        <option value="Niue" />
                        <option value="Norfolk Island" />
                        <option value="Northern Mariana Islands" />
                        <option value="Norway" />
                        <option value="Oman" />
                        <option value="Pakistan" />
                        <option value="Palau" />
                        <option value="Palestinian Territory, Occupied" />
                        <option value="Panama" />
                        <option value="Papua New Guinea" />
                        <option value="Paraguay" />
                        <option value="Peru" />
                        <option value="Philippines" />
                        <option value="Pitcairn" />
                        <option value="Poland" />
                        <option value="Portugal" />
                        <option value="Puerto Rico" />
                        <option value="Qatar" />
                        <option value="Reunion" />
                        <option value="Romania" />
                        <option value="Russian Federation" />
                        <option value="Rwanda" />
                        <option value="Saint Helena" />
                        <option value="Saint Kitts and Nevis" />
                        <option value="Saint Lucia" />
                        <option value="Saint Pierre and Miquelon" />
                        <option value="Saint Vincent and The Grenadines" />
                        <option value="Samoa" />
                        <option value="San Marino" />
                        <option value="Sao Tome and Principe" />
                        <option value="Saudi Arabia" />
                        <option value="Senegal" />
                        <option value="Serbia and Montenegro" />
                        <option value="Seychelles" />
                        <option value="Sierra Leone" />
                        <option value="Singapore" />
                        <option value="Slovakia" />
                        <option value="Slovenia" />
                        <option value="Solomon Islands" />
                        <option value="Somalia" />
                        <option value="South Africa" />
                        <option value="South Georgia and The South Sandwich Islands" />
                        <option value="Spain" />
                        <option value="Sri Lanka" />
                        <option value="Sudan" />
                        <option value="Suriname" />
                        <option value="Svalbard and Jan Mayen" />
                        <option value="Swaziland" />
                        <option value="Sweden" />
                        <option value="Switzerland" />
                        <option value="Syrian Arab Republic" />
                        <option value="Taiwan, Province of China" />
                        <option value="Tajikistan" />
                        <option value="Tanzania, United Republic of" />
                        <option value="Thailand" />
                        <option value="Timor-leste" />
                        <option value="Togo" />
                        <option value="Tokelau" />
                        <option value="Tonga" />
                        <option value="Trinidad and Tobago" />
                        <option value="Tunisia" />
                        <option value="Turkey" />
                        <option value="Turkmenistan" />
                        <option value="Turks and Caicos Islands" />
                        <option value="Tuvalu" />
                        <option value="Uganda" />
                        <option value="Ukraine" />
                        <option value="United Arab Emirates" />
                        <option value="United Kingdom" />
                        <option value="United States" />
                        <option value="United States Minor Outlying Islands" />
                        <option value="Uruguay" />
                        <option value="Uzbekistan" />
                        <option value="Vanuatu" />
                        <option value="Venezuela" />
                        <option value="Viet Nam" />
                        <option value="Virgin Islands, British" />
                        <option value="Virgin Islands, U.S" />
                        <option value="Wallis and Futuna" />
                        <option value="Western Sahara" />
                        <option value="Yemen" />
                        <option value="Zambia" />
                        <option value="Zimbabwe" />
                    </datalist><br>
                                <label>Produtora</label><br>
                                <input type="text" name="company"><br>
                                <label>Descrição</label><br>
                    <textarea name="description" style="width:200px"></textarea><br>
                                <label>Ano</label><br>
                                <input type="text" name="year"><br>
                                <input type="submit" value="Submit">
                        </form>
                {% endblock %}
                """
    path = os.getcwd() + '/gp8/templates/atualiza_cd_view.html'
    cat_out = open(path, 'w', encoding='utf-8')
    cat_out.write(atualizacd)
    cat_out.close()

def informaad():
    infoadic = """
                {% extends 'base.html' %}

                {% block head%} <title> Informaçoes Adicionais </title> {% endblock %}
                <!--

                        Neste caso no body aparece algum conteudo sobre o motivo do projecto e a lista de autores para o mesmo.

                -->
                {% block body%}
                <h1>Enquadramento do Projeto</h1>
                        <p>É apresentado o trabalho prático 2 da cadeira de Publicação Eletrónica. </p>
                <h1>Lista de Autores do Projeto</h1>
                <ul>
                    {% for autor in autores: %}
                        <li><p>{{autor.name}}</p><p>{{autor.number}}</p></li>
                    {% endfor %}
                </ul>

                {% endblock %}
                """
    path = os.getcwd() + '/gp8/templates/info_ad_view.html'
    infoad_out = open(path, 'w', encoding='utf-8')
    infoad_out.write(infoadic)
    infoad_out.close()

def procuraresultado():
    search_results = """
{% extends 'base.html' %}

{% block head%} <title> Search Results </title> {% endblock %}

{% block body%}
	<h1>Resultados da Pesquisa</h1>
	{% for cd in p: %}
		<a href="/cds/{{p[cd]}}">{{p[cd]}}</a>
	{% endfor %}
{% endblock %}"""
    path = os.getcwd() + '/gp8/templates/search_results.html'
    procurares_out = open(path, 'w', encoding='utf-8')
    procurares_out.write(search_results)
    procurares_out.close()
        
def createdb_cd():
    db_content= """import shelve
def find_all():
    with shelve.open('cds.db') as s:
        return list(s.keys())

def find_one(title):
    with shelve.open('cds.db') as s:
        return s[title]

def insert(cd):
    with shelve.open('cds.db', writeback=True) as s:
        s[cd['title']] = cd
        return s

def delete(title):
	with shelve.open('cds.db', writeback=True) as s:
		del s[title]
		return list(s.keys()) """
    
    path = os.getcwd() + '/gp8/db_cd.py'
    db_out = open(path, 'w', encoding='utf-8')
    db_out.write(db_content)
    db_out.close()

def createmain(): 
    contentmain= """    # Imports
from flask import Flask, render_template, request, redirect
import json
import requests
from db_cd import *
import re

# Lista Inicial de CDs - Catálogo
cds = [
    {
        'id': 0,
        'title': 'A Vida Que Eu Escolhi',
        'artist': 'Tony Carreira',
        'artwork': 'https://img.discogs.com/ZrC2cjDjuh_mremQ6o5kXKlTFAQ=/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-5263584-1389034439-9728.jpeg.jpg',
        'country': 'PT',
        'company': 'Espacial',
        'description': 'A Vida Que Eu Escolhi é o décimo segundo álbum de estúdio a solo do cantor português Tony Carreira. Foi lançado em 2006 pela editora Espacial. Este trabalho esteve, ao todo, 64 semanas, no Top Oficial da AFP, a tabela semanal dos 30 álbuns mais vendidos em Portugal. Entrou na época de Natal de 2006 directamente para a 4ª posição, atingindo o 1º lugar à quarta semana, lugar que disputaria com André Sardet e Madonna e que ocuparia por mais 3 ocasiões mas que perderia definitivamente para José Afonso.',
        'year': '2006'
    },
    {
        'id': 1,
        'title': 'Hide Your Heart',
        'artist': 'Bonnie Tyler',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/2/23/Hide_Your_Heart_Front_Cover.jpg',
        'country': 'GB',
        'company': 'CBS Records',
        'description': 'Hide Your Heart (released under the title Notes from America in the United States, Canada and Brazil), is the seventh studio album by Welsh singer Bonnie Tyler. The album features the song "Hide Your Heart" written by Paul Stanley, Desmond Child and Holly Knight.',
        'year': '1988'
    },
    {
        'id': 2,
        'title': 'Aja',
        'artist': 'Steely Dan',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/4/49/Aja_album_cover.jpg',
        'country': 'US',
        'company': 'Harvest',
        'description': 'Aja (/ˈeɪʒə/, pronounced like Asia) is the sixth studio album by the American jazz rock band Steely Dan. It was released in September 1977 by ABC Records. Recording alongside nearly 40 musicians, band leaders Donald Fagen and Walter Becker pushed Steely Dan further into experimenting with different combinations of session players while pursuing longer, more sophisticated compositions for the album.',
        'year': '1973'
    },
    {
        'id': 3,
        'title': 'The Dark Side of The Moon',
        'artist': 'Pink Floyd',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/3/3b/Dark_Side_of_the_Moon.png',
        'country': 'GB',
        'company': 'Harvest',
        'description': 'The Dark Side of the Moon is the eighth studio album by the English rock band Pink Floyd, released on 1 March 1973 by Harvest Records. Primarily developed during live performances, the band premiered an early version of the record several months before recording began. The record was conceived as an album that focused on the pressures faced by the band during their arduous lifestyle, and dealing with the apparent mental health problems suffered by former band member Syd Barrett, who departed the group in 1968. New material was recorded in two sessions in 1972 and 1973 at Abbey Road Studios in London.',
        'year': '1973'
    },
    {
        'id': 4,
        'title': 'Return to the 36 Chambers',
        'artist': 'Ol Dirty Bastard',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/b/bf/Odb_welfare.jpg',
        'country': 'US',
        'company': 'Elektra',
        'description': 'Return to the 36 Chambers is the solo debut album of American rapper and Wu-Tang Clan member Ol Dirty Bastard, released March 28, 1995 on Elektra Records in the United States. It was the second solo album, after Method Mans Tical, to be released from the nine-member Wu-Tang clan, following the release of their debut album. Return to the 36 Chambers was primarily produced by RZA, with additional production from Ol Dirty Bastard, and affiliates True Master and 4th Disciple. The album features guest appearances from Wu-Tang members GZA, RZA, Method Man, Raekwon, Ghostface Killah and Masta Killa, as well as several Wu-Tang affiliates and Brooklyn Zu.',
        'year': '1995'
    },
    {
        'id': 5,
        'title': 'Unchain My Heart',
        'artist': 'Joe Cocker',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/8/8e/Joe_Cocker-Unchain_My_Heart_%28album_cover%29.jpg',
        'country': 'US',
        'company': 'EMI',
        'description': 'Unchain My Heart is the eleventh studio album by Joe Cocker, released in 1987.',
        'year': '1987'
    },
    {
        'id': 6,
        'title': 'Picture Book',
        'artist': 'Simply Red',
        'artwork': 'https://upload.wikimedia.org/wikipedia/en/e/e5/PictureBookSimplyRedalbumcover.png',
        'country': 'GB',
        'company': 'Elektra',
        'description': 'Picture Book is the debut album by British pop and soul group Simply Red, released in October 1985.',
        'year': '1985'
    }]
# Lista de Autores
autores = [
    {'name': 'Bruno Rebelo Lopes', 'number': '57768'},
			{'name':'Morgana Sacramento Ferreira','number':'93779'},
			{'name':'Luís Pedro da Silva Pinto','number':'83016'}]

app = Flask(__name__) # required

# Ciclo Auxiliar para inserir a lista inicial de CDs
for cd in cds:
    insert(cd)


# --------------------------- Home Page - Index - Lista de CDs -----------------------------
# ----------------------------------------------------FRONTEND
@app.route('/', methods=['GET'])
def index_view():
    res = requests.get('http://localhost:5000/api/cds')
    ps = json.loads(res.content)
    return render_template('index.html', cds=ps)

# ----------------------------------------------------BACKEND
@app.route('/api/cds', methods=['GET'])
def api_get_cds():
    ps = find_all()
    return json.dumps(ps)

# ------------------ Lista de Autores - Informações Adicionais -----------------------------
# ----------------------------------------------------FRONTEND
@app.route('/autores', methods=['GET'])
def info_ad_view():
	res = requests.get('http://localhost:5000/api/autores')
	ss = json.loads(res.content)
	return render_template('info_ad_view.html', autores=ss)

# ----------------------------------------------------BACKEND
@app.route('/api/autores', methods=['GET'])
def api_get_autores():
    ss = autores
    return json.dumps(ss)

# ---------------------------------------------------- View CD --------------------------------
# ----------------------------------------------------FRONTEND
@app.route('/cds/<title>', methods=['GET'])
def get_cd_view(title):
    res = requests.get('http://localhost:5000/api/cds/' + title)
    cd = json.loads(res.content)
    return render_template('cd_view.html', p=cd)

# ----------------------------------------------------BACKEND
@app.route('/api/cds/<title>', methods=['GET'])
def api_get_cd(title):
    p = find_one(title)
    return json.dumps(p)

# ------------------------------------------------- Add New CD --------------------------------
# ----------------------------------------------------FRONTEND
@app.route('/cds/novocd')
def new_cd_view():
    return render_template('add_cd_view.html')

@app.route('/cds/novocd',methods=['POST'])
def post_cd():
    data = dict(request.form)
    requests.post('http://localhost:5000/api/cds/novocd', data=data)
    return redirect('http://localhost:5000/')
# ----------------------------------------------------BACKEND

@app.route('/api/cds/novocd',methods=['POST'])
def api_post_cd():
    data = dict(request.form)
    insert(data)
    return json.dumps(find_all())

# -------------------------------------------------  Apagar CD --------------------------------
# ----------------------------------------------------FRONTEND
@app.route('/delete/<title>', methods=['POST'])
def delete_cd(title):
    requests.post('http://localhost:5000/api/cds/'+ title)
    return redirect('http://localhost:5000/')

# ----------------------------------------------------BACKEND
@app.route('/api/cds/<title>', methods=['POST'])
def api_delete_cd(title):
    p = delete(title)
    return json.dumps(p)

# ----------------------------------------------- Atualizar CD --------------------------------
# ----------------------------------------------- FRONTEND -------------------------
# ----------------------------------------------- Atualizar CD --------------------------------
# ----------------------------------------------- FRONTEND -------------------------
@app.route('/update/<title>', methods=['GET'])
def get_update_cd(title):
    res = requests.get('http://localhost:5000/api/cds/'+ title)
    cd = json.loads(res.content)
    return render_template('atualiza_cd_view.html', p = cd)

@app.route('/update/<title>', methods=['POST'])
def update_cd(title):
    data = dict(request.form)
    requests.post('http://localhost:5000/api/update/'+ title, data=data)
    return redirect('http://localhost:5000/cds/'+ title)

# ----------------------------------------------- Procurar CD ---------------------------------
@app.route('/', methods=['POST'])
def procura_cd():
    userinput = request.form.get('userinput')                       # Retorna o que o user põe no editbox
    res = requests.get('http://localhost:5000/api/cds')             # Faz o request á API dos cds
    ps = json.loads(res.content)                                    # conjunto de cds existentes
    lista_cds_encontrados=[]

    for title in ps:                                                # Por cada CD encontrado
        cd=find_one(title)
        res = requests.get('http://localhost:5000/api/cds/'+ title)
        cd = json.loads(res.content)                                 # Encontra o cd por titulo
        conteudo=cd                                                  # Vai buscar o conteudo do cd
        res1=re.findall(rf"(?i)\b{userinput}\b",str(conteudo))          # Percorre á procura do userinput no conteudo
        if res1:                                                     # Se for possivel correr o res
            if title not in lista_cds_encontrados:                   # Se o titulo nao estiver na lista que foi armazenando os encontrados
                lista_cds_encontrados.append(title)                  # Adiciona o titulo á lista

    if (len(lista_cds_encontrados) == 1):
        res2 = requests.get('http://localhost:5000/api/cds/' + lista_cds_encontrados[0])
        cd = json.loads(res2.content)
        return render_template('cd_view.html', p=cd) # com o cd

    elif (len(lista_cds_encontrados)>1):
        print(lista_cds_encontrados)
        i=0
        cds={}
        for i in range(len(lista_cds_encontrados)):
            print(i)            
            res3 = requests.get('http://localhost:5000/api/cds/' + lista_cds_encontrados[i])
            print (res3)
            cd = json.loads(res3.content)
            cds[i] = cd['title']
            print (cds)

        print(cds)
            
        return render_template('search_results.html', p=cds) # Lista de encontrados ( titulo com link )

    if (len(lista_cds_encontrados)<1):
        # flash ('No results found!')
        return redirect ('/') # Não encontrado """ 

    path = os.getcwd() + '/gp8/main.py'
    main_out = open(path, 'w', encoding='utf-8')
    main_out.write(contentmain)
    main_out.close()

# Instalar e correr o Servidor com FLASK 

def install_env():
    os.system('cmd /c "cd gp8 & py -3 -m venv env"')

def openserver():
    os.system('cmd /k "cd gp8 & env\Scripts\activate & pip install Flask & pip install requests & pip install regex & set FLASK_APP=main.py & flask run"')

def openweb():
        time.sleep(5)
        webbrowser.open('http://127.0.0.1:5000/')

def multiprocessing():
        if __name__ == '__main__':
            Thread(target = openserver).start()
            Thread(target = openweb).start()
# Main 

def main():
	create_dirs()
	criarbase()
	criarindex()
	criarcd()
	adicionarcd()
	atualizarcd()
	informaad()
	procuraresultado()
	createdb_cd()
	createmain()
	install_env()
	multiprocessing()
main() 
