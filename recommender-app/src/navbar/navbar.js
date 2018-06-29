import React from 'react';

import '../index.css'
import colors from '../utils'

class Navbar extends React.Component {

    render() {

        let iconStyle = {
            fontSize: "40px"
        }

        return (
            <div className="navbar-fixed">
                <nav>
                    <div className={"nav-wrapper " + colors.orangePrimary}>
                        <div className="re-container">
                            <a href="" className="brand-logo">
                                <i className="material-icons" style={iconStyle}>not_listed_location</i>
                                <b>ñ</b> sei o que <b>ñ</b> sei
                            </a>
                            <ul id="nav-mobile" className="right hide-on-med-and-down">
                                <li>
                                    <a href="https://github.com/gacra/Recomendador-Educacional"
                                       target="_blank" rel="noopener noreferrer">
                                        <i className="material-icons left">code</i>
                                        Código fonte
                                    </a>
                                </li>
                                <li>
                                    <a href="https://www.linkedin.com/in/guilherme-jos%C3%A9-acra-6a5b7a11a/"
                                       target="_blank" rel="noopener noreferrer">
                                        <i className="material-icons left">person</i>
                                        Contato
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </div>
        );
    }

}

export default Navbar;