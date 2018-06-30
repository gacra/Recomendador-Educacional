import React from 'react'

import '../../index.css'

class QuestionCard extends React.Component{

    chipStyle = {
        marginBottom: "13px"
    }

    constructor(props) {
        super(props);
    }

    render(){
        let questionIndex = this.props.index;

        let title = "Pergunta " + (questionIndex + 1) + " (de " + this.props.total + ")";

        let {stem: stem, alternatives: alternatives, topic:topic} = this.props.question;

        let alternativesRadio = alternatives.map((item, index)=>{
           return(
               <p key={index}>
                   <label>
                       <input className="with-gap" name={questionIndex} type="radio"/>
                       <span className="textGray">{item}</span>
                   </label>
               </p>
           ) ;
        });

        return(
            <div className='col s12 m10 offset-m1' key={questionIndex}>
                <div className='card grey lighten-5'>
                    <div className='card-content'>
                        <span className="card-title orange-text accent-4-text">{title}</span>
                        <div className="chip" style={this.chipStyle}>
                            {this.props.topics[topic]}
                        </div>
                        <p>{stem}</p>
                        <form action="#">
                            {alternativesRadio}
                        </form>
                    </div>
                </div>
            </div>
        );
    }

}

export default QuestionCard