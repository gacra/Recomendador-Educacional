import React from 'react'
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import LinearProgress from '@material-ui/core/LinearProgress';
import Divider from '@material-ui/core/Divider';

import colors from '../../colors';
import {withStyles} from "@material-ui/core/styles/index";

const styles = {
    title: {
        color: colors.orangeText
    },
    similarityGrid: {
        paddingTop: 10,
        paddingLeft: 10
    },
    link: {
        color: colors.link
    },
    summary: {
        color: colors.grayText
    },
    divider: {
        marginTop: 15
    }
};

const minSimilarity = 30;

class Material extends React.Component {

    render() {
        const { classes } = this.props;

        let {title, type, summary, link, similarity} = this.props.material;

        let color = (similarity*100 >= minSimilarity)? {}: {color:"secondary"};

        return(
            <Grid item xs={10} md={8}>
                <Typography variant="subheading" gutterBottom className={classes.title}>
                    <a href={link} target="_blank" rel="noopener noreferrer">
                        {(type !== 'html')? '[' + type.toUpperCase() + ']  ': ''}
                        {title}
                    </a>
                </Typography>
                <Grid container spacing={0}>
                    <Grid item>
                        <Typography variant="body2" gutterBottom>
                            Relevância:
                        </Typography>
                    </Grid>
                    <Grid item xs={5} md={3} className={classes.similarityGrid}>
                        <LinearProgress {...color} variant="determinate" value={similarity*100}/>
                    </Grid>
                </Grid>
                <Typography variant="body1" gutterBottom className={classes.link}>
                    <a href={link} target="_blank" rel="noopener noreferrer">{link}</a>
                </Typography>
                <Typography gutterBottom className={classes.summary}>
                    {summary}
                </Typography>
                <Divider className={classes.divider}/>
            </Grid>
        );
    }

}

export default withStyles(styles)(Material)