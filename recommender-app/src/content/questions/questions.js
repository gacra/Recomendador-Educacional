import React from 'react'
import axios from 'axios';

import QuestionCard from './card'

class QuestionCardList extends React.Component{
    constructor(props){
        super(props);
        this.state = {questionsData: []}
    }

    componentDidMount(){
        let self = this;
        axios.get('http://localhost:8000/questions/topics=/').then(function (response) {
            self.setState({
                questionsData: response.data
            });
        });
    }

    render(){
        let questions =  this.state.questionsData;

        console.log(questions);

        let cardList = questions.map((item, index) => {
            return <QuestionCard index={index} stem={item.stem}/>
        });

        return(
            <div className='row'>
                {cardList}
            </div>

        );
    }

}

export default QuestionCardList