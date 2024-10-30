Cores Escolhidas "https://www.behance.net/gallery/99552617/Acai-do-Rei"

Primária #3A0930
Secundária #FF862C
Terciária #006059
Quarternária #FFEEE2


Templates:

https://blog.hubspot.com/website/bootstrap-form-template


GIT BÁSICO

terminal como adm, executa na pasta do projeto, "git init"

cria arquivo na pasta do projeto chamado .gitignore
para ignorar os arquivos é necessário usar: "**/nome do arquivo ou pasta"

cadastrar autor
git config user.email "colocar seu e-mail vinculado a conta git"
git config user.name "escolher um nome para identificação"

Criar repositório no github, colocando apenas o nome que quer.

git add . (adiciona todos os arquivos)
git commit -m "nome do commit"
git push (envia todos os arquivos para seu repositório)
Caso você não tenha o repositório é necessário adicionar o repositório do github

git remote add orgin "link do repositório"

Caso dê erro: possivelmente é necessário criar uma branch, visto que é o tipo de Classificação do git sobre versionamento, o caso mais comum é usar master eu uso main

git push --set-upstream origin main

É possível que peça para que você faça o login no git hub, caso não tiver realizado anteriormente.



Estrtura REACT JS
/src/
    /components/
      Header.js
      ProductCard.js
      Footer.js
    /pages/
      Home.js
      Products.js
      About.js

Usando api backend

import axios from 'axios';
import React from 'react';

class App extends React.Component {
  state = { details: [], }
  server = 'http://localhost:8000';
  

componentDidMount() {
  
  let data;
  axios.get('http://localhost:8000/prod/')
  
  .then(res => {
    data = res.data;
    this.setState({
      details: data
    });
    
  })
  
  .catch(err => { })
}

render(){
  return (
    <div>
    <header>Gerado Pelo Django</header>
    
    <hr></hr>
    
    
    {this.state.details.map((data, id) => (
      <div key={id}>
        
          <div type="table">
            <div scope="row"></div>
            <div>{id}</div>
            <div>{data.nome}</div>
            <div>{data.descricao}</div>
            <div>{data.preco}</div>
            <div>{data.status}</div>
            <div>{data.peso}</div>
            {/* <img className={"img"} src={this.server + data.imagem}/> */}
          </div>
        
        
      </div>
      
    ))}
    
    </div>
    
 
    
  )
}
}
export default App;


detro de packge-lock.json na raiz do react para trocar a porta do servidor coloque o código:

Original:
"scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },

Alterando a Porta:

"scripts": {
    "start": "set PORT=8000 && react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },