import React from 'react'

import '../../index.css'

class QuestionCard extends React.Component{

    chipStyle = {
        marginBottom: "13px"
    }

    constructor(props) {
        super(props);
        this.changeSelectedAlternative = this.changeSelectedAlternative.bind(this)
    }

    changeSelectedAlternative(event) {
        this.props.changeSelectedAlternative(event);
    }

    getCardColor() {
        if(this.props.unanswered === true) {
            return "yellow lighten-4";
        }
        return "grey lighten-5"
    }

    render(){
        let questionIndex = this.props.index;
        let title = "Pergunta " + (questionIndex + 1) + " (de " + this.props.total + ")";
        let {stem, alternatives, topic, _id} = this.props.question;
        let self = this;

        let alternativesRadio = alternatives.map((item, index)=>{
            return(
               <p key={index}>
                   <label>
                       <input className="with-gap"
                              name={_id} type="radio"
                              value={index}
                              onChange={self.changeSelectedAlternative}
                       />
                       <span className="textGray">{item}</span>
                   </label>
               </p>
           ) ;
        });

        return(
            <div className='col s12 m10 offset-m1'>
                <div className={'card ' + this.getCardColor()}>
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