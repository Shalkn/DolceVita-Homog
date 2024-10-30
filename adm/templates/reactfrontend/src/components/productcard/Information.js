import React from "react";
import AnchorLink from 'react-anchor-link-smooth-scroll';

export default class Information extends React.Component {
    render(){
        return(
            <div className="inicio" id="inicio">
                <img className="imglogo" src="/img/DolceVitta1.svg" alt="Logo Dolce Vitta" />
                <img className="imgletreiro" src="/img/acaiesorveteria1.svg" alt="Açaí e Sorveteria" />
                <img className="imgsorvete1" src="/img/sorvete.svg" alt="Sorvete 1" />
                <img className="imgsorvete2" src="/img/sorvete.svg" alt="Sorvete 2" />
                <img className="imgacai1" src="./img/acai.svg" alt="Açaí 1" />
                <img className="imgacai2" src="/img/acai.svg" alt="Açaí 2" />
                <img className="imgacai3" src="/img/acai.svg" alt="Açaí 3" />
                <img className="imgacai4" src="/img/acai.svg" alt="Açaí 4" />
                <img className="imgacai5" src="/img/acai.svg" alt="Açaí 5" />
            </div>
        );
    }
}