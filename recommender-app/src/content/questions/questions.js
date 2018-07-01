import React from 'react'
import axios from 'axios';

import Instructions from '../instructions'
import QuestionCard from './card'
import Button from './button'

class QuestionCardList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {questionsData: [], total: 0, questionsAnswers: {}, unansweredQuestions: []}
        this.changeSelectedAlternative = this.changeSelectedAlternative.bind(this)
        this.clickButton = this.clickButton.bind(this)
    }

    componentWillMount() {
        let self = this;
        axios.get('http://localhost:8000/questions/topics=/').then(function (response) {
            let questions = response.data;
            let questionsAnswers = {};

            questions.forEach((item) => {
                questionsAnswers[item._id] = -1;
            });

            self.setState({
                questionsData: questions,
                total: questions.length,
                questionsAnswers: questionsAnswers
            });
        });
    }

    changeSelectedAlternative(event) {
        let questionId = event.target['name'];
        let alternative = parseInt(event.target['value'], 10);

        this.setState((prevState) => {
           let questionsAnswers = prevState.questionsAnswers;

           questionsAnswers[questionId] = alternative;

           return {questionsAnswers: questionsAnswers};
        });
    }

    clickButton() {
        let unanswered = checkUnanswered(this.state.questionsAnswers);
        this.setState({unansweredQuestions: unanswered});
    }

    render() {
        let questions = this.state.questionsData;

        let cardList = questions.map((item, index) => {
            let unanswered = this.state.unansweredQuestions.includes(item._id);
            return <QuestionCard key={index}
                                 index={index}
                                 total={this.state.total}
                                 question={item}
                                 topics={this.props.topics}
                                 changeSelectedAlternative={this.changeSelectedAlternative}
                                 unanswered={unanswered}/>
        });

        return (
            <div className='col s12'>
                <Instructions text="Responda as seguintes perguntas:"/>
                {cardList}
                <Button clickButton={this.clickButton}/>
            </div>

        );
    }

}

var checkUnanswered = (questionsAnswers) => {
    let unanswered = [];
    for(var key in questionsAnswers) {
        if(questionsAnswers[key] === -1) {
            unanswered.push(key);
        }
    }
    return unanswered;
}

export default QuestionCardList