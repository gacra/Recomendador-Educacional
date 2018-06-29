import React from 'react'

class QuestionCard extends React.Component{

    render(){
        return(
            <div className='col s12 m10 offset-m1'>
                <div className='card grey lighten-5'>
                    <div className='card-content'>
                        <span className="card-title orange-text accent-4-text">{this.props.index}</span>
                        <p>{this.props.stem}</p>
                    </div>
                </div>
            </div>
        );
    }

}

export default QuestionCard