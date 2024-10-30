import React from "react";
import Nav from "./header/Nav";
import Logo from "./header/Logo";
import Adress from "./header/Adress";


export default class Header extends React.Component {
    render(){
        return(
            <div className="header">
                <Nav />
                <Logo />
                <Adress />
            </div>
        );
    }
}