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

    componentWillMount() {
        let self = this;
        axios.get('http://localhost:8000/topics/').then(function (response) {
            let topics = {};

            response.data.forEach((item) => {
                topics[item["code"]] = item["description"];
            });

            self.setState({
                topics: topics
            });

        });
    }

    changeActiveTab(index) {
        this.setState({activeTab: index})
    }

    render() {
        return (
            <div className="row">
                <Tabs
                    tabNames={this.tabNames}
                    activeTab={this.state.activeTab}
                    changeActiveTab={this.changeActiveTab}
                />
                <Questions topics={this.state.topics} descriptionRef={this.props.descriptionRef}/>
            </div>
        );
    }

}

export default Content;
