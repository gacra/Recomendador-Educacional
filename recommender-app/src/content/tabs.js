import React from 'react';
import colors from '../utils';

import '../index.css'

class Tabs extends React.Component {

    constructor(props) {
        super(props);
        this.changeActiveTab = this.changeActiveTab.bind(this);
    }


    changeActiveTab(index) {
        this.props.changeActiveTab(index);
    }

    render() {
        let activeTab = this.props.activeTab;
        let self = this;
        let tabs = this.props.tabNames.map((value, index) => {
            let color = activeTab === index ? colors.orangeTertiary : "";

            let className = "tab col s3 " + color;

            return (
                <li key={index} className={className} onClick={self.changeActiveTab.bind(null, index)}>
                    <a style={{cursor: 'pointer'}} className={colors.orangeText}>
                        <b>{value}</b>
                    </a>
                </li>
            )
        });

        let offsetIndicator = "offset-s" + (activeTab*6) + " offset-l" + (activeTab*3);

        return (
            <div className="col s12">
                <div className="card white">
                    <ul className="tabs" id={"tabs"}>
                        {tabs}
                        <li className={"indicator col s6 l3 " + offsetIndicator + " " + colors.deepOrange}></li>
                    </ul>
                </div>
            </div>
        );
    }

}

export default Tabs;