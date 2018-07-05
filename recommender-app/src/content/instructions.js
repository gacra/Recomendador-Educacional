import React from 'react';

class Instructions extends React.Component {

    headerStyle = {
        fontSize: "180%",
        margin: "0.3rem 0 1.0rem 0"
    };

    render() {
        return (
            <div className="col s10 offset-m1">
                <h1 style={this.headerStyle}>{this.props.text}</h1>
                {this.props.subText &&
                    <p>{this.props.subText}</p>
                }
            </div>
        );
    }

}

export default Instructions;