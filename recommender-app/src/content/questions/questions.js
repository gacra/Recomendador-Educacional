import React from 'react'
import axios from 'axios';

import Instructions from '../instructions'
import QuestionCard from './card'

class QuestionCardList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {questionsData: [], total: 0}
    }

    componentWillMount() {
        let self = this;
        axios.get('http://localhost:8000/questions/topics=/').then(function (response) {
            self.setState({
                questionsData: response.data,
                total: response.data.length
            });
        });
    }

    render() {
        let questions = this.state.questionsData;

        console.log(questions);

        let cardList = questions.map((item, index) => {
            return <QuestionCard key={index} index={index}
                                 total={this.state.total}
                                 question={item}
                                 topics={this.props.topics}/>
        });

        return (
            <div className='col s12'>
                <Instructions text="Responda as seguintes perguntas:"/>
                {cardList}
            </div>

        );
    }

}

export default QuestionCardList