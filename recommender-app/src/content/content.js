import React from 'react';
import axios from 'axios';

import Tabs from './tabs'
import Questions from './questions/questions'

class Content extends React.Component {

    tabNames = ['Perguntas', 'Materiais recomendados'];

    constructor(props) {
        super(props);
        this.state = {activeTab: 0, topics: {}};
        this.changeActiveTab = this.changeActiveTab.bind(this);
    }

    componentWillMount(){
        let self = this;
        axios.get('http://localhost:8000/topics/').then(function (response) {
            let topics = {};

            response.data.forEach((item)=>{
                topics[item["code"]] = item["description"];
            });

            self.setState({
                topics: topics
            });

            console.log(topics)
        });
    }

    changeActiveTab(index) {
        this.setState({activeTab: index})
        window.scroll(0, this.props.descriptionRef.current.clientHeight)
    }

    render() {
        return (
            <div className="row">
                <Tabs
                    tabNames={this.tabNames}
                    activeTab={this.state.activeTab}
                    changeActiveTab={this.changeActiveTab}
                />
                <Questions topics={this.state.topics}/>
            </div>
        );
    }

}

export default Content;
