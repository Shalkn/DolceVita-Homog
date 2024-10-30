import React from "react";
import Contact from "./productcard/Contact";
import Information from "./productcard/Information";
import Maps from "./productcard/Maps";
import Slide from "./productcard/Slide";


export default class ProductCard extends React.Component {
    render() {
        return (
            <div className="productcard">
                <Information />
                <Contact />
                <Maps />
                <Slide />
                <div className="rodape">
                    
                </div>
            </div>

        );
    }
}