import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';


class Instructions extends React.Component {

    render() {
        return (
            <Grid item xs={10} md={8}>
                <Typography variant="headline" gutterBottom>
                    {this.props.text}
                </Typography>
                <Typography variant="body1" gutterBottom>
                    {this.props.subText}
                </Typography>
            </Grid>
        )
    };

}

export default Instructions;