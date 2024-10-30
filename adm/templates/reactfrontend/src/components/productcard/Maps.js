import React from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

export default class Maps extends React.Component {
    render() {
        const sliderSettings = {
            dots: true,
            infinite: true,
            speed: 500,
            slidesToShow: 1, // Exibe um slide por vez
            slidesToScroll: 1,
            arrows: true
        };

        // Dados dos produtos
        const products = [
            {
                nome: "Açaí",
                tipo: ["Açaí Tradicional", "Açaí Batido com Morango"],
                adicionais: ["Leite em Pó", "Paçoca", "Disquete", "Amendoin", "Ovo Maltine", "Choco Ball", "Granola", "Jujuba", "Leite Condensado", "Banana"],
                adicionaispagos: [{ "Kiwi": "R$ 2,00", "Creme de Cupuaçu": "R$ 3,00", "Creme de Ninho": "R$ 3,00", "Creme de Maracujá": "R$ 3,00", "Bis": "R$ 2,00", "Nutella": "R$ 5,00" }],
                imagem: "/img/acai.png",
            },
            {
                nome: "Sorvete",
                tipo: ["Casquinha", "Cascão"],
                adicionais: ["Ovo Maltine", "Leitinho Trufado", "Flocos", "Morango", "Chiclete", "Chocolate", "Blue Ice", "Leite Condensado", "E mais..."],
                adicionaispagos: [{ "Bola": "R$ 4,00" }],
                imagem: "/img/Sorvete.png",
            },

        ];

        return (
            <div id="informacoes" className="information">
                <img className="imgsorvete5" src="/img/sorvete.svg" alt="Sorvete 1" />
                <img className="imgsorvete6" src="/img/sorvete.svg" alt="Sorvete 2" />
                <img className="imgacai11" src="/img/acai.svg" alt="Açaí 1" />
                <img className="imgacai12" src="/img/acai.svg" alt="Açaí 2" />
                <img className="imgacai13" src="/img/acai.svg" alt="Açaí 3" />
                <img className="imgacai14" src="/img/acai.svg" alt="Açaí 4" />
                <img className="imgacai15" src="/img/acai.svg" alt="Açaí 5" />

                <div className="product-carousel">
                    <Slider {...sliderSettings}>
                        {products.map((product, index) => (
                            <div key={index} className="product-card1">
                                <div className="product-content">
                                    <img className="product-image" src={product.imagem} alt={product.nome} />

                                    <div className="product-text1"> Tipos:
                                        {product.tipo.map((tipo, id) => (
                                            <p key={id} className="product-description">{tipo}</p>
                                        ))}
                                    </div>

                                    {product.nome === "Açaí" && (
                                        <>
                                            <div className="product-text1"> Adicionais:
                                                {product.adicionais.map((adc, id) => (
                                                   <p key={id} className="product-description"><li>{adc}</li></p>
                                                ))}
                                            </div>

                                            <div className="product-text1"> Adicionais Pagos:
                                                {Object.entries(product.adicionaispagos[0]).map(([item, preco], id) => (
                                                    <p key={id} className="product-description">{item}: {preco}</p>
                                                ))}
                                            </div>
                                        </>
                                    )}

                                    {product.nome === "Sorvete" && (
                                        <>
                                            <div className="product-text1"> Sabores:
                                                {product.adicionais.map((adc, id) => (
                                                    <p key={id} className="product-description"><li>{adc}</li></p>
                                                ))}
                                            </div>

                                            <div className="product-text1"> Valores:
                                                {Object.entries(product.adicionaispagos[0]).map(([item, preco], id) => (
                                                    <p key={id} className="product-description">{item}: {preco}</p>
                                                ))}
                                            </div>
                                        </>
                                    )}
                                    
                                </div>
                            </div>
                        ))}
                    </Slider>
                </div>
            </div>

        );
    }
}
