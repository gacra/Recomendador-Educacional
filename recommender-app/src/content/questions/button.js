import React from 'react'

class Button extends React.Component{

    constructor(props) {
        super(props);
        this.clickButton = this.clickButton.bind(this);
    }

    clickButton() {
        this.props.clickButton();
    }

    render() {
        return (
            <div className='col s12 m10 offset-m1'>
                <a className={"col s12 waves-effect waves-light btn-large"} onClick={this.clickButton}><b>Concluir questionário</b></a>
            </div>
        );
    }

}

export default Button;