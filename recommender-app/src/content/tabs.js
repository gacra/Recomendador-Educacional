import React from 'react';
import colors from '../utils';

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
            let color = activeTab === index ? colors.orangeSecondary : colors.orangeTertiary;

            let className = "tab col s3 " + color;

            return (
                <li key={index} className={className} onClick={self.changeActiveTab.bind(null, index)}>
                    <a style={{cursor: 'pointer'}} className={colors.orangeText}>
                        <b>{value}</b>
                    </a>
                </li>
            )
        });

        return (
            <div className="col s12">
                <div className="card white">
                    <ul className="tabs">
                        {tabs}
                    </ul>
                </div>
            </div>
        );
    }

}

export default Tabs;