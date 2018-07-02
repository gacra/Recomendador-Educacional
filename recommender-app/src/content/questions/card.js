import React from 'react'

import colors from '../../utils'

import '../../index.css'

class QuestionCard extends React.Component {

    chipStyle = {
        marginBottom: "13px"
    }

    constructor(props) {
        super(props);
        this.state = {selectedAlternative: -1};
        this.changeSelectedAlternative = this.changeSelectedAlternative.bind(this)
    }

    changeSelectedAlternative(event) {
        let questionId = event.target['name'];
        let alternative = parseInt(event.target['value'], 10);
        this.setState({selectedAlternative: alternative})
        this.props.changeSelectedAlternative(questionId, alternative);
    }

    getCardColor() {
        let correctAlternative = this.props.correctAlternative;
        let selectedAlternative = this.state.selectedAlternative;
        let unanswered = this.props.unanswered;

        if (unanswered === true) {
            return colors.warningCard;
        } else if (correctAlternative !== false) {
            let rightAnswers = correctAlternative === selectedAlternative;
            if (rightAnswers) {
                return colors.rightCard;
            } else {
                return colors.wrongCard;
            }
        }
        return colors.normalCard;
    }

    render() {
        let questionIndex = this.props.index;
        let title = "Pergunta " + (questionIndex + 1) + " (de " + this.props.total + ")";
        let {stem, alternatives, topic, _id} = this.props.question;
        let self = this;

        let alternativesRadio = alternatives.map((item, index) => {
            let correctAlternative = this.props.correctAlternative;

            let input;
            if (correctAlternative !== false) {
                input = (<input className="with-gap"
                                name={_id} type="radio"
                                value={index}
                                onChange={self.changeSelectedAlternative}
                                disabled="disabled"/>)
            } else {
                input = (<input className="with-gap"
                                name={_id} type="radio"
                                value={index}
                                onChange={self.changeSelectedAlternative}/>)
            }

            let alternativeText;
            if (correctAlternative === index) {
                alternativeText = (<span className={colors.rightAlternativeText}><b>{item}</b></span>)
            } else {
                alternativeText = (<span className="textGray">{item}</span>);
            }

            return (
                <p key={index}>
                    <label>
                        {input}
                        {alternativeText}
                    </label>
                </p>
            );
        });

        return (
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