import React from "react";


export default class Slide extends React.Component {
    render() {
        return (

            <div id="contato" className="contact">
                <img className="imgsorvete7" src="/img/sorvete.svg" alt="Sorvete 1" />
                <img className="imgsorvete8" src="/img/sorvete.svg" alt="Sorvete 2" />
                <img className="imgacai16" src="/img/acai.svg" alt="Açaí 1" />
                <img className="imgacai17" src="/img/acai.svg" alt="Açaí 2" />
                <img className="imgacai18" src="/img/acai.svg" alt="Açaí 3" />
                <img className="imgacai19" src="/img/acai.svg" alt="Açaí 4" />
                <img className="imgacai20" src="/img/acai.svg" alt="Açaí 5" />

                <div className="contact-info">
                    <div className="contact-info-1">
                        <img className="delivery" src="/img/Delivery.svg" alt="Delivery" />
                        <p className="Titulo-Contact">Temos Delivery, Faça Seu Pedido </p>
                        <p className="Horario-Contact">Horário de Atendimento: Sábado à Quinta-Feira das 17h às 2h.</p>
                        <p className="End-Contact">Av. Existente, 4 - Pedra 90, Cuiabá - MT, CEP: 78099-000</p>


                    </div>

                    <div className="contact-info-2">
                        <iframe src="https://maps.google.com/maps?q=15%C2%B038%2704.2%22S+55%C2%B057%2733.1%22W&t=&z=19&ie=UTF8&iwloc=&output=embed" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
                    </div>
                </div>

            </div>

        );
    }
}